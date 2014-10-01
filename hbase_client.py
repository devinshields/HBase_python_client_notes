#!/usr/bin/env python
'''  '''


import sys

import happybase



# test tablename and table schema
table_name = r'rock_gods'
families = {
    'genre': dict(max_versions=5),
    'hairstyle': dict(max_versions=9)
}

# connect to Thrift, then to HBase
c = happybase.Connection()

# query
tables = c.tables()
print '\navailable hbase tables:'
print '\t', tables
print '\n'

# lazy create the table - http://happybase.readthedocs.org/en/latest/api.html#happybase.Connection.create_table
if table_name not in tables:
  c.create_table(table_name, families)

# fetch a table reference
table = c.table(table_name)

# insert
table.put('the beatles', {'genre:': 'brit-pop',
                          'hairstyle:john': 'mop-top',
                          'hairstyle:paul': 'mop-top',
                          'hairstyle:george': 'mop-top',
                          'hairstyle:ringo': 'mop-top'})







# cleanup to prevent state changes
c.delete_table(table_name, disable=True)


# exit
sys.exit(0)




# update
table = connection.table('table-name')

table.put('row-key', {'family:qual1': 'value1',
                      'family:qual2': 'value2'})

row = table.row('row-key')
print row['family:qual1']  # prints 'value1'


print '\n'
for key, data in table.rows(['row-key-1', 'row-key-2']):
    print key, data  # prints row key and data for each row


print '\n'
for key, data in table.scan(row_prefix='row'):
    print key, data  # prints 'value1' and 'value2'

#
row = table.delete('row-key')

print '\nProcess Complete!'


