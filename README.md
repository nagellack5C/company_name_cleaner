# company_name_cleaner

Given a company name, this simple function returns a name cleaned from various endings like Ltd., Corp. etc. You do not need any external libraries to use it.

This can be useful if you want to do an exact comparison of two company names but they are given in different forms, e.g. if fed with 'Apple Corporation' and 'Apple Corp.' this function will return 'Apple' for both names.

Endings can be customized in the endings.txt file.

Usage:

from name_cleaner import clean_name

name = clean_name("Apple Corp.")

print(name) //Apple
