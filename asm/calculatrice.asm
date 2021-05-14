mov eax, 4
mov ebx, 4
add eax, ebx
add eax, 0x30
push eax
mov eax, 4
mov ebx, 1
mov ecx, esp
mov edx, 1
int 80h
mov eax, 1
xor ebx, ebx
int 80h