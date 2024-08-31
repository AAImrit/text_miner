import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import csv
import re
import pandas as pd
from datetime import datetime

from create_expression import make_regex_expression

pd.set_option('display.max_columns', None) #to not hide any columns when printin

def get_user_input():
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
    content (pd DataFrame): content we want to filter through
    col_name (string): The column through which we are searching

    Returns:
    the newly created dataframe
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
    return new_df

def get_closure_info (common_issues_path, common_issue_list, user_search, re_expression):
    #get info for the issue to log the regex used, that way later we can use the same regex to pull 
    #also saves info in the common_issues list

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

        test_df = test_expression(expression, file_path, content, col_name)
        print("Here's a sample of the retrieved info. The full test file is located: " + file_path)
        print(test_df.head(20))
    
        user_validation = input("Is this what you were looking for? (0 - yes, 1 - no): ")
        
        if user_validation == "0":
            name = get_closure_info(common_issues_path, common_issues_list, user_search, expression)
            test_df.to_csv(file_path[:-8]+name+".csv", index=False)

if __name__ == '__main__':
    print ("Why")