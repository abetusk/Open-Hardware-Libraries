#!/usr/bin/python
#A -200 -200 70 -1120 -1800 0 0 15 N -226 -264 -270 -200
#A -200 -200 70 1800 680 0 0 15 N -270 -200 -174 -264

import sys


r = 70
x = 200
y = 200

dr = 20
da = 400

p = [ -270, -200, -174, -264 ]
sa = 1800

### neg ea results in smaller arc
### 0 ea results in circle
p = [ -270, -200, -174, -264 ]
sa = 1800
for k in range(6):
  ea = [680,-680,0,90,-90,45][k]
  x0 = (p[0]-x) * (k+1)
  y0 = (p[1]-y) * (k+1)
  x1 = (p[2]-x) * (k+1)
  y1 = (p[3]-y) * (k+1)
  print "A", x , y, r, sa, ea, 0, 0, 15, "N", x0, y0, x1, y1
  r += dr
sys.exit(0)


### neg ea results in smaller arc
### 0 ea results in circle
p = [ -226, -264, -270, -200 ]
sa = 1800
for k in range(6):
  ea = [680,-680,0,90,-90,45][k]
  x0 = p[0] * (k+1)
  y0 = p[1] * (k+1)
  x1 = p[2] * (k+1)
  y1 = p[3] * (k+1)
  print "A", x , y, r, sa, ea, 0, 0, 15, "N", x0, y0, x1, y1
  r += dr
sys.exit(0)

### neg ea results in smaller arc
### 0 ea results in circle
p = [ -270, -200, -174, -264 ]
sa = -1800
for k in range(6):
  ea = [680,-680,0,90,-90,45][k]
  x0 = p[0] * (k+1)
  y0 = p[1] * (k+1)
  x1 = p[2] * (k+1)
  y1 = p[3] * (k+1)
  print "A", x , y, r, sa, ea, 0, 0, 15, "N", x0, y0, x1, y1
  r += dr
sys.exit(0)


for ea in range(0,3600,da):
  print "A", x , y, r, sa, ea, 0, 0, 15, "N"
  r += dr

sa = -1800
for ea in range(0,3600,da):
  print "A", x , y, r, sa, ea, 0, 0, 15, "N"
  r += dr

sys.exit(0)


sa = 900
ea = sa+da
for k in range(10):
  print "A", x , y, r, sa, ea, 0, 0, 15, "N"
  r += dr
  ea += da

sa = 1800
ea = 0
for k in range(10):
  print "A", x , y, r, sa, ea, 0, 0, 15, "N"
  r += dr
  ea += da

sys.exit(0)


for sa in range(0, 2100, 200):
  print "A", x , y, r, sa, sa+da, 0, 0, 15, "N"
  r += dr

da = 400

for sa in range(0, -2200, -300):
  print "A", x , y, r, sa, sa-da, 0, 0, 15, "N"
  r += dr


for ea in range(da, 3600, da):
  print "A", x , y, r, 0, ea, 0, 0, 15, "N"
  r += dr

for ea in range(-da, -3600, -da):
  print "A", x , y, r, 0, ea, 0, 0, 15, "N"
  r += dr


sa = 900
ea = sa+da
for k in range(20):
  print "A", x , y, r, sa, ea, 0, 0, 15, "N"
  r += dr
  ea += da
  if ea >= 3600: ea -= 3600
  if ea <= -3600: ea += 3600

sa = -900
ea = sa-da
for k in range(20):
  print "A", x , y, r, sa, ea, 0, 0, 15, "N"
  r += dr
  ea -= da
  if ea >= 3600: ea -= 3600
  if ea <= -3600: ea += 3600



