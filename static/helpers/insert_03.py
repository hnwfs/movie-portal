#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, sys

movie = (
    (517987, 'Rafiki',' Barátnők', 'Rafiki'),
    (41261, '１リットルの涙', '1 liter könny', '1 litre of Tears'),
    (365283, '残穢-住んではいけない部屋-','A kitörölhetetlen','The Inerasable'),
    (515596,'ハニー','Édesem','Honey'),
    (300892,'ホットロード','Forró út','Hot road'),
    (695576,'A Soldier\'s Revenge','Katonaszív','A Soldier\'s Revenge'),
    (988667,'Thanh Sói: Cúc Dại Trong Đêm','Lángoló harag','Furies'),
    (849869,'길복순','Boksoon kettős élete','Kill Boksoon'),
    (768362,'Missing','Eltűnt','Missing'),
    (248784,'空へ ―救いの翼','Égre: Az üdvösség szárnyai','Rescue Wings')
)

try:
    con = sqlite3.connect('../sqlite/part-mozi-03.sqlite3')

    with con:
        cur = con.cursor()
        cur.executemany('INSERT INTO movie (tmdb,o_title, m_title, e_title) VALUES(?,?,?,?)', movie)

except sqlite3.Error as e:
    print('Error {}'.format(e.args[0]))

finally:
    if con:
        con.close()
