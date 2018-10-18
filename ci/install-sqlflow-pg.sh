#!/bin/bash

# install SQLFlow PostgreSQL extension
EXT_PATH=myflow

mkdir -p myflow
cd mysqlow

echo "Download PG Extension for SQLFlow"
wget https://github.com/sql-flow/pg-extension/archive/master.tar.gz
tar -zxf master.tar.gz

ls -l

echo "Install SQLFlow on PostgreSQL"
psql -v "ON_ERROR_STOP=1" -f ./sql/sqlflow-structure.sql -U postgres myflow
psql -v "ON_ERROR_STOP=1" -f ./sql/sqlflow-instance.sql -U postgres myflow
