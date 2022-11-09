import sys

ident= 0
const=1
factor=2
factor_tail = 3
term = 4
term_tail = 5
expression = 6
statement = 7
statements = 8
program = 9
assignment_op = 10
semi_colon = 11
add_operator = 12
mult_operator = 13
left_paren = 14
right_paren = 15
token_dic={'ident': 0,'const':1,":=": 10,';' : 11,'+' : 12, '-': 12,"*" : 13, "/": 13,'(' : 14,')' : 15, 'errorid':16 }

def lexical(inputs):
    checkdic={'T0': {"a": "T1", "b": "T1", "c": "T1", "d": "T1", "e": "T1", "f": "T1", "g": "T1", "h": "T1", "i": "T1",
            "j": "T1", "k": "T1",
            "l": "T1", "m": "T1", "n": "T1", "o": "T1", "p": "T1", "q": "T1", "r": "T1", "s": "T1", "t": "T1",
            "u": "T1", "v": "T1", "w": "T1", "x": "T1", "y": "T1", "z": "T1",
            "A": "T1", "B": "T1", "C": "T1", "D": "T1", "E": "T1", "F": "T1", "G": "T1", "H": "T1",
            "I": "T1", "J": "T1", "K": "T1", "L": "T1", "M": "T1", "N": "T1", "O": "T1", "P": "T1",
            "Q": "T1", "R": "T1", "S": "T1", "T": "T1", "U": "T1", "V": "T1", "W": "T1", "X": "T1", "Y": "T1",
            "Z": "T1", "_": "T1",
            "0": "T2", "1": "T2", "2": "T2", "3": "T2", "4": "T2", "5": "T2", "6": "T2", "7": "T2",
            "8": "T2", "9": "T2", ":": "T6", ';': "T3", '+': "T4", '-': "T4", "*": "T5", "/": "T5", '(': "T7",
            ')': "T8"},
     'T1': {"a": "T1", "b": "T1", "c": "T1", "d": "T1", "e": "T1", "f": "T1", "g": "T1", "h": "T1", "i": "T1",
            "j": "T1", "k": "T1",
            "l": "T1", "m": "T1", "n": "T1", "o": "T1", "p": "T1", "q": "T1", "r": "T1", "s": "T1", "t": "T1",
            "u": "T1", "v": "T1", "w": "T1", "x": "T1", "y": "T1", "z": "T1",
            "A": "T1", "B": "T1", "C": "T1", "D": "T1", "E": "T1", "F": "T1", "G": "T1", "H": "T1",
            "I": "T1", "J": "T1", "K": "T1", "L": "T1", "M": "T1", "N": "T1", "O": "T1", "P": "T1",
            "Q": "T1", "R": "T1", "S": "T1", "T": "T1", "U": "T1", "V": "T1", "W": "T1", "X": "T1", "Y": "T1",
            "Z": "T1", "_": "T1",
            "0": "T1", "1": "T1", "2": "T1", "3": "T1", "4": "T1", "5": "T1", "6": "T1", "7": "T1",
            "8": "T1", "9": "T1", ":": "T6", ';': "T3", '+': "T4", '-': "T4", "*": "T5", "/": "T5", '(': "T7",
            ')': "T8"},
     'T2': {"a": "T9", "b": "T9", "c": "T9", "d": "T9", "e": "T9", "f": "T9", "g": "T9", "h": "T9", "i": "T9",
            "j": "T9", "k": "T9",
            "l": "T9", "m": "T9", "n": "T9", "o": "T9", "p": "T9", "q": "T9", "r": "T9", "s": "T9", "t": "T9",
            "u": "T9", "v": "T9", "w": "T9", "x": "T9", "y": "T9", "z": "T9",
            "A": "T9", "B": "T9", "C": "T9", "D": "T9", "E": "T9", "F": "T9", "G": "T9", "H": "T9",
            "I": "T9", "J": "T9", "K": "T9", "L": "T9", "M": "T9", "N": "T9", "O": "T9", "P": "T9",
            "Q": "T9", "R": "T9", "S": "T9", "T": "T9", "U": "T9", "V": "T9", "W": "T9", "X": "T9", "Y": "T9",
            "Z": "T9", "_": "T9",
            "0": "T2", "1": "T2", "2": "T2", "3": "T2", "4": "T2", "5": "T2", "6": "T2", "7": "T2",
            "8": "T2", "9": "T2", ":": "T6", ';': "T3", '+': "T4", '-': "T4", "*": "T5", "/": "T5", '(': "T7", ')': "T8"
            },
     'T6': {"=": "T10"}}

    symbol="T0"
    i = 0
    lexem=inputs[i]

    symbol = checkdic[symbol][inputs[i]]
    others=[ ":", ';', '+', '-', "*", "/", '(', ')']
    while(i<len(inputs)):
        i+=1
        if(symbol=="T9"):
            while(True):
                if(inputs[i] in others):
                    next_token.append(16)
                    token_string.append(lexem)
                    symbol = checkdic["T0"][inputs[i]]
                    lexem = inputs[i]
                    break
                lexem=lexem+inputs[i]
                i+=1
        elif(symbol=="T1" or symbol=="T2"):
            if(i==len(inputs)):
                if(symbol=="T1"):
                    next_token.append(0)
                    token_string.append(lexem)
                if(symbol=="T2"):
                    next_token.append(1)
                    token_string.append(lexem)
            else:
                if(symbol=="T1" and symbol!=checkdic[symbol][inputs[i]]):
                    next_token.append(0)
                    token_string.append(lexem)
                    symbol = checkdic["T0"][inputs[i]]
                    lexem=inputs[i]
                elif(symbol=="T2" and symbol!=checkdic[symbol][inputs[i]] and checkdic[symbol][inputs[i]]!="T9"):
                    next_token.append(1)
                    token_string.append(lexem)
                    symbol = checkdic["T0"][inputs[i]]
                    lexem = inputs[i]
                else:
                    symbol= checkdic[symbol][inputs[i]]
                    lexem = lexem+inputs[i]

        elif(symbol=="T6"):
            lexem = lexem + inputs[i]
            next_token.append(10)
            token_string.append(lexem)
            i+=1
            lexem=inputs[i]
            symbol=checkdic["T0"][inputs[i]]
        elif (symbol == "T3"):
            next_token.append(11)
            token_string.append(lexem)
            symbol = checkdic["T0"][inputs[i]]
            lexem = inputs[i]
        elif (symbol == "T4"):
            next_token.append(12)
            token_string.append(lexem)
            symbol = checkdic["T0"][inputs[i]]
            lexem = inputs[i]
        elif (symbol == "T5"):
            next_token.append(13)
            token_string.append(lexem)
            symbol = checkdic["T0"][inputs[i]]
            lexem = inputs[i]
        elif (symbol == "T7"):
            next_token.append(14)
            token_string.append(lexem)
            symbol = checkdic["T0"][inputs[i]]
            lexem = inputs[i]
        elif (symbol == "T8"):
            next_token.append(15)
            token_string.append(lexem)
            if(i!=len(inputs)):
                symbol = checkdic["T0"][inputs[i]]
                lexem = inputs[i]
        else:
            symbol = checkdic[symbol][inputs[i]]
            lexem = lexem+inputs[i+1]

num=0
temp=0
result=0
error=0
message=""
warnings=0
termfactorcount=0
unknown=0
def program_f():
    statements_f()

def statements_f():
    global num,temp,result,error,idcount, constcount, opcount,warnings,message,unknown,termfactorcount
    idcount,constcount,opcount,error,warnings,termfactorcount=0,0,0,0,0,0
    message=""

    statement_f()

    if (num < len(token_string)):
        print("%s" % token_string[num], end='')
    print("\nID: %d; CONST: %d; OP: %d" %(idcount, constcount, opcount))
    if error==1:
        print("(ERROR)%s"%message)

        pos = [i for i in range(num) if next_token[i] == 10]
        indexnum = pos[-1] - 1
        result_dic[token_string[indexnum]]="Unknown"

    elif warnings==1:
        print("(Warning)%s"%message)
    else:
        print("(OK)")


    if(num<len(next_token) and next_token[num]==11): #semicolon 임을 확인하는 작업 맞으면 +1 해서 다음 토큰 확인하기
        num+=1
        statements_f()

    elif(num==len(next_token)):
        return True
    else:
        error=1
        message="'문법 오류'"
        return False

def statement_f():
    global num,temp,result,error,idcount, constcount, opcount,message,termfactorcount,oneop
    if(next_token[num]==0): #ident인지 확인하는 작업 맞으면 +=1 해서 다음 토큰 확인하기
        idcount+=1
        print("%s"%token_string[num],end='')
        result_dic[token_string[num]]=0
        temp=0
        result=0
        num+=1
        if(next_token[num]==10):
            print("%s" % token_string[num], end='')
            num+=1
            result = expression_f()
            pos = [i for i in range(num) if next_token[i] == 10]
            indexnum = pos[-1]-1
            if(termfactorcount==2):
                result=oneop
            result_dic[token_string[indexnum]]=result

        else:
            error=1
            message="'문법 오류'"
            return False
    else:

        error = 1
        message="'문법 오류'"
        return False

def expression_f():
    global num, result,error,idcount, constcount, opcount
    num1 = term_f()
    return term_tail_f(num1)

def term_tail_f(num1):
    global num,result,error,idcount, constcount, opcount,warnings,message,termfactorcount
    termfactorcount+=1
    if(num<len(next_token) and next_token[num]==12):
        print("%s" % token_string[num], end='')
        if(next_token[num+1]==12):
            if(token_string[num]=='-'):
                error=1
                message="'(-)중복 연산자, 문법 규칙 위반'"
            else:
                warnings=1
                message="'중복연산자 (+) 제거'"
                del token_string[num]
                del next_token[num]
        if (token_string[num] == '+'):
            num += 1
            t=term_f()
            if(type(num1) is not str and type(t) is not str):
                result = t + num1

        else:
            num += 1
            t=term_f()
            if (type(num1) is not str and type(t) is not str):
                result = num1 - t
        opcount+=1
        term_tail_f(result)
        return result
    elif (num == len(token_string)):
        return num1
    elif(next_token[num] == 11 or (next_token[num] == 15 and (14 in next_token[:num])) or next_token[num]==12):
        return num1
    else:
        error=1
        if(next_token[num] == 15 and (14 in next_token[:num])==False):
            message="'문법 오류' left_paren없음"
        else:
            message = "'문법 오류'"
        while(next_token[num]!=11):
            print("%s" % token_string[num], end='')
            if(next_token[num]==0):
                idcount+=1
            elif(next_token[num]==1):
                constcount+=1
            elif(next_token[num]==12 or next_token[num]==13):
                opcount+=1
            num+=1
            if(num == len(next_token)):
                break

        return False

def term_f():
    global num, result,error,idcount, constcount, opcount
    num1=factor_f()
    return factor_tail_f(num1)

def factor_tail_f(num1):
    global num,result,error,idcount, constcount, opcount,termfactorcount
    termfactorcount += 1
    if( num<len(next_token) and next_token[num]==13):
        print("%s" % token_string[num], end='')
        if(token_string[num]=='*'):
            num+=1
            t=factor_f()
            if (type(num1) is not str and type(t) is not str):
                result=num1*t
        else:
            num+=1
            t=factor_f()
            if (type(num1) is not str and type(t) is not str):
                if(t!=0):
                    result=num1/t
                else:
                    error = 1
                    message = "'0으로 나누기 실행'"
                    result='Unknown'
                    return False

        opcount+=1
        factor_tail_f(result)
        return result
    elif (num == len(token_string)):
        return num1
    elif( next_token[num] == 11 or (next_token[num] == 15 and (14 in next_token[:num])) or next_token[num]==12 ):
        return num1
    else:
        error = 1
        message = "'문법 오류'"
        while (next_token[num-1] == 11 or num == len(next_token)):
            print("%s" % token_string[num], end='')
            num += 1
        result='Unknown'
        return result

def factor_f():
    global num,result,error,idcount,constcount,opcount,message,unknown,oneop
    if(next_token[num]==14):
        print("%s" % token_string[num], end='')
        num+=1
        t = expression_f()
        if(next_token[num]==15):
            print("%s" % token_string[num], end='')
            num+=1
            return t
        else:
            message="'문법 오류(right_paren 없음)'"
            error = 1
            return False
    else:
        print("%s" % token_string[num], end='')
        if(next_token[num]==0):
            if token_string[num] in result_dic:
                if(result_dic[token_string[num]]=='Unknown'):
                    error = 1
                    message = "'정의되지 않은 변수(" + token_string[num] + ")가 참조됨'"
                    result_dic[token_string[num]] = 'Unknown'
                    unknown = 1
                    num += 1
                    result='Unknown'
                    return result
                else:
                    temp=result_dic[token_string[num]]
                    oneop=result_dic[token_string[num]]

                    num+=1
                    idcount+=1
                    return temp
            else:
                error = 1
                message = "'정의되지 않은 변수(" + token_string[num] + ")가 참조됨'"
                result_dic[token_string[num]] = 'Unknown'
                unknown = 1
                num += 1
                result = 'Unknown'
                return result
        elif(next_token[num]==16):
            error = 1
            message = "'identifier rule 위반'"
            result_dic[token_string[num]] = 'Unknown'
            num += 1
            return False
        elif(next_token[num]==1):
            temp= int(token_string[num])
            oneop=int(token_string[num])
            #if (result == 0):
                #result = temp
            num += 1
            constcount+=1
            return temp
        else:
            message="'문법 오류'"
            error=1
            return False




next_token = []
token_string = []
result_dic={} #symboltable 역할을 한다.
input_string=""


def main():
    global input_string
    inputfile = sys.argv[1]
    f = open(inputfile,'r')
    #f = open('hello.txt', 'r')
    data = f.readlines()
    f.close()
    for line in data:
        input_string=input_string+line.strip()

    input_string=input_string.replace(" ","")
    lexical(input_string)
    program_f()
    print("result=> ",end='')
    for key, value in result_dic.items():
        print("%s:"%(key),end="")
        print(value,end='')
        print("; ",end='')

if __name__=="__main__":
    main()

