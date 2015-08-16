#!/bin/bash

eagle2kicad="../../Eagle2Kicad/eagle2kicad"
modjson="../../pykicad/modjson.py"
libjson="../../pykicad/libjson.py"

libsnap="../../www.meowcad.com/js/libsnap.js"
modsnap="../../www.meowcad.com/js/modsnap.js"

$eagle2kicad -l tmp/sf-aes.lbr tmp/osh.lib tmp/osh.mod
$libjson tmp/osh.lib tmp/
#node $libsnap -I tmp/OSHW-LOGOL_OSHW-LOGO-L.json -W 400 -H 400 -o tmp/foo.png
node $libsnap -I tmp/SFE_LOGO_NAME_FLAME.9_INCH_SFE_LOGO_NAME_FLAME_.9.json -W 400 -H 400 -o tmp/foo.png

#head -n3 tmp/oshtmp.lib > tmp/oshonly.lib
#grep -A10679 '#Generated for OSHW-LOGOS package OSHW-LOGO-S' tmp/osh.lib >> tmp/oshonly.lib
##tail -n1 tmp/oshtmp.lib >> tmp/oshonly.lib

xloadimage tmp/foo.png

