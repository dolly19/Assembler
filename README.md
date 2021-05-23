# Assembler
An assembler to translate the assembly code into machine code

An Assembler takes a text file as an input, which contains the Assembly code. It translates the assembly code into machine code. The machine code generated will be saved in a separate text file.

**Input format:**

[Filename] [START] [Location count ]

[Label] [Opcode] [operand] * Number of line

[Label] [CLA] (In case of CLA)

[STP]

**Label is not mandatory

**Assumption:**

1. The address should be in binary form, and if any other format like hex or oct is given, it will be taken as a string, and a new address will be allocated. 
    
2.  Label names can't be repeated, and if still given, they will be allocated different addresses, and line numbers will be clearly emotion in respected tables.
   
3. Variable and Label cannot have the same name, and if still used line num of both will be visible in tables.
    
4. There can be a maximum of 264 labels, literal and variable combined.
    
5. A variable or literal name can never be the same as operands.
    
6. The literal format is "=" followed by an integer value.
    
7. STP is always given.
    
8. The variable should be declared after STP.
    
9. Its format must be [Variable name] followed by "=" than integer value. Eg, A = 6
    
10. Commenting should be after the variables defined.
     
11. Comment should start from "#."

Error reporting:

1. assembly code must start from file followed by START opcode and location counter. if not then it can be
       - Formate error.
       -"START" Not found.
        -The location counter is not of integer type.

2. If any of the lines are blank, it will show Blank line error with line num.

3. Input format keeps in mind; otherwise, it will show " format error with line num" or "an instruction with   too many operands or may not contain enough operands along with line num."

4. If any of the instruction lines are having CLA as an assembly opcode, then that line takes no [operand].

5. The [label] must be of binary or in the form of a variable(string).

6. The [operand] should be literal(i.e., = 3) or can be any variable (i.e., any alphabet, small word ) basically string.

7. All those variables[operand ], which are defined but not used, will show an error. Similarly, variables used but not defined will also print errors with line numbers.

CO Assembler Project

Team Member - Sambhav Jain
