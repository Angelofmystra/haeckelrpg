#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('db.sqlite3')
    cur = con.cursor()    
    cur.execute('SELECT name FROM worldbuilder_Area')
    data = cur.fetchall()
    for d in data:
    	print d

except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    if con:
        con.close()

def area(cursor):
	cursor.execute('SELECT name FROM worldbuilder_Area')
