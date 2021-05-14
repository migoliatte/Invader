def CheckNullBytes(shellcode):
    NB = False
    for i in range(0, len(shellcode), 2):
        if shellcode[i:i+2] == "00":
            NB = True
            print("NullBytes here : " + shellcode[i:i+2])
    if NB == False:
        print("No NullBytes.")