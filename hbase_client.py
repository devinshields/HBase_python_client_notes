#!/usr/bin/env python
'''  '''


import sys

import happybase


#connection = happybase.Connection('localhost')
c = happybase.Connection()


# query
tables = c.tables()

print '\navailable hbase tables:'
print '\t', tables
print '\n'



# lazy create a testing table
table_name = r'rock_gods'


if table_name not in tables:
  # schema definition
  families = {
      'musical_style': dict(max_versions=5),
      'hairstyle:': dict(max_versions=9, block_cache_enabled=False)
  }
  c.create_table(table_name, families)



# query
print '\navailable hbase tables:'
print '\t', c.tables()
print '\n'



# cleanup
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


