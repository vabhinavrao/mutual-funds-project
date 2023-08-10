import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

import pandas as pd

mutual_fund = pd.read_csv("mutual_funds.csv")
mutual_fund = mutual_fund.set_index("symbol")
def view_data_multiple_fund(data):
    a=int(input("Enter the no of mutual funds you wish to view "))
    for i in range(a):
        fund_name = input("Enter the name of the mutual fund: ")
        fund_data = data[data['name'] == fund_name]
        print(f"\n{fund_data}")
def view_data_single_fund(data):
    fund_name = input("Enter the name of the mutual fund: ")
    fund_data = data[data['name'] == fund_name]
    print(f"Data for mutual fund {fund_name}"
          f"\n{fund_data}")
def view_single_fund_parameters():
    a = input("Enter the starting column name : ")
    selected_data = mutual_fund.loc[:, str(a):str(a)]
    print(selected_data)
def view_multiple_fund_parameters():
    a = input("Enter the starting column name : ")
    b = input("Enter the ending column name : ")
    if a > b:
        a, b = b, a
    selected_data = mutual_fund.loc[:, str(a):str(b)]
    print(selected_data)
def names_of_mutual_funds():
    selected_data = mutual_fund.loc[:, "name":"name"]
    print(selected_data)

print("Welcome to the ultimate MUTUAL FUNDS Program ")
condition='Yes'
while condition=="Yes":
    print("1 To view the name of all the mutual fund used in the program "
          "\n2 To view the parameter of the fund "
          "\n3 To get investment advice ")
    print()
    choice=int(input("Enter the number beside the task you want to perform : "))
    if choice==1:
        print("to view the name of the funds used in this program ")
        print('1 To view data of a particular mutual fund '
              '\n2 To view data of multiple mutual fund '
              '\n3 To view single parameter of the data'
              "\n4 To view multiple parameters of the data "
              "\n5 To view only the names pf the mutual finds used in this program  ")
        print()
        choice_1 = int(input("Enter the number beside the task you want to perform : "))
        if choice_1==1:
            print("To view data of a particular mutual fund")
            print(view_data_single_fund(mutual_fund))
        elif choice_1==2:
            print("To view data of multiple mutual fund ")
            print(view_data_multiple_fund(mutual_fund))
        elif choice_1==3:
            print("To view single parameter of the data")
            print(view_single_fund_parameters())
        elif choice_1==4:
            print("To view multiple parameters of the data ")
            print(view_multiple_fund_parameters())
        elif choice_1==5:
            print("To view only the names of the mutual funds used in this program  ")
            print(names_of_mutual_funds())
    elif choice==2:
        print("To view the parameter of the fund")
        print(f"There are many parameter for the mutual fund they are :{mutual_fund.columns}")
        print(mutual_fund.columns.tolist())
    elif choice==3:
        print("To get investment advice")
    condition=input("Enter Yes to continue ").capitalize()
print()
print("program ended successfully")

