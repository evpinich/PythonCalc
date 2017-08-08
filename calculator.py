""""Funcrion for parsing lexem and calculate them"""
def parser_lexem_and_calc(lex):
    list_element = []
    symbolBufer = ""
    for symbol in lex:
        if (len(symbolBufer)>0) and (symbol in  "+-"):
            list_element.append(symbolBufer)
            symbolBufer=""
        if (symbol in  "*/"):
            list_element.append(symbolBufer)
            list_element.append(symbol)
            symbolBufer=""
        if symbol in  "-+1234567890.":
            symbolBufer=symbolBufer+symbol         
    list_element.append(symbolBufer)        
    for i in range(len(list_element)-1):
        if (i>0) and (list_element[i]=="*")and (len(list_element)):
            list_element[i+1]=str(float(list_element[i-1])*float(list_element[i+1]))
            list_element[i-1]="0"
            list_element[i]="0"
        if (i>0) and (list_element[i]=="/")and (len(list_element)):
            list_element[i+1]=str(float(list_element[i-1])/float(list_element[i+1]))
            list_element[i-1]="0"
            list_element[i]="0"    
    ansver=0;
    for i in range(len(list_element)):
       ansver=ansver+float( list_element[i])
    return ansver
""""Funcrion lexem extractor from expression"""
def lexem_extractor_from_expression(express):
    countOpeningBrackets=0
    countClosingBrackets=0
    beginIndexLem=0
    endIndexLem=0
    counter=0
    lexemFieldFlag=False
    for i in express:
        counter +=1  
        if (i=="("):
            lexemFieldFlag=True
            beginIndexLem=counter
            countOpeningBrackets += 1
        if  (lexemFieldFlag==False) and ( i==")"):
            countClosingBrackets += 1
        if  lexemFieldFlag and ( i==")"):
            lexemFieldFlag=False
            endIndexLem=counter-1
            countClosingBrackets += 1
            lexem=express[beginIndexLem:endIndexLem]
            express=express[0:beginIndexLem-1]+str( parser_lexem_and_calc(lexem) )+express[endIndexLem+1:len(express)]  
            break
    return express
    
print("*****************")
expression=input("Введите выражение в формате ПРИМЕР: 23-(34*34)/(30-5)+23-(34*34)/(30-5)\n")
print("*******************************************************")
while "(" in expression:
    expression= lexem_extractor_from_expression(expression)
    print("step of calculation expression",expression)   
expression= parser_lexem_and_calc (expression)
print("*******************************************************")
print("ОТВЕТ=",expression)
print("*******************************************************")
