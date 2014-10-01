#!/usr/bin/env python
''' run `start-hbase.sh` to spin up HBase
    run `hbase thrift start -threadpool` to spin up Thrift
    example won't work without them
'''


import sys
import happybase


# test tablename, table schema, and row key
table_name = r'rock_gods'
families = {
    'genre': dict(max_versions=5),
    'hairstyle': dict(max_versions=9)
}
row_key = 'the beatles'


# connect to HBase via Thrift
c = happybase.Connection()

# query
tables = c.tables()
print '\navailable hbase tables:'
print '\t', tables
print '\n'

# lazy create the table - http://happybase.readthedocs.org/en/latest/api.html#happybase.Connection.create_table
if table_name not in tables:
  print '\ncreating test table'
  c.create_table(table_name, families)

# fetch a table reference
table = c.table(table_name)

# insert, sleep, insert
table.put(row_key, {'genre:': 'brit-pop',
                          'hairstyle:john': 'mop-top',
                          'hairstyle:paul': 'mop-top',
                          'hairstyle:george': 'mop-top',
                          'hairstyle:ringo': 'mop-top'})

import time;time.sleep(2)

table.put(row_key, {'hairstyle:john': 'beard-tastic',
                    'hairstyle:paul': 'scruffy',
                    'hairstyle:george': 'mustache',
                    'hairstyle:ringo': 'balding'})

# fetch a row
print '\nfetching a single row:'
print '\t', table.row(row_key)

# cleanup, no state changes in testing
#c.delete_table(table_name, disable=True)

