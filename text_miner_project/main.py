import csv
import os, re
import pandas as pd

from create_new_issue import *

def get_data_path (file_name):
    '''
    get path of where the repo was cloned ant then concatenate with whatever we want
    assuming that this file is one 1 folder below the main (main/folder/file.py)

    Args:
    file_name (string): path where file should be relative to the repo location

    returns:
    (string): absolute path of where file_name should be
    '''
    cwd = os.path.dirname(__file__)
    main_dir = os.path.split(cwd)[0]
    
    return os.path.join(main_dir, file_name)

def get_common_issues(file_path):
    rows = []
    with open(common_issues_path, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)

    return rows

def main_options():
    options = ["Quit", "Create New Issue", "Pull Common Issue", "Edit Common Issue"]

    print ("\n")
    for i in range (0, len(options), 1):
        print (str(i+1) + " - " + options[i])
    
    user_choice = input("Enter number from options above: ")

    return user_choice

def get_data(file_name, path=False):
    file_path = file_name
    if path == False:
        file_path = get_data_path(file_name)
    df = pd.read_csv(file_path)
    return df

def create_new_issue(common_issue_path, file_name="dataset\\all_data.csv"):
    user_confirmation = 0
    path=False

    while (user_confirmation != '1'):
        user_confirmation = input("Is the data in: '" + file_name + "' (1-Yes, 0-No): \n")

        if user_confirmation == '0':
            file_name = input("Enter the file path: \n")

            path=True
            user_confirmation = '1'

    save_path = get_data_path("new_dataset\\test.csv")
    
    data = get_data(file_name, path)
    col_name = "Description"

    if path == True:
        col_name_exist=False
        while col_name_exist == False:
            col_name = input("Enter the name of the column to search through: \n")

            if col_name not in data.columns:
                print(col_name + " is not in the data. The following are the columns in the dataset:")
                print(data.columns)
            else:
                col_name_exist = True

    create_new_issue_main(data, save_path, common_issue_path, col_name)

def pull_common_issue(common_issue_path):
    print ("Secret Stuff")

def edit_common_issue():
    print ("working on it")

if __name__ == "__main__":
    common_issues_path = get_data_path("dataset\\common_issues.csv")
    issue_list = pd.read_csv(common_issues_path)
    
    user_choice = "0"

    while (user_choice != "1"):
        user_choice = main_options()

        if (user_choice == "2"):
            create_new_issue(common_issues_path)

        elif (user_choice == "3"):
            pull_common_issue(common_issues_path)

        elif (user_choice == '4'):
            edit_common_issue()
        
        elif (user_choice != "1"):
            print ("\nINVALID INPUT TRY AGAIN\n")
        