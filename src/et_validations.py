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
#####
# Perl style regexp capability.
#####
import re
import time
#############################################################################
def is_valid_YYYYMMDD(proposed_datestamp):
    #####
    # First, we are going to constrain the possible values that we are 
    # willing to accept using a Perl style regexp. For the following regexp,
    # a datestamp fitting into the following range will "match":
    #   20000000 through 29991239. 
    # Of couse, since we all know there are invalid dates in that range, 
    # further processing is necessary.
    #####
    regexp = re.compile('^2[0-9]{3}[0-1][0-2][0-3][0-9]$')

    if regexp.match(proposed_datestamp):
        #####
        # A Google search on "python date validation" reflects several 
        # examples of using this technique to ensure that the proposed 
        # datestamp reflects a proper calendar date.
        #####
        try:
            time.strptime(proposed_datestamp, '%Y%m%d')
        except ValueError:
            #####
            # The ValueError exception should be thrown for invalid months
            # and days within a month. For example, 20110229, since there
            # is no 29th of February for 2011.
            #####
            return False
        else:
            return True

    return False
#############################################################################
def main():
    print "Hello world"

#############################################################################
if __name__ == '__main__':
    main()
#############################################################################
#############################################################################
#############################################################################
