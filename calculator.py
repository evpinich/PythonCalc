class Calculator(object):

    __errorState  = False
    __errorMasage = set()
 
    """"Method for calculating expression  -------------------------------------------------------------------------"""  
    def calcExpression(self,expression):
        self.__errorStatus=False
        self.__errorMasage=set()
        
        proxyExpression = expression.strip(" \t\n")
        countLeftBrackets=0
        countRightBrackets=0
        for symbol in proxyExpression:
            if (symbol==")"):countLeftBrackets += 1
            if (symbol=="("):countRightBrackets += 1
        if not(countLeftBrackets==countRightBrackets):
            self.__errorStatus=True;
            self.__errorMasage.add("ERROR: обнаружены непарные скопки внутри выражения")

        try:
            while "(" in proxyExpression:
                lexem = "("+self.__findLexemInsideExpression(proxyExpression)+")"
                resultOfLexem = str(self.__calcLexem(lexem) )
                proxyExpression=proxyExpression.replace(lexem,resultOfLexem)      
            result=self.__calcLexem(proxyExpression)
        except:
              self.__errorStatus=True;
              self.__errorMasage.add("ERROR: обнаружена неизвестная синтаксическая ошибка")      
        if (self.__errorStatus) : return self.__errorMasage
        else: return result
      
    """"Method that doing calculation of simple lexem  -------------------------------------------------------------"""
    def __calcLexem(self,lexem):
        list_element = []
        symbolBufer = ""
        for symbol in lexem:
            if (not(symbol in "()-+*/.1234567890")):
                self.__errorStatus=True
                self.__errorMasage.add("ERROR: обнаружен недопустимый символ внутри выражения")
                return 0
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
                try:
                    list_element[i+1]=str(float(list_element[i-1])/float(list_element[i+1]))
                except ZeroDivisionError:
                    self.__errorStatus=True;
                    self.__errorMasage.add("ERROR: обнаружено деление на ноль внутри выражения")

                list_element[i-1]="0"
                list_element[i]="0"
        ansver=0
        
        for i in range(len(list_element)):
           ansver=ansver+float( list_element[i])
        return ansver
    
    """"Method that extractoring simple lexem from expression  -----------------------------------------------------"""
    def __findLexemInsideExpression(self,expression):
        lexem=""
        countOpeningBrackets=0
        countClosingBrackets=0
        beginIndexLem=0
        endIndexLem=0
        counter=0
        lexemFieldFlag=False
        for i in expression:
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
                lexem=expression[beginIndexLem:endIndexLem]
                break
        return lexem


ClassCalc=Calculator()    
user_expression=input("Введите выражение в формате ПРИМЕР: 23-(34*34)/(30-5)+23-(34*34)/(30-5)\n")
print("*******************************************************")
print("ОТВЕТ=",ClassCalc.calcExpression(user_expression))
print("*******************************************************")
