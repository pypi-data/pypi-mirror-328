import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set level to INFO or higher
from psycopg2 import sql, connect
from psycopg2.extras import DictCursor,RealDictCursor
from abstract_utilities import make_list, SingletonMeta, is_number
from abstract_security import get_env_value
import psycopg2,time
env_path = '/home/solcatcher/.env'

def get_env_val(key):
    return get_env_value(key=key, path=env_path)

RABBITMQ_HOST = get_env_val("SOLCATCHER_AMQP_HOST") or 'solcatcher.io'
RABBITMQ_PORT = get_env_val("SOLCATCHER_AMQP_PORT") or '5672'
RABBITMQ_USER = get_env_val("SOLCATCHER_AMQP_USER") or 'solcatcher'
RABBITMQ_NAME = get_env_val("SOLCATCHER_AMQP_NAME") or 'solcatcher'
RABBITMQ_PASSWORD = get_env_val("SOLCATCHER_AMQP_PASSWORD") or 'solcatcher123'

POSTGRESQL_HOST = get_env_val("SOLCATCHER_POSTGRESQL_HOST") or 'solcatcher.io'
POSTGRESQL_PORT = get_env_val("SOLCATCHER_POSTGRESQL_PORT") or '5432'
POSTGRESQL_USER = get_env_val("SOLCATCHER_POSTGRESQL_USER") or 'solcatcher'
POSTGRESQL_NAME = get_env_val("SOLCATCHER_POSTGRESQL_NAME") or 'solcatcher'
POSTGRESQL_PASSWORD = get_env_val("SOLCATCHER_POSTGRESQL_PASSWORD") or 'solcatcher123!!!456'

DB_URL = f"postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_NAME}"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_connection():
    """Establish a database connection."""
    return psycopg2.connect(
        dbname=POSTGRESQL_NAME,
        user=POSTGRESQL_USER,
        password=POSTGRESQL_PASSWORD,
        host=POSTGRESQL_HOST,
        port=POSTGRESQL_PORT
    )
def query_data_as_dict(query, values=None, error="Error executing query:"):
    """Execute a query and return a list of dictionaries using RealDictCursor."""
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            try:
                cursor.execute(query, values)
                result = cursor.fetchall()
                # Return the result as a list of dicts
                return result
            except Exception as e:
                conn.rollback()
                logging.error("%s %s\nValues: %s\n%s", error, query, values, e)
                return []

def get_all_table_names(schema='public'):
    """Fetch all table names from a specified schema."""
    conn = get_connection()
    query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = %s AND table_type = 'BASE TABLE';
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (schema,))
            table_names = [row[0] for row in cursor.fetchall()]
            return table_names
    except Exception as e:
        print(f"An error occurred in get all tyables: {e}")
    finally:
        conn.close()


def get_query_result(query, conn):
    """Executes a query and returns the results or commits the transaction."""
    with conn.cursor() as cursor:
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            return cursor.fetchall()  # Return data for SELECT queries
        conn.commit()

def query_data(query, values=None, error="Error executing query:", zipRows=True):
        """Execute a query and handle transactions with error management."""
        logging.info(f"query = {query} and values = {values}")
        
        with get_connection() as conn:
            # Choose the cursor type based on whether you want to zip rows with column names
            cursor_factory = RealDictCursor if zipRows else None
            with conn.cursor(cursor_factory=cursor_factory) as cursor:
                try:
                    cursor.execute(query, values)
                    result = cursor.fetchall()
                    # Log the first row to see its structure
                    if result:
                        logging.info("First row data structure: %s", result[0])
                    return result
                except Exception as e:
                    conn.rollback()
                    logging.error("%s %s\nValues: %s\n%s", error, query, values, e)
def get_query_result(query, conn=None):
    conn = conn or getConnection()
    """Executes a query and returns the results or commits the transaction."""
    with conn.cursor() as cursor:
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            return cursor.fetchall()  # Return data for SELECT queries
        conn.commit()
def aggregate_rows(query, values=None, errorMsg='Error Fetching Rows'):
    conn = get_connection()
    cursor = None
    try:
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute(query, values)

        # Handle SELECT queries differently
        if query.strip().upper().startswith("SELECT"):
            try:
                results = cursor.fetchall()
                return results  # Return fetched rows
            except psycopg2.ProgrammingError as e:
                # No rows to fetch—return an empty list
                logger.warning(f"No rows to fetch for query: {query}")
                return []

        # Commit and return empty for non-SELECT queries
        conn.commit()
        return []
    except Exception as e:
        error_details = f"{errorMsg}:\n{str(e)}\nTraceback:\n{traceback.format_exc()}"
        logger.error(error_details)
        return []
    finally:
        if cursor:
            cursor.close()
