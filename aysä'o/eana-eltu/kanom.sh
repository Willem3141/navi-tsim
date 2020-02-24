#!/bin/sh

wget https://tirea.learnnavi.org/dictionarydata/NaviData_fwew.sql
mysql test < NaviData_fwew.sql  # assuming a database named "test" exists
echo "select * from metaWords;" | mysql --batch test > metaWords.tsv
echo "select * from localizedWords;" | mysql --batch test > localizedWords.tsv
