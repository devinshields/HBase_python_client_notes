#!/bin/bash
#
# http://hadoop.apache.org/docs/r1.2.1/single_node_setup.html#Prepare+to+Start+the+Hadoop+Cluster
# http://hbase.apache.org/book/quickstart.html
#
# On OSX, use brew to install hadoop, hbase, and thrift.
# note that this script isn't runnable, some sections are hbase cli script.
#


#
# --- HADOOP ---
#
hadoop namenode -format -force
start-all.sh

# loook at the monitoring web ui
open http://localhost:50070/
open http://localhost:50030/

# shutdown
stop-all.sh



#
# --- HBASE ---
#
start-hbase.sh
jps

# look at the web ui
open http://localhost:60010

# hbase CLI
hbase shell
help

# create a table
create 'test', 'cf'
list 'test'

# populate the table
put 'test', 'row1', 'cf:a', 'value1'
put 'test', 'row2', 'cf:b', 'value2'
put 'test', 'row3', 'cf:c', 'value3'

# inspect
scan 'test'

# edit, then delete
disable 'test'
enable 'test'
disable 'test'
drop 'test'

# quit hbase
exit
stop-hbase.sh



# --- THRIFT ---
# start a threadpool, preferably in a tmux session
hbase thrift start -threadpool


