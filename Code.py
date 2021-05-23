#a new address alloted if hex or given oly binary check done
#label name can't be same
#variable and label cannot have  same name and if still used line no. of both will be visible in tables
#no multiple variable defined
#there can be maximun of 264 label,literal and variable
#variable or literal name can never be same as operands
#literal format is (= followed by integer value)
import random
file = open('assembly.txt', 'r')
outputf = open('output.txt', 'w')
lines = file.readlines()
finalList=[]
list=[]
for line in lines:
    line=line.split()
    list.append(line)
literals = []
symbols = []
symbols2=[]
opcodeTable = []
symbolsDefined=[]

def checkVarNdLable(s):
    temp_bool=False
    for i in range(0,len(symbols)):
        if s==symbols[i][0]:
            temp_bool=True
            global VarHelp
            VarHelp=i

    return temp_bool


def checkLiterals(s):
    temp_bool = False
    for i in range(0,len(literals)):
        if s == literals[i][0]:
            temp_bool = True
            global LitHelp
            LitHelp=i

    return temp_bool


def IsBinary(s):
    try:
        if len(s)<2:
            int(s)
            return 'integer'

        else:
            if s[1]=="b":
                return "binary"
            else :
                int(s)
                return 'integer'
    except ValueError or IndexError:
        return 'string'


def IsInteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def checkOpcode(val):
    temp = False
    for i in opcodeG:
        if i[0] == val:
            return True
def getopcode(val):
    for i in range(0,len(opcodeG)):
        if opcodeG[i][0] == val:
            return i


def checkType(s):
    if s[0] == "=":
        return "literal"
    else:
        return "symbol"


def checkSymbol(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

opcodeG = [['CLA', "0000"],
           ['LAC', '0001'],
           ['SAC', '0010'],
           ['ADD', '0011'],
           ['SUB', '0100'],
           ['BRZ', '0101'],
           ['BRN', '0110'],
           ['BRP', '0111'],
           ['INP', '1000'],
           ['DSP', '1001'],
           ['MUL', '1010'],
           ['DIV', '1011'],
           ['STP', '1100'],
           ]

lc = 0

# outputf.write("Error List-")
# outputf.write("\n")
# outputf.write("\n")
print("Error List :")

while not ('STP' in list[lc]):

    if len(list[lc]) == 0:
        print ("Blank Line, line no. ",lc+1)
        # outputf.write("Blank Line, line no. "+str(lc+1)+"\n")
        lc += 1
        continue
    else:
        if lc == 0:

            global Filename
            Filename = list[lc][0]
            if list[lc][1]=="START":
                pass

            else:
                print(' "Start" Not found, line 1')
                # outputf.write(' "Start" Not found, line 1')

            if IsInteger(list[lc][2]):
                global locationCounter
                locationCounter = int(list[lc][2])

            else:
                print('LC must of integer type, line 1 ')
                # outputf.write('LC must of integer type, line 1 ')
        else:
            if checkOpcode(list[lc][0]):
                if list[lc][0] == "CLA":
                    if len(list[lc]) > 1:
                        print("CLA takes no Operand, line no. ", lc + 1)
                        # outputf.write("CLA takes no Operand , line no. "+ str(lc + 1)+ '\n ')
                    else:
                        opcodeTable.append(["CLA",lc+1])
                        finalList.append(list[lc])
                        pass
                else:

                    if len(list[lc]) > 2:
                            print("An opcode is supplied with too many operand, line no.  ", lc + 1)
                            #outputf.write("An opcode is supplied with too many operand, line no. "+ str(lc + 1)+ '\n ')
                    elif len(list[lc]) ==1 :
                            print("An opcode is not supplied with enough operand, line no.  ", lc + 1)
                            #outputf.write("An opcode is not supplied with enough operand, line no. "+ str(lc + 1)+ '\n ')
                    else:
                        if checkSymbol(list[lc][1]):
                            print("Operand must be either literal or in the form of variable(string), line no. ", lc + 1)
                            #outputf.write("Operand must be either literal or in the form of variable(string), line no. " + str(lc + 1)+ '\n ')
                        else:
                            if checkType(list[lc][1])=="literal":
                                if checkLiterals(list[lc][1]):
                                    literals[LitHelp].append(lc+1)
                                    pass
                                else:
                                    literals.append([list[lc][1],lc+1])
                            else:

                                if checkVarNdLable(list[lc][1]):
                                    symbols[VarHelp].append(lc + 1)

                                    pass
                                else:
                                    symbols.append([list[lc][1],"Variable",lc+1])
                                    symbols2.append([list[lc][1],lc+1])
                            opcodeTable.append([list[lc][0], lc + 1])
                            finalList.append(list[lc])
            else:
                if len(list[lc])==1:
                    print("Format error, line no. ", lc+1)
                    #outputf.write("Format error, line no. " + str(lc+1))
                else:
                    if IsBinary(list[lc][0]) == "integer":
                        print("Label must be either binary or in the form of variable, line no. ", lc+1)
                        #outputf.write("Label must be either binary or in the form of variable, line no. " + str(lc+1)+ '\n ')
                        lc+=1
                        continue

                    elif IsBinary(list[lc][0]) == "binary":
                        pass

                    else:
                        if checkVarNdLable(list[lc][0]):
                            symbols[VarHelp].append(lc + 1)
                            pass
                        else:
                            symbols.append([list[lc][0],"Label",lc+1])


                    if checkOpcode(list[lc][1]):
                        if list[lc][1] == "CLA":
                            if len(list[lc]) > 2:
                                print("CLA takes no Operand, line no. ", lc + 1)
                                #outputf.write("CLA takes no Operand , line no. " + str(lc + 1) + '\n ')
                            else:
                                opcodeTable.append(["CLA", lc + 1])
                                finalList.append(list[lc])
                                pass
                        else:

                            if len(list[lc]) > 3:
                                print("An opcode is supplied with too many operand, line no.  ", lc + 1)
                                #outputf.write("An opcode is supplied with too many operand, line no. " + str(lc + 1) + '\n ')
                            elif len(list[lc]) == 2:
                                print("An opcode is not supplied with enough operand, line no.  ", lc + 1)
                                #outputf.write("An opcode is not supplied with enough operand, line no. " + str(lc + 1) + '\n ')

                            else:

                                if checkSymbol(list[lc][2]):
                                    print("Operand must be either literal or in the form of variable(string), line no. ", lc + 1)
                                    #outputf.write("Operand must be either literal or in the form of variable(string), line no. " + str(lc + 1) + '\n ')
                                else:
                                    if checkType(list[lc][2]) == "literal":
                                        if checkLiterals(list[lc][2]):
                                            literals[LitHelp].append(lc + 1)
                                            pass
                                        else:
                                            literals.append([list[lc][2], lc+1])
                                    else:
                                        if checkVarNdLable(list[lc][2]):
                                            symbols[VarHelp].append(lc + 1)
                                            pass
                                        else:
                                            symbols.append([list[lc][2], "Variable", lc+1])
                                            symbols2.append([list[lc][2],lc+1])
                                    opcodeTable.append([list[lc][1], lc + 1])
                                    finalList.append(list[lc])
                    else:
                        print("opcode not found, line no.", lc + 1)
                        #outputf.write("opcode not found, line no. " + str(lc + 1) + "\n")

    lc+=1
lc=lc+1
#Literal Defined But Not Used
#outputf.write("\n")
for i in range(lc,len(lines)):
    tempbool=False
    var=lines[i]
    if var == "\n":
        continue
#comments at last
    if var[0]=='#':
        break
    symbolsDefined.append(var)
    for j in range(0,len(symbols)):
        if var[0] == symbols[j][0]:
            tempbool=True
            break
        else:
            pass
    if tempbool == False:
        print("Variable Defined But Not Used , line no." , i+1)
        s = str(i+1)
        #outputf.write("Variable Defined But Not Used , line no." + s + '\n ')


#Literal Used But Not Defined
for i in range(0,len(symbols2)):
    tempbool=False
    temp=0
    var=symbols2[i]
    for j in symbolsDefined:
        if var[0] == j[0]:
            temp=j
            tempbool=True
            break
        else:
            pass
    if tempbool == False:
        print("Variable Used But Not Defined, line no." , var[1])
        #outputf.write("Variable Used But Not Defined, line no." + str(var[1]) + '\n ')

outputf.write("\n")
outputf.write("Machine Code-")
outputf.write("\n")
randomvar=[]
def checkrval():
    rval = random.randrange(256, 511)
    for i in range(0,len(randomvar)):
        if rval==randomvar[i]:
            return checkrval()
    randomvar.append(rval)
    return rval

finalList2= []
for i in range(0,len(finalList)):
    finalList2.append([])
    for j in range(0,len(finalList[i])):
        finalList2[i].append([0])


for i in range(0,len(finalList)):
    for j in range(0,len(finalList[i])):
        if IsBinary(finalList[i][j])=='binary':
            finalList2[i][j]=(finalList[i][j])
        elif checkOpcode(finalList[i][j]):
            temporary = getopcode(finalList[i][j])

            finalList2[i][j]=opcodeG[temporary][1]
        else:
            finalList2[i][j]=bin(checkrval())


for i in range(0,len(finalList2)):
    for j in range(0,len(finalList2[i])):
        outputf.write(finalList2[i][j]+" ")
    outputf.write("\n")

# for i in symbols:
#     print(i)

# for i in literals:
#      print(i)

# for i in opcodeTable:
#     print(i)
# for i in finalList:
#     print (i)
# for i in finalList2:
#     print (i)
#outputf.write("\n")
print("Opcode Table:")
#outputf.write("Opcode Table-")
#outputf.write("\n")
#outputf.write("\n")

for i in range(0,len(opcodeTable)):

    print(opcodeTable[i][0]+ " Line no. " + str(opcodeTable[i][1]))

#outputf.write("\n")
#outputf.write("literal Table-")
#outputf.write("\n")
#outputf.write("\n")
print("literal Table:")

for i in range(0,len(literals)):
    for j in range(0,len(literals[i])):
        if j==0:
            print(literals[i][j],end=" ")
        elif j==1:
            print("Line no. " + str(literals[i][j]) ,end=" ")
        else:
             print("," + str(literals[i][j])+" ")
    #outputf.write("\n")

#outputf.write("\n")
#outputf.write("Symbol Table-")
print("Symbol Table:")
#outputf.write("\n")
#outputf.write("\n")


for i in range(0,len(symbols)):
    for j in range(0,len(symbols[i])):
        if j==0 or j==1:
            print(symbols[i][j],end=" ")
        elif j==2:
            print("Line no. "+str(symbols[i][j]))
        else:
            print(',' + str(symbols[i][j])+ " ")
    #outputf.write("\n")
