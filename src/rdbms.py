#!/usr/bin/python
#############################################################################
#  The MIT License
#  
#  Copyright (c) 2011 dtcubed 
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#############################################################################
# TODO: Read the contents off of this link:
# http://www.doughellmann.com/PyMOTW/sqlite3/
# Determine how to shift this code around if necessary.
#####
import os.path

from sqlite3 import dbapi2 as sqlite
#############################################################################
def create_et_db_if_necessary(db_name):

    #####
    # Only create database if it doesn't already exist.
    #####
    if not os.path.isfile(db_name):
        print 'creating database:[', db_name, ']'
        connection = sqlite.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(create_table_sql('category'))
        cursor.execute(create_table_sql('expense'))
        cursor.execute(create_table_sql('info'))
        connection.commit()
        connection.close()
        insert_info(db_name, 'ExpenseTracker', '0', '1')
    else:    
        print 'database:[', db_name, '] exists'
#############################################################################
def create_table_sql(table_name):

    if table_name == 'category': 
        sql =  'CREATE TABLE category '
        sql += '(code TEXT NOT NULL, '
        sql += 'desc TEXT NOT NULL, '
        sql += 'parent_code TEXT NOT NULL)'
    elif table_name == 'expense': 
        sql =  'CREATE TABLE expense '
        sql += '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
        sql += 'amount REAL, '
        sql += 'category_code TEXT, '
        sql += 'desc TEXT NOT NULL)'
    elif table_name == 'info': 
        sql =  'CREATE TABLE info '
        sql += '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
        sql += 'name TEXT NOT NULL, '
        sql += 'major_version TEXT NOT NULL, '
        sql += 'minor_version TEXT NOT NULL)'
    else:
        sql = 'INVALID'

    return sql
#############################################################################
def insert_expense(db_name, amount, category_code, desc):

    if os.path.isfile(db_name):
        sql =  'INSERT INTO expense VALUES '
        sql += '(null, ?, ?, ?)'
        connection = sqlite.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(sql, (amount, category_code, desc))
        connection.commit()
        connection.close()
#############################################################################
def insert_info(db_name, name, major, minor):

    if os.path.isfile(db_name):
        connection = sqlite.connect(db_name)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO info VALUES (null, ?, ?, ?)', (name, major, minor))
        connection.commit()
        connection.close()
#############################################################################
def print_expense(db_name):

    if os.path.isfile(db_name):
        connection = sqlite.connect(db_name)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM expense')
        for row in cursor:
           print '-'*50
           print 'id:', row[0]
           print 'amount:', row[1]
           print 'category_code:', row[2]
           print 'desc:', row[3]
           print '-'*50   
        connection.close()
#############################################################################
def print_info(db_name):

    if os.path.isfile(db_name):
        connection = sqlite.connect(db_name)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM info')
        for row in cursor:
           print '-'*50
           print 'id:', row[0]
           print 'name:', row[1]
           print 'major_ver:', row[2]
           print 'minor_ver:', row[3]
           print '-'*50   
        connection.close()
#############################################################################
if __name__ == "__main__":
    #####
    # Create the database if necessary.
    #####
    create_et_db_if_necessary('expense.db')
    #print_info('expense.db')
    insert_expense('expense.db', 13.13, 'AUTO', 'Muffler Repair')
    insert_expense('expense.db', 14.14, 'FOOD', 'Cub Foods')
    insert_expense('expense.db', 15.15, 'CLOTHING', 'Target')
    print_expense('expense.db')
#############################################################################
