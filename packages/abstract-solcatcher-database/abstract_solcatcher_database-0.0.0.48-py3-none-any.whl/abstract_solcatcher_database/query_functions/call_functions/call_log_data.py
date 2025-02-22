from .queries import get_db_from
def get_logdata_from(columnNames=None,searchColumn=None,searchValue=None,count=False):
    columnNames = columnNames or '*'
    return get_db_from(tableName='logdata',
                       columnNames=columnNames,
                       searchColumn=searchColumn,
                       searchValue=searchValue,
                       count=count)
def get_logdata_from_log_id(log_id):
    return get_logdata_from(searchColumn='id',searchValue=log_id)
def get_signature_from_log_id(log_id):
    return get_logdata_from(columnNames='signature',searchColumn='id',searchValue=log_id)
def get_logdata_from_signature(signature):
    return get_logdata_from(columnNames='*',searchColumn='signature',searchValue=signature)

                    
