import csv

def read_file(file_name):
    rows = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(row)
    return rows

def create_sql_insert_statement(file_name):
    table_name = file_name.split(".")[0]
    rows = read_file(file_name)
    headers = ",".join(rows[0])
    insert_line = "INSERT INTO " + table_name + "(" + headers + ")\n"
    values_line = "VALUES\n"
    entries = []
    
    for row in rows[1:]:
        value = "\t(" + ",".join(row) + ")"
        entries.append(value)
    
    entry_lines = ",\n".join(entries)
    
    return insert_line + values_line + entry_lines + ";"
    
print(create_sql_insert_statement("usernames.csv"))

