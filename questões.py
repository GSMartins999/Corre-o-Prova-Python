#Questão 1


def calcular_desconto(valor_compra, tipo_cliente):
    cliente = tipo_cliente.lower()
    if(cliente == ""):
        print("Você não indicou o tipo de cliente")
    elif(valor_compra >= 100 and cliente == "regular"):
        desconto = (0.10 * valor_compra)
        valor_final = valor_compra - desconto
        return valor_final
    elif(valor_compra >= 200 and cliente == "vip"):
        desconto = (0.20 * valor_compra)
        valor_final = valor_compra - desconto
        return valor_final
    else: 
        return "Você não tem direito a desconto porque sua compra é menor que 100 para regular e 200 para vip."

valor = float(input("Qual o valor da sua compra? "))
tipo = str(input(f"Qual seu tipo de cliente? "))

print(f"O valor inicial é: {valor}, para o cliente {tipo}, foi oferecido um desconto de: ", calcular_desconto(valor, tipo))



#Questão 2


def inverter_palavras(frase):
    palavras = frase.split()
    invertida = []
    for palavra in palavras:
        invertida.append(palavra[::-1])
    return ' '.join(invertida)

frase_original = "Python é uma linguagem de programação"
frase_invertida = inverter_palavras(frase_original)

print(f"A frase original foi: {frase_original}")
print(f"A frase invertida ficou: {frase_invertida}")



#Questão 3


def adicionar (estoque, codigo, nome, quantidade, preco): 
    if codigo not in estoque: 
        estoque[codigo] = {'nome': nome, 'qtd': quantidade, 'preco': preco}
    else: 
        print(f"Produto de código: {codigo} já existe no estoque")

def atualizar(estoque, codigo, quantidade):
    if codigo in estoque:
        if quantidade > 0:
            estoque[codigo]['qtd'] += quantidade
        else: 
            print(f"A quantidade é menor que 0!")
    else:
        print(f"Produto de código {codigo} não encontrado!")

def remover(estoque, codigo):
    if codigo in estoque:
        del estoque[codigo]
    else:
        print(f"Produto de código {codigo} não encontrado!")

def exibir_estoque(estoque):
    print(f"Estoque atual: ")
    for codigo, produtos in estoque.items():
        print(f"Código: {codigo}, Nome: {produtos['nome']}, Quantidade: {produtos['qtd']}, Preço: {produtos['preco']}")


estoque = {}

adicionar(estoque, "002", "Abacate", 10, 5)
remover(estoque, "002")

exibir_estoque(estoque)







#Questão 4]


class Funcionario:
    def __init__ (self, salario, nome, idade, cargo):
        self.salario = salario
        self.nome = nome.upper() 
        self.idade = idade
        self.cargo = cargo.upper()
    def aumentar_salario(self):
        salario_novo = (self.salario * 0.2) + self.salario
        print(f'novo salário : {salario_novo}') 
    def promover(self):
        if(self.cargo == "OPERARIO"):
            cargo_novo = self.cargo = "ANALISTA"
            salario_novo = (self.salario * 0.2) + self.salario
            print(f"{self.nome} seu novo cargo é: {cargo_novo}, e seu novo salário é: {salario_novo} e sua idade é: {self.idade + 1}")
        elif(self.cargo == "ANALISTA"):
            cargo_novo = self.cargo = "GERENTE"
            salario_novo = (self.salario * 0.4) + self.salario
            print(f"{self.nome} seu novo cargo é: {cargo_novo}, e seu novo salário é: {salario_novo} e sua idade é: {self.idade + 1}")
        elif(self.cargo == "GERENTE"):
            cargo_novo = self.cargo = "CHEFE"
            salario_novo = (self.salario * 0.8) + self.salario
            print(f"{self.nome} seu novo cargo é: {cargo_novo}, e seu novo salário é: {salario_novo} e sua idade é: {self.idade + 1}")
        else:
            print("Opção inválida")
    def aniversario(self):
        print(f'nova idade : {self.idade + 1}')
    

x = Funcionario(1203, "Antônio", 22, "operario")
y = Funcionario(1503, "José", 25, "gerente")
(x.promover())
(y.promover())
(y.aumentar_salario())
