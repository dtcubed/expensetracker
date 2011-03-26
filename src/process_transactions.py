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
import csv 
import os
from sys import argv, exit

#####
# ET modules.
#####
from rdbms import insert_expense_transaction, insert_category_transaction
#############################################################################
def main():
    sqlite_db = argv[1]
    #####
    # Before continuing, check for existence.
    #####
    if not os.path.exists(sqlite_db):
        print "\nSQLite DB: [", sqlite_db, "] does not exist. Exiting.\n" 
        exit()

    transactions_file = argv[2]
    #####
    # Before continuing, check for existence.
    #####
    if not os.path.exists(transactions_file):
        print "\nTransactions File: [", transactions_file, "] does not exist. Exiting.\n" 
        exit()

    transactionReader = csv.reader(open(transactions_file, 'rb'))

    #####
    # Each row is really a list of strings as parsed by the csv reader.
    #####
    for transaction in transactionReader:
        #####
        # INSERT record.
        #####
        if transaction[0] == 'I':
            if transaction[1] == 'C':
                print "INSERT->Category"
                insert_category_transaction(sqlite_db, transaction)
            elif transaction[1] == 'E':
                print "INSERT->Expense"
                insert_expense_transaction(sqlite_db, transaction)
        #####
        # UPDATE record.
        #####
        elif transaction[0] == 'U':
            print "UPDATE"
        #####
        # DELETE record.
        #####
        elif transaction[0] == 'D':
            print "DELETE"

#############################################################################
if __name__ == '__main__':
    main()
#############################################################################
#############################################################################
#############################################################################
