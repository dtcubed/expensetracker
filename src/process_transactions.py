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
import argparse
import csv 
import os

from sys import exit

#####
# ET modules.
#####
from et_rdbms import create_et_db_if_necessary
from et_transactions import insert_expense_transaction, insert_category_transaction
#############################################################################
def main():
    parser = argparse.ArgumentParser(description='Process ExpenseTracker Transactions.')
    parser.add_argument('--create_db', dest='create_db', default=0, type=int, choices=[0, 1])
    parser.add_argument('--debug', dest='debug', default=0, type=int, choices=[0, 1])
    parser.add_argument('--sqlite_db', dest='sqlite_db_file', required=True)
    parser.add_argument('--transactions', dest='transactions_file', required=True)
    args = parser.parse_args()

    #####
    # Before continuing, check for existence.
    #####
    if not os.path.exists(args.sqlite_db_file):
        #####
        # If the CLI flag is set, be willing to create the sqlite database. 
        #####
        if args.create_db:
            create_et_db_if_necessary(args.sqlite_db_file)
        else:
            print "\nSQLite DB: [", args.sqlite_db_file, "] does not exist. Exiting.\n" 
            exit()

    #####
    # Before continuing, check for existence.
    #####
    if not os.path.exists(args.transactions_file):
        print "\nTransactions File: [", args.transactions_file, "] does not exist. Exiting.\n" 
        exit()

    transactionReader = csv.reader(open(args.transactions_file, 'rb'))

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
                insert_category_transaction(args.sqlite_db_file, transaction)
            elif transaction[1] == 'E':
                print "INSERT->Expense"
                insert_expense_transaction(args.sqlite_db_file, transaction)
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
