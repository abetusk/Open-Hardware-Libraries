#!/bin/bash

for x in `ls json.mod/*.json`
do
  f=`basename $x .json`
  echo making png/mod/$f.png
  node /home/abram/prog/github/abetusk/www.meowcad.com/js/modsnap.js -I $x -W 200 -H 200 -o png/mod/$f.png
done

for x in `ls json.lib/*.json`
do
  f=`basename $x .json`
  echo making png/lib/$f.png
  node /home/abram/prog/github/abetusk/www.meowcad.com/js/libsnap.js -I $x -W 200 -H 200 -o png/lib/$f.png
done
