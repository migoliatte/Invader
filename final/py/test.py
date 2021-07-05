import socket
import random


def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

# print(search_string_in_file("asm/fnl_reverse_shell_copy.asm","xor"))


def check():
    with open('asm/fnl_reverse_shell_copy.asm') as f:
        datafile = f.readlines()

    with open("asm/test.asm", "w") as file:
        for line in datafile:
            test = line.split()
            if "xor" in line:
                # found = True # Not necessary
                # return True
                if(test[1][:-1] == test[2]):
                    if(random.randint(0, 1)):
                        file.write("and " + test[2] + ", " + str("0x01010101") +
                                   "\nand " + test[2] + ", " + str("0x02020202")+"\n")
                    else:
                        file.write("sub " + test[2] + ", " + test[2]+"\n")
                else:
                    file.write("xor " + test[1][:-1] + ", " + test[2]+"\n")
            elif "mov" in line:
                if(test[1][:-1] in set(["al", "bl", "cl", "dl", "ax", "eax", "edx", "ecx", "ebx", "esp", "ebp", "esp"])):
                    if(test[2] not in set(["al", "bl", "cl", "dl","ax" "eax", "edx", "ecx", "ebx", "esp", "ebp", "esp"]) and test[2][0:2] == "0x"):
                        if(not ((len(test[2]) == 10 and test[2] == "0xffffffff") or (len(test[2]) == 6 and test[2] == "0xffff") or (len(test[2]) == 4 and test[2] == "0xff"))):
                            value = hex(int(test[2], 16)+1)
                            if(len(value) == 3):
                                value = "0x0"+value[2]
                            print(value[0:len(value)])
                            file.write("mov "+ test[1][:-1] + ", "+value+"\n dec "+ test[1][:-1]+"\n")
                        #else: #il faut rajouter un test pour savoir si ça a été fait ou aps
                        #    print(line)
                        #    value = hex(int(test[2], 16)-1)
                        #    if(len(value) == 3):
                        #        value = "0x0"+value[2]
                        #    print(value[0:len(value)])
                        #    file.write("mov "+ test[1][:-1] + ", "+value+"\n inc "+ test[1][:-1]+"\n")
#return "mov " + val1 + #", 2\ndec " + val1
#if num == 2:
#return "mov " + val1 + ", 1h\ninc " + val1
                    else:
                        file.write("mov " + test[1][:-1] + ", " + test[2]+"\n")

            else:
                file.write(line)


check()
# input file
#fin = open("asm/fnl_reverse_shell_copy.asm", "rt")
# data=fin.readlines()
# for i in data:
#    if(i.find("   xor")==0):
#        print("OUI")
#    print(i)
#
# close input and output files
# fin.close()
