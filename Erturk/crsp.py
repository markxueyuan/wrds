from __future__ import print_function
import wrds
import csv
import pandas as pd


"""
    WRDS data is structured according to vendor (e.g. CRSP) and
    referred to as a library.
    Each library contains a number of component databases (e.g. DSF).
    Together, they are called a product (e.g. CRSP.DSF)
"""
result = wrds.sql('select distinct libname from dictionary.tables')

f = open("data/libraries" , "w")

print(result.to_string(), file=f)

f.close()


"""
    CRSP products lists
"""


CRSP = wrds.sql('select distinct memname from dictionary.columns \
                where libname="CRSP"')

f2 = open("data/CRSP" , "w")

print(CRSP.to_string(), file=f2)

f2.close()


"""
    CRSP stocknames db headers
"""


stocknames = wrds.sql('select name from dictionary.columns \
                   where libname="CRSP" \
                   and memname="STOCKNAMES"')

f3 = open("data/stocknames_header" , "w")

print(stocknames.to_string(), file=f3)

f3.close()


"""
    CRSP stocknames db headers
"""


stocknames = wrds.sql('select * from CRSP.STOCKNAMES')

stocknames.to_csv("data/stocknames")


