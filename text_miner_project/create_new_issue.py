import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import csv
import re
import pandas as pd
from datetime import datetime

from create_expression import make_regex_expression

def get_user_input():
    #!!!!Should also get the name of the column we are searching
    '''
    gets user expression, what they are looking for, turns in into regex 
    expression and ask user to validate that expression is good

    Args:
    none

    Return:
    expression (string): regex expression of user input
    '''
    user_validation = "1"
    expression = "1"
    search = "1"

    while user_validation != "0":
        search = input("Enter expression to search or enter 0 to quit:\n")

        if search == "0":
            break
        
        expression = make_regex_expression(search)
        user_validation = input("Is " + expression + " the correction expression. Enter 0 for yes, 1 for no:\n")
    
    return expression, search

def test_expression(regex_expression, file_path, content, col_name):
    '''
    uses expression to get the filter for words we want in the decription field of the data

    Args:
    regex_expression (string): regex expression for the search we want to perform
    file_path (string): path for where to save file created
    content (pd DataFrame): content we want to filter through -> currently pd dataframe, will be 
    changed to a something else once figure out how to read from l2l api call
    col_name (string): The column through which we are searching

    Returns:
    none
    '''

    new_df = pd.DataFrame(columns = list(content.columns))
    content = content.reset_index()
    
    
    for index, row in content.iterrows():
        description = row[col_name]

        if(isinstance(description, str) and re.search(regex_expression, description, re.IGNORECASE)):
            #new_df = pd.concat([row, new_df], axis=1)
            new_df = new_df.append(row)
    
    new_df = new_df.reset_index()
    #print(new_df)
    new_df.to_csv(file_path, index=False)

def get_closure_info (common_issues_path, common_issue_list, user_search, re_expression):
    #get info for the issue to log the regex used, that way later we can use the same regex to pull again
    name_issue = input("Enter Name of issue:\n")

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    new_issue = {'name': name_issue, 'looking':user_search, 'regex':re_expression, 'date created': dt_string}
    common_issue_list = common_issue_list.append(new_issue, ignore_index=True)

    common_issue_list.to_csv(common_issues_path, index=False)
    return name_issue

def create_new_issue_main (content, file_path, common_issues_path, col_name="Description"):
    user_validation = "1"
    common_issues_list = pd.read_csv(common_issues_path)
    
    while user_validation != "0":
        expression, user_search = get_user_input()
        if user_search == "0":
            break

        test_expression(expression, file_path, content, col_name)

        print ("The test file is located: " + file_path)
        user_validation = input("Is this what you were looking for? (0 - yes, 1 - no): ")
        
        if user_validation == "0":
            name = get_closure_info(common_issues_path, common_issues_list, user_search, expression)
            test_expression(expression, file_path[:-8]+name+".csv", content, col_name)

    #Need to ask person to validate the file created or if they want to change what
    #they searched for
    #once validated, save in common_issue file
    
if __name__ == '__main__':
    print ("Why")