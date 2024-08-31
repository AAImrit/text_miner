# text_miner
This was originally made for scenarios where you have to search through a large dataset where each entry had a decription written by people. And where you would use the search query to do other things that can be linked to other python code.

The code allows you to write a simple search expression like "(cat&mouse)|crow", and it will use this search query to turn it into a regex expression to searh through the dataset to find all entries that adhere to the search query (in this example it will be any entry that only contains the word cat & mouse or only contains crow). 

The code basically simplifies seaching through these description ad allows you to easily create and retain new if statement without much effort and without needing to go into the code everytime to change a simple if statement.

It mainly only works for simple & or | queries. Anything too complex and it will probably result in an error.