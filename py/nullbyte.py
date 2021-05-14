import subprocess
import re # https://regex101.com/
import os

def CheckNullBytes(shellcode):
    NB = False
    for i in range(0, len(shellcode), 2):
        if shellcode[i:i+2] == "00":
            NB = True
            print("NullBytes here : " + shellcode[i:i+2])
    if NB == False:
        print("No NullBytes.")
    return("test")
        


name="/home/migoliatte/progra/security_shellcode/asm/calculatrice_no_nullByte"
os.system("nasm -f elf "+name+".asm  && ld "+name+".o -m elf_i386 -o "+name)
p = subprocess.run('objdump -d '+name,shell=True,stdout=subprocess.PIPE)
p = p.stdout.decode("utf-8")

p=p.replace("\t","")
result=re.findall(":[0-9a-f ]{21}",p)
resultfinal=[]
for res in result:
    resultfinal.append(res[1:].replace(" ",""))

#CheckNullBytes("".join(resultfinal))

#print(str(int(len("".join(resultfinal))/2)))
resultfinal="".join(resultfinal)
second=""
for i in range(0, len(resultfinal), 2):
    second+="\\x"+resultfinal[i:i+2]

print(second)
