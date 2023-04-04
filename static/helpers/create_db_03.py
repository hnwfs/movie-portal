#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, sys

con = None

try:
    con = sqlite3.connect('../sqlite/part-mozi-03.sqlite3')

    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS movie;')
    cur.execute('''
CREATE TABLE movie(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tmdb int NOT NULL,
    o_title text NOT NULL,
    m_title text NOT NULL,
    e_title text NOT NULL)
''')

except sqlite3.Error as e:
    print('Error {}'.format(e.args[0]))

finally:
    if con:
        con.close()