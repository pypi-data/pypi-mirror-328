import logging,os,json,time,requests
import pandas as pd
import mplfinance as mpf
from ...query_functions.call_functions import get_transactions
from ..user_txns.transaction_history import process_transaction_history
from ...utils import convert_chart_data_keys_to_int,get_timestamps,get_sorted_txn_history, get_txn_price,get_sol_amount, get_user_address,convert_timestamp_to_datetime,get_sorted_txn_history
def generate_price_chart(txn_history=None,pair_id=None,save_path=None):
    """
    Generates a candlestick chart with volume indicators from transaction history.

    Parameters:
        txn_history (list of dict): The transaction history data.
        save_path (str): Path to save the generated chart image.

    Returns:
        None
    """
    new_history = []
    if not txn_history and pair_id != None:
        txn_history = get_transactions(pair_id=pair_id)
    elif isinstance(txn_history,int):
        txn_history = get_transactions(pair_id=txn_history)
    save_path = save_path or os.path.join(os.getcwd(),"chart.png")
    txn_history = get_sorted_txn_history(txn_history)
    # Step 1: Prepare transaction data
    for i, txn in enumerate(txn_history):
        if isinstance(txn,list):
            txn = txn[0]
        try:
            txn['timestamp'] = get_timestamps(txn)
            txn['price'] = get_txn_price(txn)
            txn['volume'] = get_sol_amount(txn)
            txn['user_address'] = get_user_address(txn)
            new_history.append(txn)
        except Exception as e:
            print(f"{e} and txn == {txn}")
    txn_history = new_history
    if not isinstance(txn_history, list) or not all(isinstance(item, dict) for item in txn_history):
        raise ValueError("txn_history must be a list of dictionaries with keys 'timestamp', 'price', and 'volume'.")

    # Step 2: Process and create DataFrame
    processed_txns = process_transaction_history(txn_history)
    processed_txns['save_path']=save_path
    processed_data = processed_txns.get('processed_data')
    try:
        df = pd.DataFrame(processed_data)
    except Exception as e:
        raise ValueError(f"Error creating DataFrame from transaction history: {e}")
    
    if df.empty:
        raise ValueError("DataFrame is empty after processing transaction history.")
    
    # Check for required columns
    required_columns = ['timestamp', 'price', 'volume']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column '{col}' in transaction history. Columns found: {df.columns.tolist()}")
    
    # ** Step 3: Ensure numeric columns **
    try:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
        
        # Drop any rows where price or volume are NaN
        df.dropna(subset=['price', 'volume'], inplace=True)
        
        if df.empty:
            raise ValueError("DataFrame is empty after converting price and volume to numeric and dropping NaN values.")
    except Exception as e:
        raise ValueError(f"Error converting price and volume columns to numeric: {e}")
    
    # ** Step 4: Convert timestamp to datetime and set as index **
    try:
        df['datetime'] = pd.to_datetime(df['timestamp'], unit='s', errors='coerce', utc=True)        
        if df['datetime'].isnull().all():
            raise ValueError("All timestamps failed to convert. Check 'timestamp' column values.")
        
        # Set the datetime as the index
        df.set_index('datetime', inplace=True)
        df.sort_index(inplace=True)
    except Exception as e:
        raise ValueError(f"Error converting 'timestamp' to 'datetime': {e}")
    
    # ** Step 5: Resample DataFrame into OHLC and Volume for 1-minute intervals **
    try:
        ohlc_dict = {'price': 'ohlc', 'volume': 'sum'}
        df_resampled = df.resample('1min').agg(ohlc_dict).dropna(how='any')
        
        if df_resampled.empty:
            raise ValueError("No data available after resampling. Check if timestamps are too sparse.")
        
        print("Columns after resampling and flattening:", df_resampled.columns)
    except Exception as e:
        raise ValueError(f"Error resampling DataFrame: {e}")
    
    # ** Step 6: Flatten multi-level columns and rename them for mplfinance **
    try:
        df_resampled.columns = ['_'.join(col) if isinstance(col, tuple) else col for col in df_resampled.columns]
        df_resampled.rename(columns={
            'price_open': 'Open', 
            'price_high': 'High', 
            'price_low': 'Low', 
            'price_close': 'Close', 
            'volume_volume': 'Volume'
        }, inplace=True)
        
        #print("Renamed columns after flattening:", df_resampled.columns)
        
        if 'Volume' not in df_resampled.columns:
            raise ValueError(f"'Volume' column is missing. Current columns: {df_resampled.columns}")
    except Exception as e:
        raise ValueError(f"Error renaming DataFrame columns: {e}")
    
    # ** Step 7: Plot the candlestick chart **
    try:
        mc = mpf.make_marketcolors(up='g', down='r', inherit=True)
        s = mpf.make_mpf_style(marketcolors=mc)

        mpf.plot(
            df_resampled,
            type='candle',
            style=s,
            volume=True,
            savefig=dict(fname=save_path, format='png', bbox_inches='tight')
        )
        try:
            chart_data = df_resampled.to_dict()
            
            converted_chart_data_int = convert_chart_data_keys_to_int(chart_data)
            processed_txns['chart_data']=converted_chart_data_int
        except Exception as e:
            print(f"Error plotting candlestick chart: {e}")
    except Exception as e:
        raise ValueError(f"Error plotting candlestick chart: {e}")
    print(f"Chart saved to {save_path}")
    return processed_txns
