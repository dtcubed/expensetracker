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
from sys import exit

#####
# ET modules.
#####
from et_rdbms import insert_category, insert_expense
from et_validations import is_valid_amount, is_valid_YYYYMMDD
#############################################################################
def insert_category_transaction(db_name, transaction):

    code = transaction[2]
    parent_code = transaction[3]
    desc = transaction[4]

    insert_category(db_name, code, desc, parent_code)
#############################################################################
def insert_expense_transaction(db_name, transaction):

    incurred_date = transaction[2]
    amount = transaction[3]
    category_code = transaction[4]
    desc = transaction[5]

    insert_expense(db_name, incurred_date, amount, category_code, desc)
    
#############################################################################
if __name__ == "__main__":
    exit()
#############################################################################
