import sys

def checkletter(word):
    letterdic={'T0':{"a": "T1", "b": "T1", "c": "T1", "d":"T1" , "e": "T1", "f" : "T1" , "g": "T1","h": "T1","i": "T1", "j": "T1" , "k": "T1",
            "l": "T1", "m": "T1", "n":"T1" , "o": "T1", "p":"T1" , "q" : "T1" , "r": "T1", "s": "T1" , "t": "T1",
            "u": "T1", "v": "T1", "w": "T1", "x":"T1" ,"y": "T1", "z": "T1",
            "A": "T1", "B": "T1", "C":"T1" , "D": "T1", "E":"T1" , "F" : "T1","G":"T1" , "H":"T1" ,
            "I": "T1", "J": "T1", "K": "T1", "L":"T1", "M": "T1", "N" : "T1", "O": "T1", "P":"T1" ,
            "Q": "T1", "R": "T1", "S":"T1", "T": "T1", "U": "T1", "V": "T1", "W":"T1" , "X": "T1", "Y":"T1" , "Z":"T1","_":"T1",
            "0": "T2", "1": "T2", "2": "T2", "3": "T2", "4": "T2", "5": "T2", "6": "T2", "7": "T2",
            "8": "T2", "9": "T2"},
        'T1':{"a": "T1", "b": "T1", "c": "T1", "d":"T1" , "e": "T1", "f" : "T1" , "g": "T1","h": "T1","i": "T1", "j": "T1" , "k": "T1",
            "l": "T1", "m": "T1", "n":"T1" , "o": "T1", "p":"T1" , "q" : "T1" , "r": "T1", "s": "T1" , "t": "T1",
            "u": "T1", "v": "T1", "w": "T1", "x":"T1" ,"y": "T1", "z": "T1",
            "A": "T1", "B": "T1", "C":"T1" , "D": "T1", "E":"T1" , "F" : "T1","G":"T1" , "H":"T1" ,
            "I": "T1", "J": "T1", "K": "T1", "L":"T1", "M": "T1", "N" : "T1", "O": "T1", "P":"T1" ,
            "Q": "T1", "R": "T1", "S":"T1", "T": "T1", "U": "T1", "V": "T1", "W":"T1" , "X": "T1", "Y":"T1" , "Z":"T1","_":"T1",
            "0": "T1", "1": "T1", "2": "T1", "3": "T1", "4": "T1", "5": "T1", "6": "T1", "7": "T1",
            "8": "T1", "9": "T1"}
           }
    symbol='T0'
    word='1operand1'
    for i in range(len(word)):
        symbol=letterdic.get(symbol).get(word[i])
        if symbol=="T2":
            break
    if symbol=='T1':
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

def lexical(word):
    return 0

i=0
inputs=[]
print(sys.argv)
#with open(inputfile,'r',newline='')as filereader:
    #for row in filereader:
        #inputs[i]=row.strip()

print(inputs)


#token_string="word"

#tokendic[token_string]=lexical(word)