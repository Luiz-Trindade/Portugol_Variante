from sys import argv, stdout

#Definição do texto de versão
version_text = """
    Interpretador de uma variante personalizada de PORTUGOL
    ------------------------------------------------------------
    portugol 1.0 Copyright (C) 2024  Luiz Gabriel Magalhães Trindade
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions; type: "https://www.gnu.org/licenses/gpl-3.0.en.html#license-text" 
    in an browser the for details.
"""

#Definição de variáveis do interpretador
program_name        = str("")
program_content     = []
program_variables   = {}
program_length      = int(0)
counter             = int(0)

#Função que exibe uma mensagem de erro e encerra
def Die(msg):
    print(msg)
    exit()

#Função que lê o código e armazena 
#para ser interpretado posteriormente
def ReadCode():
    global program_name, program_content, program_length
    try:
        program_name = str(argv[1])
        if program_name == "-v":
            print(version_text)
            exit()
    except IndexError:
        Die("Defina o programa!")

    with open(program_name, "r") as file:
        content = file.readlines()
        program_content = [code.strip() for code in content]
        program_length = int(len(program_content))-1
        program_name = program_name.replace(".por", "")

#Função para interpretar o código
def InterpretCode():
    global program_name, program_length, counter
    
    #Funções Principais
    def Escreva(*args):
        cleaned_args = [str(arg).strip('"') for arg in args]
        stdout.write(" ".join(cleaned_args) + " ")

    #Implementação da interpretação do cabeçalho do programa
    while program_content[counter] != "inicio":
        tokens = program_content[counter].split(" ")

        #Verifica se o nome do algorítimo é o mesmo do nome do programa
        if tokens[0] == "algoritmo":
            if len(tokens) >= 2 and str(tokens[1]) == program_name:
                pass
            else:
                Die("Nome do algoritmo não corresponde ao nome do programa!")

        #Declaração das variáveis de texto
        elif tokens[0] == "texto:":
            text_variables = tokens[1:]
            for name in text_variables:
                program_variables[name] = ""
            pass

        #Declaração da variáevis numéricas
        elif tokens[0] == "numero:":
            text_variables = tokens[1:]
            for name in text_variables:
                program_variables[name] = float(0)
            pass

        #Verifica o início do programa para parar de interpretar o cabeçalho
        #e iniciar a interpretar o programa em si
        elif tokens[0] == "inicio":
            break

        counter += 1

    #Trecho onde a interpretação ocorre de fato
    while counter <= program_length:
        tokens   = program_content[counter].split(" ")
        function = tokens[0].lower()

        #Chamada da função "escreva"
        if function == "escreva":
            content_to_write = tokens[1:]
            for i in content_to_write:
                if i in program_variables:
                    Escreva(*program_variables[i])
                else:
                    Escreva(i)
            print("")

        #Atribuição de valor às variáveis
        elif function in program_variables:
            var_name = function
            operator = tokens[1]
            if operator == "<-":
                var_content = tokens[2:]
                try:
                    program_variables[var_name] = float(var_content)
                except: program_variables[var_name] = var_content

        #Interpretação do fim do programa
        elif program_length == counter:
            if function == "fim":
                exit()
            else: 
                while True: pass

        else: pass

        counter += 1


#Função para limpar/resetar os dados antes de fechar o interpretador
def CleanMemoryBeforeExit():
    global program_name, program_content, program_length, program_variables, counter
    program_name = ""
    program_content = []
    program_variables = {}
    program_length = 0
    counter = 0

#Função principal
def Main():
    ReadCode()
    InterpretCode()
    CleanMemoryBeforeExit()

if __name__ == "__main__":
    Main()
