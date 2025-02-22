import logging
import psycopg2
from psycopg2.extras import RealDictCursor
from abstract_security import get_env_value
import traceback

# Configure logging once with a consistent format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

# Environment setup
ENV_PATH = '/home/solcatcher/.env'

def get_env_val(key, default=None):
    """Retrieve environment variable with optional default."""
    return get_env_value(key=key, path=ENV_PATH) or default

# Centralized configuration
CONFIG = {
    'RABBITMQ': {
        'HOST': get_env_val("SOLCATCHER_AMQP_HOST", 'solcatcher.io'),
        'PORT': get_env_val("SOLCATCHER_AMQP_PORT", '5672'),
        'USER': get_env_val("SOLCATCHER_AMQP_USER", 'solcatcher'),
        'NAME': get_env_val("SOLCATCHER_AMQP_NAME", 'solcatcher'),
        'PASSWORD': get_env_val("SOLCATCHER_AMQP_PASSWORD"),
    },
    'POSTGRESQL': {
        'HOST': get_env_val("SOLCATCHER_POSTGRESQL_HOST", 'solcatcher.io'),
        'PORT': get_env_val("SOLCATCHER_POSTGRESQL_PORT", '5432'),
        'USER': get_env_val("SOLCATCHER_POSTGRESQL_USER", 'solcatcher'),
        'NAME': get_env_val("SOLCATCHER_POSTGRESQL_NAME", 'solcatcher'),
        'PASSWORD': get_env_val("SOLCATCHER_POSTGRESQL_PASSWORD"),
    }
}

DB_URL = (
    f"postgresql://{CONFIG['POSTGRESQL']['USER']}:{CONFIG['POSTGRESQL']['PASSWORD']}"
    f"@{CONFIG['POSTGRESQL']['HOST']}:{CONFIG['POSTGRESQL']['PORT']}/{CONFIG['POSTGRESQL']['NAME']}"
)

def get_connection():
    """Establish a PostgreSQL connection."""
    return psycopg2.connect(
        dbname=CONFIG['POSTGRESQL']['NAME'],
        user=CONFIG['POSTGRESQL']['USER'],
        password=CONFIG['POSTGRESQL']['PASSWORD'],
        host=CONFIG['POSTGRESQL']['HOST'],
        port=CONFIG['POSTGRESQL']['PORT']
    )
def execute_query(query, values=None, fetch=True, as_dict=True):
    """
    Execute a SQL query and return results if applicable.
    
    Args:
        query (str): SQL query to execute.
        values (tuple, optional): Values for parameterized queries.
        fetch (bool): Whether to fetch results (for SELECT) or commit (for INSERT/UPDATE).
        as_dict (bool): Return results as dictionaries if True, else as tuples.
    
    Returns:
        list: Query results (empty if no fetch or error).
    """
    logger.info(f"Executing query: {query} with values: {values}")
    conn = get_connection()
    cursor_factory = RealDictCursor if as_dict else None
    
    try:
        with conn.cursor(cursor_factory=cursor_factory) as cursor:
            cursor.execute(query, values)
            if fetch and query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
                if result:
                    logger.debug(f"First row: {result[0]}")
                return result
            conn.commit()
            return []
    except Exception as e:
        conn.rollback()
        logger.error(f"Query failed: {query}\nValues: {values}\nError: {e}\n{traceback.format_exc()}")
        return []
    finally:
        conn.close()

def get_all_table_names(schema='public'):
    """Fetch all table names from a specified schema."""
    query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = %s AND table_type = 'BASE TABLE';
    """
    result = execute_query(query, values=(schema,), fetch=True, as_dict=False)
    return [row[0] for row in result] if result else []

def query_data_as_dict(query, values=None, error="Error executing query:"):
    return execute_query(query=query, values=values, as_dict=True)

def get_query_result(query,values=None,zipit=False,**kwargs):
    """Executes a query and returns the results or commits the transaction."""
    result = execute_query(query,values=values, fetch=True, as_dict=zipit)
    return result
def query_data(query, values=None, error="Error executing query:", zipRows=True):
        """Execute a query and handle transactions with error management."""
        logging.info(f"query = {query} and values = {values}")
        result = execute_query(query, values=(schema,), fetch=True, as_dict=zipRows)
        return result
def aggregate_rows(query, values=None, errorMsg='Error Fetching Rows',fetch=True, as_dict=None,zipRows=None,zipit=None,**kwargs):
    if as_dict!=None:
        as_dict =as_dict
    elif zipRows!=None:
        as_dict =zipRows
    elif zipit!=None:
        as_dict =zipit
    
    return execute_query(query, values=values, fetch=True, as_dict=as_dict)
