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
    else:    
        print 'database:[', db_name, '] exists'
#############################################################################
def create_table_sql(table_name):

    if table_name == 'category': 
        sql =  'CREATE TABLE category '
        sql += '(code STRING NOT NULL, '
        sql += 'desc STRING NOT NULL, '
        sql += 'parent_code STRING NOT NULL)'
    elif table_name == 'expense': 
        sql =  'CREATE TABLE expense '
        sql += '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
        sql += 'category_code STRING, '
        sql += 'desc STRING NOT NULL)'
    elif table_name == 'info': 
        sql =  'CREATE TABLE info '
        sql += '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
        sql += 'desc STRING NOT NULL, major_version STRING NOT NULL, '
        sql += 'minor_version STRING NOT NULL)'
    else:
        sql = 'INVALID'

    return sql
#############################################################################
def insert_into_names(db_name, name, email):

    if os.path.isfile(db_name):
        connection = sqlite.connect(db_name)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO names VALUES (null, ?, ?)', (name, email))
        connection.commit()
#############################################################################
def print_all_names(db_name):

    if os.path.isfile(db_name):
        connection = sqlite.connect(db_name)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM names')
        for row in cursor:
           print '-'*10
           print 'ID:', row[0]
           print 'Name:', row[1]
           print 'E-Mail:', row[2]
           print '-'*10   

#############################################################################
def routine_03():
    print 'routine_03'

if __name__ == "__main__":
    #####
    # Create the database if necessary.
    #####
    create_et_db_if_necessary('expense.db')
#    insert_into_names('expense.db', 'john', 'john@gmail')
#    insert_into_names('expense.db', 'frank', 'frank@gmail')
#    print_all_names('expense.db')
#############################################################################
