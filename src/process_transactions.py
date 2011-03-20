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
#####
# Perl style regexp! Nice.
#####
import re

from sys import argv, exit
#############################################################################
def is_valid_insert_category_record(transaction_record):
    #####
    # First list element must be 'I' for INSERT.
    #####
    if transaction_record[0] != 'I':
        return False

    #####
    # Second list element must be 'C' for "catagory".
    #####
    if transaction_record[1] != 'C':
        return False

    return True
#############################################################################
def is_valid_insert_expense_record(transaction_record):
    #####
    # First list element must be 'I' for INSERT.
    #####
    if transaction_record[0] != 'I':
        return False

    #####
    # Second list element must be 'E' for "expense".
    #####
    if transaction_record[1] != 'E':
        return False

    #####
    # Third list element must be a valid date in the form of: YYYYMMDD 
    #####
    if not is_valid_yyyymmdd(transaction_record[2]):
        return False

    return True
#############################################################################
# TODO: Do in-depth checking here to ensure that this date is really a valid
#       date on the calendar, not just that the formatting conforms.
#############################################################################
def is_valid_yyyymmdd(a_string):
    #####
    # Use Perl style regexp here.
    #####
    regexp = re.compile('^2[0-9]{3}[0-1][0-2][0-3][0-9]$')

    if regexp.match(a_string):
        return True

    return False
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
    for transactionRecord in transactionReader:
        if is_valid_insert_expense_record(transactionRecord):
            print "TRUE, the transaction record is VALID"

#############################################################################
if __name__ == '__main__':
    main()

#############################################################################
#############################################################################
#############################################################################
