import sys

def checkletter(word):
    letterdic={'T0':{"a": "T1", "b": "T1", "c": "T1", "d": "T1", "e": "T1", "f" : "T1" , "g": "T1","h": "T1","i": "T1", "j": "T1" , "k": "T1",
            "l": "T1", "m": "T1", "n":"T1" , "o": "T1", "p": "T1" , "q" : "T1" , "r": "T1", "s": "T1" , "t": "T1",
            "u": "T1", "v": "T1", "w": "T1", "x": "T1" ,"y": "T1", "z": "T1",
            "A": "T1", "B": "T1", "C":"T1" , "D": "T1", "E":"T1" , "F" : "T1","G":"T1" , "H":"T1" ,
            "I": "T1", "J": "T1", "K": "T1", "L": "T1", "M": "T1", "N" : "T1", "O": "T1", "P":"T1" ,
            "Q": "T1", "R": "T1", "S":"T1", "T": "T1", "U": "T1", "V": "T1", "W":"T1" , "X": "T1", "Y":"T1" , "Z":"T1","_":"T1",
            "0": "T2", "1": "T2", "2": "T2", "3": "T2", "4": "T2", "5": "T2", "6": "T2", "7": "T2",
            "8": "T2", "9": "T2", ":":"T2", ';': "T2",'+': "T2", '-': "T2", "*": "T2", "/": "T2",'(': "T2",')': "T2"},
        'T1':{"a": "T1", "b": "T1", "c": "T1", "d": "T1" , "e": "T1", "f" : "T1" , "g": "T1","h": "T1","i": "T1", "j": "T1" , "k": "T1",
            "l": "T1", "m": "T1", "n":"T1" , "o": "T1", "p":"T1" , "q" : "T1" , "r": "T1", "s": "T1" , "t": "T1",
            "u": "T1", "v": "T1", "w": "T1", "x": "T1" ,"y": "T1", "z": "T1",
            "A": "T1", "B": "T1", "C":"T1" , "D": "T1", "E": "T1" , "F": "T1","G": "T1" , "H": "T1" ,
            "I": "T1", "J": "T1", "K": "T1", "L": "T1", "M": "T1", "N": "T1", "O": "T1", "P": "T1" ,
            "Q": "T1", "R": "T1", "S":"T1", "T": "T1", "U": "T1", "V": "T1", "W": "T1" , "X": "T1", "Y":"T1" , "Z": "T1", "_": "T1",
            "0": "T1", "1": "T1", "2": "T1", "3": "T1", "4": "T1", "5": "T1", "6": "T1", "7": "T1",
            "8": "T1", "9": "T1"}
        }
    symbol='T0'
    for i in range(len(word)):
        symbol=letterdic[symbol][word[i]]
        if (symbol=="T2"):
            break
    if (symbol=='T1'):
        return True
    else:
        return False

def checkdigit(word):
    symbol="T0"

    digitdic={"T0":{"0": "T2", "1": "T1", "2": "T1", "3": "T1", "4": "T1", "5": "T1", "6": "T1", "7": "T1",
    "8": "T1", "9": "T1"},
              "T1":{"0": "T1", "1": "T1", "2": "T1", "3": "T1", "4": "T1", "5": "T1", "6": "T1", "7": "T1",
    "8": "T1", "9": "T1"},
              "T2":{"0": "T2", "1": "T2", "2": "T2", "3": "T2", "4": "T2", "5": "T2", "6": "T2", "7": "T2",
    "8": "T2", "9": "T2"}
              }
    for i in range(len(word)):
        symbol=digitdic.get(symbol,"T3").get(word[i],"T3")
        if symbol=="T3":
            break
    if symbol=="T2":
        return "F" #0으로 시작하는 숫자 그래서 word[1:]로 고쳐주면 됨
    elif symbol=="T1":
        return True
    else:
        return False #digit 아님




#token_string="word"

#tokendic[token_string]=lexical(word)

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
token_dic={'ident': 0,'const':1,":=": 10,';' : 11,'+' : 12, '-': 12,"*" : 13, "/": 13,'(' : 14,')' : 15 }

num=0
temp=0
result=0

def program_f():
    statements_f()

def statements_f():
    global num,temp,result
    j = num
    statement_f()
    idcount= [i for i in range(j,num) if next_token[i]==0]
    constcount = [i for i in range(j, num) if next_token[i] == 1]
    opcount = [i for i in range(j, num) if (next_token[i] == 12 or next_token[i] == 13)]
    for i in range(j,num+1):
        if(num==len(next_token)):
            break
        print(token_string[i],end='')
    print("\nID: %d; CONST: %d; OP: %d" % (len(idcount), len(constcount),len(opcount)))
    print("(OK)")

    if(num<len(next_token) and next_token[num]==11): #semicolon 임을 확인하는 작업 맞으면 +1 해서 다음 토큰 확인하기
        num+=1
        statements_f()
    elif(num-1==len(next_token)):
        return True
    else:
        print(num)
        print("ERROR")
        return False

def statement_f():
    global num,temp,result
    if(next_token[num]==0): #ident인지 확인하는 작업 맞으면 +=1 해서 다음 토큰 확인하기
        result_dic[token_string[num]]=0
        temp=0
        result=0
        num+=1
        if(next_token[num]==10):
            num+=1
            expression_f()
            pos = [i for i in range(num) if next_token[i] == 10]
            indexnum = pos[-1]
            result_dic[token_string[indexnum]]=result
        else:
            print(num)
            print("ERROR")
            return False
    else:
        print(num)
        print("ERROR")
        return False

def expression_f():
    global num, temp,result
    term_f()
    term_tail_f()

def term_tail_f():
    global num,temp,result
    if(num<len(next_token) and next_token[num]==12):
        if(next_token[num+1]==12):
            print("(Warning)'중복연산자(%s)제거'"%token_string[num+1])
            del token_string[num]
            del next_token[num]
        if (token_string[num] == '+'):
            num += 1
            term_f()
            result = result + temp
        else:
            num += 1
            term_f()
            result = result - temp
        term_tail_f()
    else:
        return True

def term_f():
    global num, temp,result
    factor_f()
    factor_tail_f()


def factor_tail_f():
    global num,temp,result
    if( num<len(next_token) and next_token[num]==13):
        if(token_string[num]=='*'):
            num+=1
            factor_f()
            result = result * temp
        else:
            num+=1
            factor_f()
            result = result/temp
        factor_tail_f()
    else:
        return True

def factor_f():
    global num, temp,result
    if(next_token[num]==14):
        num+=1
        expression_f()
        if(next_token[num]==15):
            num+=1
            return True
        else:
            print("ERROR")
            print(num)
            return False
    else:
        if(next_token[num]==0):
            temp=result_dic[token_string[num]]
            num+=1
            return True
        elif(next_token[num]==1):
            temp= int(token_string[num])
            num += 1
            return True
        else:
            print("ERROR")
            print(num)
            return False




next_token = []
token_string = []
result_dic={} #symboltable 역할을 한다.
data=[]
def main():
    #inputfile = sys.argv[1]
    #f = open(inputfile,'r')
    f = open('hello.txt', 'r')
    data = f.readlines()
    f.close()
    print(data)
    for line in data:
        i=0
        lexeme = ''
        line=line.strip()
        for i in range(len(line)):
            if (len(line)-1==i):
                lexeme+=line[i]
            if(line[i]!=' ' and len(line)-1!=i):
                lexeme+=line[i]
            else:
                if(lexeme=='\n'):
                    continue
                elif(checkletter(lexeme)):
                    next_token.append(0)
                    token_string.append(lexeme)
                elif(checkdigit(lexeme)):
                    if(checkdigit(lexeme)=='F'):
                        print('error')
                        next_token.append(1)
                        token_string.append(lexeme[1:])
                    else:
                        next_token.append(1)
                        token_string.append(lexeme)
                else:
                    next_token.append(token_dic.get(lexeme))
                    token_string.append(lexeme)
                lexeme = ''

    print(next_token)
    print(token_string)
    #result_dic[token_string[3]]=0
    #result_dic[token_string[3]]+=3
    program_f()
    print(result_dic)
if __name__=="__main__":
    main()

