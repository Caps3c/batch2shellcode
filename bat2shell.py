import os ,sys
### a script that reads a batch file then outputs a shellcode of the batch file

## a function to output the shell code to txt file with the name shellcode.txt
def write_shellcode():
    try:
        if sys.argv[2]=="txt":
            output = open("shellcode.txt","w")
            output.write(shellcode)
            output.close()
        else:
            pass
    except IndexError:
        pass

try:
    
## open the batch file to read it's contents

    handle = open(sys.argv[1], "rb")
    dump = handle.read()
    handle.close()

    shellcode = ""
### checks every byte and turns the number to a hex string
    for byte in dump:
        hex_byte = (hex(byte))
        hex_byte = "\\"+(hex_byte[1:])
        if len(hex_byte)==3:
            hex_byte = hex_byte+"0"
        else:
            pass
        shellcode += hex_byte 
        #print (hex_byte)
    print ("The shell code of the following batch file is : "+sys.argv[1]) 
    print (shellcode)
    write_shellcode()
#print (dump)

except IndexError:
    print ("no input files was detected \n")
    print ("Usage: python batreader.py batchfile")
except FileNotFoundError:
    print ("No such batch file was found " +sys.argv[1])



### author: capsec
### Friday 03/01/2020
### email capsec@protonmail.com
