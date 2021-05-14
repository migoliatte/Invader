main:
    xor eax,eax
    xor ebx,ebx
    xor edx,edx
    mov al, 4
    mov bl, 4
    add eax, ebx
    add eax, 0x30
    push eax
    mov al, 4
    mov bl, 1
    mov ecx, esp
    mov dl, 1
    int 80h
    mov al, 1
    xor ebx, ebx
    int 80h