# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 13:58:27 2020

@author: ARAVIND PC
"""

import sqlite3 
 
conn = sqlite3.connect('ABC_complaints.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE complaints
             (name text, invref text, invdate date, pname text, nature text, 
             cref integer primary key autoincrement, status text)''')

# INSERT INTO complaints (name, invref, invdate, pname, nature, status ) 
# VALUES ('Rahul','RF236','2019-05-07', 'Samsung Mobile', 'Battery is not charging', 'Service personal will meet you')

#UPDATE complaints SET status = '' WHERE cref=''

#select * from complaints


