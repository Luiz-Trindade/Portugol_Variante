from sys import argv

#Definição de variáveis do interpretador
program_name        = str("")
program_content     = []
program_variables   = {}
program_length      = int(0)
counter             = int(0)

#Função que lê o código e armazena 
#para ser interpretado posteriormente
def ReadCode():
    global program_name, program_content, program_length
    try:
        program_name = str(argv[1])
    except:
        print("Defina o programa!")
        exit()

    with open(program_name, "r") as file:
        content = file.readlines()
        program_content = [code.strip() for code in content]
        program_length = int(len(program_content))

#Função para interpretar o código
def InterpretCode():
    global program_length, counter
    
    #Funções Principais
    def Escreva(msg):
        print("".join(msg))

    while counter <= program_length:
        try:
            tokens   = program_content[counter].split(" ")
            function = tokens[0].lower()
            #print(counter)
        except: pass

        if function == "escreva":
            content_to_write = tokens[1:]
            Escreva(content_to_write)
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
