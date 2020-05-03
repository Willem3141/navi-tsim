#!/bin/sh

wget https://tirea.learnnavi.org/dictionarydata/NaviData_fwew.sql
echo "create database test;" | mysql
mysql test < NaviData_fwew.sql
rm NaviData_fwew.sql

echo "select * from metaWords;" | mysql --batch test > metaWords.tsv
echo "select * from localizedWords;" | mysql --batch test > localizedWords.tsv
echo "select * from sources;" | mysql --batch test > sources.tsv
#echo "drop database test;" | mysql --batch test > metaWords.tsv
