#!/bin/sh

wget https://eanaeltu.learnnavi.org/dicts/NaviData.sql
mysql test < NaviData.sql  # assuming a database named "test" exists
echo "select * from metaWords;" | mysql --batch test > metaWords.tsv
echo "select * from localizedWords;" | mysql --batch test > localizedWords.tsv
