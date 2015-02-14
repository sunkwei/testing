# coding: utf-8

import sqlite3 as sql
import time

FNAME = ':memory:'

s0 = 'create table t1 (name varchar(64), stamp integer, info text)'
s1 = 'insert into t1 values("abcd", 1234, "test recording ....")'

conn = sql.connect(FNAME)
c = conn.cursor()
c.execute(s0)

t1 = time.time()
for i in range(0, 100000):
	c.execute(s1)
	conn.commit()
t2 = time.time()

print 'using %f seconds' % (t2 - t1)
conn.close

