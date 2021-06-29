nasm -f elf32 -o reverse_shell.o reverse_shell.nasm
ld -o reverse_shell_x86 reverse_shell.o
file reverse_shell_x86
objdump -d reverse_shell_x86 |grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'