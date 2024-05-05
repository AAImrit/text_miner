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

def find_closing_posi (opPosi, sentence):
    '''
    Given the opening position of a bracket, find the corresponding closing bracket position

    Args:
    opPosi: index of the opening bracker
    sentence (string): sentence we want to clean

    Returns:
     - (int): the index of the closing bracket
    '''
    substring = sentence[opPosi:]

    closeMatch = re.search(r'\)', substring)

    if closeMatch:
        return (closeMatch.start()+opPosi)

    return len(sentence)-1

def find_opening_posi (closePosi, sentence):
    '''
    Given the closing position of a bracket, find the corresponding opening bracket position

    Args:
    closePosi: index of the closing bracker
    sentence (string): sentence we want to clean

    Returns:
     - (int): the index of the opening bracket
    '''
    substring = sentence[:closePosi]
    print(substring)

    opMatch = re.search(r'\([^()]*\)$', substring)
    print(opMatch)
    if opMatch:
        return opMatch.start()
    
    return 0

def find_closest (posi, sentence, isRight=False):
    substring = sentence[:posi]
    if isRight:
        substring = sentence[posi:]


def replace_and (sentence):
    posi = sentence.find(AND_OP)
    miniLeft = ""
    miniRigth=""

    if posi == -1:
        return sentence
    
    if sentence[posi-1] == ")":
        opPosi = find_opening_posi(posi, sentence)
        print(opPosi)

    miniLeft = sentence[:opPosi] + "(?=*" + sentence[opPosi:posi] + ")"
    
    if sentence[posi+1] == "(":
        closePosi = find_closing_posi(posi+1, sentence)
    
    miniRigth = "(?=*" + sentence[posi+1:closePosi+1] + ")" + sentence[closePosi+1:]
    
    sentence = miniLeft+miniRigth
    print(sentence)
    return sentence
    #replace_and(sentence)

        #check right

if __name__ == '__main__':
    #sentence = "((pin)&((lift|lead)|((test)&(right))))&(test)"
    sentence="(test|new)&(free|you)"
    sentence=replace_and(sentence)
    sentence=replace_and(sentence)
    sentence=replace_and(sentence)