import json

j_file = "data/sample_table.json"

with open(j_file) as jf:
    data = json.load(jf)
    #print(json.dumps(data, indent=2))

tableName = data['tableName']
tableSchema = data['tableSchema']
columns = tableSchema['columns']

ordered_cols = sorted(columns, key=lambda d: d['order'])

create_stmt = "CREATE TABLE {} (". format(tableName)

for d in ordered_cols:
    create_stmt = create_stmt + "{} {},".format(d['name'], d['datatype'])

create_stmt = create_stmt[:-1] + ");"

print(create_stmt)