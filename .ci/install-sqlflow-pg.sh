#!/bin/bash

# install SQLFlow PostgreSQL extension
EXT_PATH=myflow

mkdir -p myflow
cd myflow

echo "Download PG Extension for SQLFlow"
wget https://github.com/sql-flow/pg-extension/archive/master.tar.gz
tar -zxf master.tar.gz

ls -l

echo "Create user and database"
psql -c "CREATE USER myflow WITH PASSWORD 'myflow';" -U postgres
psql -c 'CREATE DATABASE myflow WITH OWNER myflow;' -U postgres

echo "Install SQLFlow on PostgreSQL"
cd pg-extension-master
psql -v "ON_ERROR_STOP=1" -f ./sql/sqlflow-structure.sql -U postgres myflow
psql -v "ON_ERROR_STOP=1" -f ./sql/sqlflow-instance.sql -U postgres myflow
