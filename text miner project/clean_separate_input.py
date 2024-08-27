import re

OR_OP = '|'
AND_OP = '&'

def basicClean (sentence):
    '''
    cleans up the sentence to make sure every thing is ok

    Args:
    sentence (string): sentence we want to clean

    Returns:
    cleanSen (string): sentence that has been cleaned
    '''
    #remove unexpected characters at the begining and end of the user input
    reExpression = '^[\)' + AND_OP + OR_OP + ']|[' + AND_OP + OR_OP + '\(]+$'
    cleanSen = re.sub(reExpression, "", sentence)

    #find all unclosed brackets and close them
    return cleanSen

def find_closing_posi (opPosi, sentence, special=False):
    '''
    Given the opening position of a bracket, find the corresponding closing bracket position

    Args:
    opPosi: index of the opening bracker
    sentence (string): sentence we want to clean

    Returns:
     - (int): the index of the closing bracket
    '''
    substring = sentence[opPosi:]

    expression = '\)'
    if special:
        expression = '[&)]'
    closeMatch = re.search(expression, substring)

    if closeMatch:
        return (closeMatch.start()+opPosi)

    return len(sentence)-1

def find_opening_posi (closePosi, sentence, special=False):
    '''
    Given the closing position of a bracket, find the corresponding opening bracket position

    Args:
    closePosi: index of the closing bracker
    sentence (string): sentence we want to clean

    Returns:
     - (int): the index of the opening bracket
    '''
    substring = sentence[:closePosi]
    if special: #this is for finding potential opening braket of a sentence missing a closing braket
        substring += ")"

    expression = '\([^()]*\)$'
    opMatch = re.search(expression, substring)

    if opMatch:
        return opMatch.start(), True
    
    return 0, False

def replace_and (sentence):

    posi = sentence.find(AND_OP)
    if posi == -1: #there are no & in the search resequest
        return sentence

    miniLeft = ""
    miniRigth=""
    special=False

    if sentence[posi-1] != ")": #missing closing bracket
        #this is not for full proofing, it only work in cases when there is one word for exampple (test&right)
        special=True
        specialOpPosi = find_opening_posi(posi, sentence, special)
        if specialOpPosi[1]: #an opening was actually matching
            opPosi = specialOpPosi[0]
            sentence = sentence[:opPosi] + "(" + sentence[opPosi:posi] + ")" + sentence[posi:]
            posi=sentence.find(AND_OP) #recalculating the position of the posi


    opPosi = find_opening_posi(posi, sentence)[0]
    miniLeft = sentence[:opPosi] + "(?=.*" + sentence[opPosi:posi] + ")"
    
    special=False
    if sentence[posi+1] != "(":
        special = True

    closePosi = find_closing_posi(posi+1, sentence)
    miniRigth = "(?=.*" + sentence[posi+1:closePosi+1] + ")" + sentence[closePosi+1:]
    
    sentence = miniLeft+miniRigth
    print(sentence)

    return replace_and(sentence)

    #sentence=replace_and(sentence)
    #print("pass " + sentence)

if __name__ == '__main__':
    #sentence = "(pin&(lift|lead))|(test&right)"
    sentence = "(lift|lead)&pin"
    #sentence = "(test&right)"
    #sentence = "((pin)&(lift|lead))|((test)&(new))" #((?=*(pin))(?=*(lift|lead)))|((?=*(test))(?=*(new))) -> right expresion
    #sentence="(test|new)&(free|you)"
    #sentence="(test&new)"
    #sentence = "pin&(lift|new)"
    test=replace_and(sentence)
    print("\nFinal Version:")
    print(test)