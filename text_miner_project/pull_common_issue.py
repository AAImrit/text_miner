#!!!!!!!!!!!!!!!!!!!!!!!!THIS FILE NEEDS TO FIXED!!!!!!!!!!!!!

import pandas as pd
import numpy as np
import re
from openpyxl import load_workbook


def find_dispatch (regex_expression, info = "1"):
    dispatches = get_most_recent() #should read file instead
    info = pd.DataFrame(columns = list(dispatches.columns)) #creating new dt, later will check if need to create new one or not
    #print(dispatches.columns)

    for index, row in dispatches.iterrows():
        description = row['Description']
        if(isinstance(description, str) and re.search(regex_expression, description, re.IGNORECASE)):
            info = info.append(row)
    
    info.reset_index
    return info

def choose_issue (common_issue_path):
    issue_list = (pd.read_csv(common_issue_path)).to_dict('index')

    print ("\nChoose dispatches to close under master dispatched")
    print("0 - Quit")
    for i in range(0, len(issue_list), 1):
        print(str(i+1) + " - " + issue_list[i]['name'] + " - " + issue_list[i]['looking'])
    
    user_input = input("Choose Issue: ") #will need to validate this later
    if user_input == "0":
        return 0

    issue_chosen = int(user_input) -1

    issue_dispatches = find_dispatch(issue_list[issue_chosen]['regex'])