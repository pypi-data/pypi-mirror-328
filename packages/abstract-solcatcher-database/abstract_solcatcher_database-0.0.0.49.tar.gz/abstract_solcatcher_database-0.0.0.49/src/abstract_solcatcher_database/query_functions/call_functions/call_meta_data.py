from .queries import get_db_from
from .call_pair_data import get_any_pair
def get_metadata_from(columnNames=None,searchColumn=None,searchValue=None,count=False):
    columnNames = columnNames or '*'
    return get_db_from(tableName='metadata',
                       columnNames=columnNames,
                       searchColumn=searchColumn,
                       searchValue=searchValue,
                       count=count)
def get_meta_data_from_mint(mint,columnNames=None):
    return get_metadata_from(searchColumn='mint', searchValue=mint,columnNames=columnNames)
def get_meta_data_from_meta_id(meta_id,columnNames=None):
    return get_metadata_from(searchColumn='id', searchValue=meta_id,columnNames=columnNames)
def get_meta_data_from_pair(pair_data,columnNames=None):
    pair = get_any_pair(pair_data)
    meta_id = pair.get('meta_id')
    if not meta_id:
        return []
    return get_meta_data_from_meta_id(meta_id,columnNames=columnNames)
#####################################
# Fix #4: get_meta_data uses correct references
#####################################
def get_meta_data(pair_id=None, meta_id=None, mint=None):
    if mint:
        return get_meta_data_from_mint(mint)
    if pair_id:
        return get_meta_data_from_pair(pair_id)
    if meta_id:
        return get_meta_data_from_meta_id(meta_id)
    return []
