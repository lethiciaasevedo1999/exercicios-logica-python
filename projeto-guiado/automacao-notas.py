dataset = {} #dicionário
nome = "" #variável global --> Todas as funções podem acessar essa variável
          #variável local --> Apenas funções específicas podem acessar a variável


#Função Main()
#Utilizada para definir qual é a função principal, vai indicar pro programa por 
#qual função começar a executar o código. 

def main():
    print("\n--- Seja bem vinda a Escola do Reprograma! ---\n")
    print("Aqui voê pode calcular a aprovação de uma aluna.\n")

    obter_dados_aluna()

def obter_dados_aluna():
    print("Insira os dados: ")
    nome = input("Nome da aluna: ")
    turma = input("Turma da aluna: ")

    notas = obter_notas()

def obter_notas():
    quantidade_notas = input("Quantidade de notas: ")
    notas =[] #Lista para receber as notas
    #É recomendado utilizar o "for" quando tivermos uma contagem pré definida.
    #Exemplo: eu sei que a minha contagem vai de 0 1 20
    for i in range(int(quantidade_notas)):
        entrada = input(f"Insira sua nota #{i + 1}: ")
        nota = float(entrada)
        notas.append(nota)
    return notas

main()