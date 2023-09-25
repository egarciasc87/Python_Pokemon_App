import pandas as pd
import numpy as np 
import pyodbc
import math

conn_string = ("Driver={SQL Server Native Client 11.0};"
            "Server=eric-pc\sqlexpress;"
            "Database=pokemonreview;"
            "Trusted_Connection=yes;")
            #"Integrated Security=SSPI;")
            #"UID=Alex;"
            #"PWD=Alex123;")

dict_tables = {"1": "countries", 
               "2": "categories",
               "3": "owners",
               "4": "pokemon"}

#SayHello()

def ReadCountry():
    #table_name = dict_tables.get(entity)
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    query = "select * from countries"
    data = pd.read_sql(query, conn)
    print(data)


def UpdateCountry():
    print("\n-> UPDATE COUNTRY")
    id = input("Enter ID of country to update: ")
    name = input("Enter new NAME: ")

    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    query = "EXEC UPDATE_COUNTRY_SP " + id + ", '" + name + "'"
    cursor.execute(query)
    cursor.commit()
    print("Item updated successfully!")   


def DeleteCountry():
    print("\n-> DELETE A COUNTRY")
    id = input("Enter ID of the country: ")

    query = "EXEC DELETE_COUNTRY_SP " + id
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.commit()
    print("Item deleted successfully!")   


def InsertCountry():
    print("\n-> INSERT NEW COUNTRY")
    name = input("Enter new NAME: ")

    query = "EXEC INSERT_COUNTRY_SP '" + name + "'"
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.commit() 
    print("Item inserted successfully!")   


option = ""
suboption = ""

while (option != "S"):
    print("\n----------MAIN MENU----------")
    print("Select entity you want to operate on: ")
    print("[1] Country")
    print("[2] Category")
    print("[3] Owner")
    print("[4] Pokemon")
    print("[S] Exit app")
    option = input("Enter input: ")
    option = option.upper()

    if option == "S":
        break

    while (suboption != "S"):
        print("\nSelect operation: ")
        print("[R] Read")
        print("[U] Update")
        print("[I] Insert")
        print("[D] Delete")
        print("[S] Back to main menu")
        suboption = input("Enter option: ")
        suboption = suboption.upper()

        if suboption == "S":
            break
        elif suboption == "R":
            ReadCountry()
        elif suboption == "U":
            UpdateCountry()
        elif suboption == "I":
            InsertCountry()
        elif suboption == "D":
            DeleteCountry()
        else:
            print("Operation not valid!")

