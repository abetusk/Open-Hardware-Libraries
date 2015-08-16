#!/bin/bash

../../../../pykicad/modjson.py osh.mod
node ../../../../www.meowcad.com/js/modsnap -I OSHWLOGO_TOL_0.2.json -o foo.png
xloadimage foo.png
#node ../../../../www.meowcad.com/js/modsnap -I OSHWLOGO_TOP_0.2.json -o foo.png
#xloadimage foo.png
