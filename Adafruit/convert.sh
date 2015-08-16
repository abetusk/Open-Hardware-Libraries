#!/bin/bash

eagle2kicad="../../Eagle2Kicad/eagle2kicad"
modjson="../../pykicad/modjson.py"
libjson="../../pykicad/libjson.py"

libsnap="../../www.meowcad.com/js/libsnap.js"
modsnap="../../www.meowcad.com/js/modsnap.js"

mkdir -p json.lib
mkdir -p json.mod
mkdir -p png/lib
mkdir -p png/mod
mkdir -p KiCAD

for x in `ls Eagle/*.lbr`
do
  f=`basename $x .lbr`

  echo $x $f

  $eagle2kicad -l $x KiCAD/$f.lib KiCAD/$f.mod

  mkdir -p json.lib/$f
  mkdir -p png/lib/$f
  $libjson KiCAD/$f.lib json.lib/$f/

  for y in `ls json.lib/$f/*.json`
  do
    echo $y
    yb=`basename $y .json`
    node $libsnap -I $y -W 200 -H 200 -o png/lib/$f/$yb.png
  done

  mkdir -p json.mod/$f
  mkdir -p png/mod/$f
  $modjson KiCAD/$f.mod json.mod/$f/

  for y in `ls json.mod/$f/*.json`
  do
    echo $y
    yb=`basename $y .json`
    node $modsnap -I $y -W 200 -H 200 -o png/mod/$f/$yb.png
  done

done
