import subprocess
import re # https://regex101.com/
import os
import sys

def help():
    print("<---------- HELP ---------->")
    print("-h Affiche ce méssage")
    print("-s Création de lu shellcode")
    print("-c compile exploit.c et le lance")
    print("<---------- HELP ---------->")
    exit()

def recupArgument(verbose):
    print("<---------- Récupération du nom du fichier en cours ---------->")
    name=""
    if(  len(sys.argv) == 1  ):
        name = input("Entrez le nom du fichier .asm  :")
    else:
        name=str(sys.argv[1])
    file_test=subprocess.run("ls "+name,shell=True,stdout=subprocess.PIPE)
    if( file_test.returncode != 0 ):
        print("Le fichier "+name+" n'existe pas !")
        exit()
    name=name.split(".asm")
    name=name[0]
    print("Nom du fichier : "+name)
    return name

def objdump(verbose):
    name=recupArgument(verbose)
    print("<---------- Lancement de ObjDump en cours ---------->")
    os.system("nasm -f elf "+name+".asm  && ld "+name+".o -m elf_i386 -o "+name)
    if(verbose):
        print("Lancement de la commande objdump -d "+name)
    objdump = subprocess.run('objdump -d '+name,shell=True,stdout=subprocess.PIPE)
    objdump = objdump.stdout.decode("utf-8")
    if(verbose):
        print("Resultat de OBJDUMP :"+objdump)
    objdump=objdump.replace("\t","")
    result=re.findall(":[0-9a-f ]{21}",objdump)
    return result

def CheckNullBytes(verbose,shellcode):
    print("<---------- Check des NUllsBytes en cours ---------->")
    NB = False
    for i in range(0, len(shellcode), 2):
        if shellcode[i:i+2] == "00":
            NB = True
            print("NullBytes here : " + shellcode[i:i+2])
    
    if NB == False:
        print("Pas de NullBytes détécté.")
    else:
        exit()

def cleanOpCode(verbose):
    resultfinal=[]
    for res in objdump(verbose):
        resultfinal.append(res[1:].replace(" ",""))
    print("<---------- Nettoyage de l'opcode en cours ---------->")
    resultfinal="".join(resultfinal)
    CheckNullBytes(verbose,resultfinal)
    if(verbose):
        print("Opcode nettoyé : "+resultfinal)
    return resultfinal

def shellcodeCreation(verbose):
    resultfinal=cleanOpCode(verbose)
    print("<---------- Génération de l'exploit en cours ---------->")
    exploit=""
    for i in range(0, len(resultfinal), 2):
        exploit+="\\x"+resultfinal[i:i+2]
    print("Shellcode : "+exploit)
    print("Taille de l'exploit : "+str(int(len(resultfinal)/2)))

def lancementCodeC(verbose):
    print("<---------- Compilation et lancement de exploit.c ---------->")
    if(verbose):
        print("Lancement de la commande gcc -o exploit c/exploit.c -z execstack -m32 -fno-stack-protector")
    os.system("gcc -o exploit c/exploit.c -z execstack -m32 -fno-stack-protector")
    if(verbose):
        print("Lancement de l'executable ./exploit") 
    os.system("./exploit ")

def menu():
    array=[0,0,0,0]
    for i in range(0,len(sys.argv)):
        if str(sys.argv[i]) == "-h":
            array[0]=1
        elif str(sys.argv[i]) == "-v":
            array[3]=1
        elif str(sys.argv[i]) == "-s":
            array[1]=1
        elif str(sys.argv[i]) == "-c":
            result = input("Avez vous pensé à changer la variable 'shellcode' de exploit.c ([y/yes/o/oui]/[n/no/non]) :  ")
            result = result.lower()
            if( result == "y" or result == "yes" or result == "o" or result == "oui" ):
                print("Très bien, continuons !")
            elif( result == "n" or result == "no" or result == "non"):
                print("Allez le modifier !")
                exit()
            else:
                print("Merci de répondre y/yes/o/oui ou n/no/non merci !")
                exit()
            array[2]=1
    return array

def main():
    array=menu()
    if array[0] == 1:
        help()
    elif array[1] == 1:
        shellcodeCreation(array[3])
    elif array[2] == 1:
        lancementCodeC(array[3])
        exit()
    else:
        help()

if __name__ == "__main__":
    main()