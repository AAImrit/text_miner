import re

OR_OP = '|'
AND_OP = '&'

def basicClean (sentence):
    #find all unclosed brackets and close them
    reExpression = '^[\)' + AND_OP + OR_OP + ']|[' + AND_OP + OR_OP + '\(]+$'
    cleanSen = re.sub(reExpression, "", sentence)
    #find all unclosed brackets and close them

def find_closing_posi (opPosi, sentence):
    substring = sentence[opPosi:]

    closeMatch = re.search(r'\)', substring)
    return (closeMatch.start()+opPosi)

def find_opening_posi (closePosi, sentence):
    substring = sentence[:closePosi]
    print(substring)

    opMatch = re.search(r'\([^()]*\)$', substring)
    print(opMatch)
    if opMatch:
        return opMatch.start()
    
    return -1

def replace_and (sentence):
    posi = sentence.find(AND_OP)
    miniLeft = ""
    miniRigth=""

    if posi == -1:
        return sentence
    
    if sentence[posi-1] == ")":
        opPosi = find_opening_posi(posi, sentence)
        print(opPosi)

    if opPosi != -1:
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