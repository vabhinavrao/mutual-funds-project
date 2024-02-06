import pandas as pd
import matplotlib.pyplot as pl
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from io import StringIO
mutual_fund = pd.read_csv("mutual_funds.csv")
name_column = mutual_fund.columns.tolist()

#DEFINITIONS
def names_of_mutual_funds():
    selected_data = mutual_fund.loc[:, ["name", "symbol"]]
    print(selected_data)


def view_data_multiple_fund():
    a = int(input("Enter the no of mutual funds you wish to view "))
    fund_names = []
    for i in range(a):
        fund_name = input("Enter the symbol of the mutual fund: ").upper()
        fund_names.append(fund_name)
    fund_data = mutual_fund.loc[mutual_fund['symbol'].isin(fund_names)]
    print(f"\n{fund_data}")


def single_paramenter_multiple_funds():
    a = input("Enter the name of the parameter you want to view of all the mutual funds ")
    print(mutual_fund.loc[:, str(a):str(a)])


def multiple_parameter_multiple_funds():
    n = int(input("Enter the number of columns: "))
    column_names = []
    for i in range(n):
        col_name = input(f"Enter the column name {i + 1} : ")
        column_names.append(col_name)
    I = []
    for i in column_names:
        if i in mutual_fund.columns:
            I.append(i)
        else:
            print(f"Column '{i}' not found in the DataFrame.")
    selected_mf = mutual_fund[I]
    print(selected_mf)


def multiple_parameter_single_fund():
    m = input("Enter the symbol of the mutual fund : ").upper()
    print((m))
    column_names_i = []
    n = int(input("Enter the number of columns: "))
    for i in range(n):
        m = input(f"Enter the column name {i + 1} : ")
        column_names_i.append(m)
    selected_dataframe = mutual_fund[column_names_i]
    print(selected_dataframe)


def all_parameter_single_fund():
    m = input("Enter the symbol of the mutual fund ").upper()
    print(mutual_fund.loc[m:m, :])



def compare_n_parameters():
    n = int(input("Enter the number of mutual funds you want to compare: "))
    fund_names = []

    for i in range(n):
        fund_name = input(f"Enter the symbol or name of mutual fund {i + 1}: ").upper()
        fund_names.append(fund_name)

    print(f"Selected Mutual Funds: {fund_names}")

    parameters_to_compare = ['return', 'risk', 'expense_ratio']
    for parameter in parameters_to_compare:
        for fund_name in fund_names:
            value = mutual_fund.loc[mutual_fund['symbol'] == fund_name, parameter].values
            print(f"{fund_name} - {parameter}: {value}")

def create_plots():
    parameters = ['return', 'risk', 'expense_ratio', '1 year returns%', '3 year returns%', '5 year returns%', 'alpha', 'aum(in ₹)']

    for parameter in parameters:
        pl.figure(figsize=(10, 6))
        pl.bar(mutual_fund['name'], mutual_fund[parameter])
        pl.xlabel('Mutual Fund Name')
        pl.ylabel(parameter)
        pl.title(f'{parameter} for Mutual Funds')
        pl.xticks(rotation=45, ha='right')
        pl.tight_layout()
        pl.show()

def kyc_financial_status():
    def calculate_points(age, savings, liability):
        points = 0
        points += (60 - age)
        points += int(savings / 10000)
        points -= int(liability / 500000)
        return points

    def evaluate_financial_health(points):
        if points >= 70:
            return "You have excellent financial health."
        elif 50 <= points < 70:
            return "You have good financial health."
        elif 30 <= points < 50:
            return "You have moderate financial health."
        elif 10 <= points < 30:
            return "You have poor financial health."

    age = int(input("Enter your age: "))
    savings = int(input("Enter your monthly savings for investment: "))
    liability = int(input("Enter your total liability: "))

    points = calculate_points(age, savings, liability)
    result = evaluate_financial_health(points)

    print(result)
    print(f"Points: {points}")

    age = int(input("Enter your age: "))
    savings = int(input("Enter your monthly savings for investment: "))
    liability = int(input("Enter your total liability: "))

    points = calculate_points(age, savings, liability) * 600
    result = evaluate_financial_health(points)

    print(result)
    print(f"Points: {points}")







def modify_excel_data_gui():
    def save_changes():
        try:
            # Get the modified data from the Text widget
            modified_data = text_widget.get("1.0", tk.END)

            # Load the modified data into a new DataFrame
            modified_df = pd.read_csv(StringIO(modified_data))

            # Save the modified DataFrame to the CSV file
            modified_df.to_csv("mutual_funds_modified.csv", index=False)

            messagebox.showinfo("Success", "Changes saved successfully!")
            root.destroy()  # Close the Tkinter window after saving changes
        except Exception as e:
            messagebox.showerror("Error", f"Error saving changes: {str(e)}")
    mutual_fund = pd.read_csv("mutual_funds.csv")
    root = tk.Tk()
    root.title("Mutual Fund Editor")
    text_widget = tk.Text(root, height=15, width=50)
    text_widget.insert(tk.END, mutual_fund.to_csv(index=False))
    text_widget.pack()
    save_button = ttk.Button(root, text="Save Changes", command=save_changes)
    save_button.pack()
    root.mainloop()

def main_menu():
    print('OM')
    print('Welcome to Mutual Funds Program')
    condition = 'yes'
    while condition == "yes":
        print('Before you proceed, please note the names of all the mutual funds: ')
        print('1 To view data of mutual funds'
              '\n2 To view different parameter of a mutual fund'
              '\n3 To compare between mutual funds'
              '\n4 To analyze mutual fund with the help of pictorial representation (e.g., graphs, charts)'
              '\n5 To get investment advice'
              '\n6 Modify Data')
        print()
        try:
            choice = int(input("Enter the number beside the task you want to perform: "))
            if choice == 1:
                print("You have selected the option to view the data of the mutual funds used in this program")
                print(names_of_mutual_funds())
                print(view_data_multiple_fund())
            elif choice == 2:
                print('You have selected the option to view the parameter of the fund')
                print('The different parameters of mutual fund are: ')
                print('Name: Name of mutual fund\n'
                      'Category: Category of mutual fund\n'
                      'Returns: Returns generated by mutual fund\n'
                      'Risk: Risk associated with the mutual fund\n'
                      'Expense_ratio: The expense ratio is the total annual cost of managing the mutual fund, expressed as a percentage of the fund average net assets.'
                      '1 year_returns: Specifies the returns generated by the mutual fund over the past one year\n'
                      '3 year_returns: Represents the returns over the past three years.\n'
                      '5year_returns: Indicates the returns over the past five years.\n'
                      'Alpha: Alpha is a measure of a mutual fund risk-adjusted performance compared to a benchmark index. \n'
                      'AUM(in ₹): AUM stands for Assets Under Management. It represents the total market value of all the financial assets managed by the mutual fund.')
                print()
                print('These parameters will be further used, so kindly copy and paste the exact text from here.')
                print("1 To view a parameter of all the mutual funds"
                      "\n2 To view parameter of a single mutual fund")
                choice_2 = int(input("Enter the number beside the task you want to perform: "))
                if choice_2 == 1:
                    print()
                    print(single_paramenter_multiple_funds())
                elif choice_2 == 2:
                    print()
                    print(multiple_parameter_single_fund())
            elif choice == 3:
                print()
                print('You have selected the option to compare mutual funds')
                compare_n_parameters()
                print()
            elif choice == 4:
                create_plots()
            elif choice == 5:
                print('You have selected the option to get investment advice')
                print('This will help you to understand your risk profile')
                print(kyc_financial_status())
                condition = input("Enter Yes to continue ").lower()
                print()
            elif choice == 6:
                print('You have selected the option to modify data')
                modify_excel_data_gui()
        except ValueError:
            print()
            print("Invalid input. Please enter a valid number.")
            print()

# Call the main menu function
main_menu()




def kyc_financial_status():
    def calculate_points(age, savings, liability):
        points = 0
        points += (60 - age)
        points += int(savings / 10000)
        points -= int(liability / 500000)
        return points

    def evaluate_financial_health(points):
        if points >= 70:
            return "You have excellent financial health."
        elif 50 <= points < 70:
            return "You have good financial health."
        elif 30 <= points < 50:
            return "You have moderate financial health."
        elif 10 <= points < 30:
            return "You have poor financial health."

    age = int(input("Enter your age: "))
    savings = int(input("Enter your monthly savings for investment: "))
    liability = int(input("Enter your total liability: "))

    points = calculate_points(age, savings, liability)
    result = evaluate_financial_health(points)

    print(result)
    print(f"Points: {points}")

    age = int(input("Enter your age: "))
    savings = int(input("Enter your monthly savings for investment: "))
    liability = int(input("Enter your total liability: "))

    points = calculate_points(age, savings, liability) * 600
    result = evaluate_financial_health(points)

    print(result)
    print(f"Points: {points}")



def create_plots():
    parameters = ['return', 'risk', 'expense_ratio', '1 year returns%', '3 year returns%', '5 year returns%', 'alpha', 'aum(in ₹)']

    for parameter in parameters:
        pl.figure(figsize=(10, 6))
        pl.bar(mutual_fund['name'], mutual_fund[parameter])
        pl.xlabel('Mutual Fund Name')
        pl.ylabel(parameter)
        pl.title(f'{parameter} for Mutual Funds')
        pl.xticks(rotation=45, ha='right')
        pl.tight_layout()
        pl.show()


def modify_excel_data_gui():
    def save_changes():
        try:
            # Get the modified data from the Text widget
            modified_data = text_widget.get("1.0", tk.END)

            # Load the modified data into a new DataFrame
            modified_df = pd.read_csv(StringIO(modified_data))

            # Save the modified DataFrame to the CSV file
            modified_df.to_csv("mutual_funds_modified.csv", index=False)

            messagebox.showinfo("Success", "Changes saved successfully!")
            root.destroy()  # Close the Tkinter window after saving changes
        except Exception as e:
            messagebox.showerror("Error", f"Error saving changes: {str(e)}")
    mutual_fund = pd.read_csv("mutual_funds.csv")
    root = tk.Tk()
    root.title("Mutual Fund Editor")
    text_widget = tk.Text(root, height=15, width=50)
    text_widget.insert(tk.END, mutual_fund.to_csv(index=False))
    text_widget.pack()
    save_button = ttk.Button(root, text="Save Changes", command=save_changes)
    save_button.pack()
    root.mainloop()
