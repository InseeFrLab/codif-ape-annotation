import pyarrow.parquet as pq

def split_parquet(parquet_file, num_splits):
    # Read the Parquet file
    table = pq.read_table(parquet_file)
    
    # Calculate the number of rows in each split
    num_rows = len(table)
    rows_per_split = num_rows // num_splits
    
    # Split the table into multiple tables
    tables = []
    start_idx = 0
    for i in range(num_splits):
        end_idx = start_idx + rows_per_split
        if i == num_splits - 1:
            # Last split may have remaining rows
            end_idx = num_rows
        split_table = table.slice(start_idx, end_idx)
        tables.append(split_table)
        start_idx = end_idx
    
    return tables

# Example usage
parquet_file_path = "test_data_NAF2008.parquet"
num_splits = 3
split_tables = split_parquet(parquet_file_path, num_splits)

# Writing split tables to separate Parquet files
for i, table in enumerate(split_tables):
    pq.write_table(table, f"split_{i+1}.parquet")
