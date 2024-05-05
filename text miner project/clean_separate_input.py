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
    #substring = sentence[:closePosi]
    substring = sentence[:closePosi]
    print(substring)
    expression = '\([^()]*\)$'
    if special:
        expression = '.{0,%d}[&)]' % closePosi
        
    opMatch = re.search(expression, substring)

    #opMatch = re.search(r'\([^()]*\)$', substring)
    if opMatch:
        return opMatch.start()
    
    return 0

def find_closest_terminatorR (posi, sentence):
    substring = sentence[posi:]

def replace_and (sentence):
    posi = sentence.find(AND_OP)
    miniLeft = ""
    miniRigth=""
    special=False

    if posi == -1:
        return sentence
    
    if sentence[posi-1] != ")":
        special = True

    opPosi = find_opening_posi(posi, sentence, special)
    miniLeft = sentence[:opPosi] + "(?=*" + sentence[opPosi:posi] + ")"
    
    special=False
    if sentence[posi+1] != "(":
        special = True

    closePosi = find_closing_posi(posi+1, sentence)
    miniRigth = "(?=*" + sentence[posi+1:closePosi+1] + ")" + sentence[closePosi+1:]
    
    sentence = miniLeft+miniRigth
    print(sentence)
    return sentence
    #replace_and(sentence)

        #check right

if __name__ == '__main__':
    #sentence = "((pin)&((lift|lead)|((test)&(right))))&(test)"
    #sentence = "(pin&(lift|lead)|(test&right))&test"
    #sentence="(test|new)&(free|you)"
    sentence="(test&new)"
    sentence=replace_and(sentence)
    sentence=replace_and(sentence)
    sentence=replace_and(sentence)