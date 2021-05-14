#!/bin/bash
a=""
result=0
count=0
while (($result==0))
do
        a+="a"
        count=$(($count+1))
        echo $a|./$1 > /tmp/test
        result=$(echo $?)
done
clear
echo "Le script accepte jusque $count caractere avant detre en segfault !"
