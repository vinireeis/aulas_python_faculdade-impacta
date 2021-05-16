class Pessoa:
    #contrutor
    def __init__(self, nome, email, telefone):
        #atributos
        self.nome = nome
        self.email = email
        self.telefone = telefone

#testando objetos
pessoa1 = Pessoa("Vinicius", "vih-reis@hotmail.com", "11952945737")

print ("Nome:", pessoa1.nome)
print ("email:", pessoa1.email)
print ("Telefone:", pessoa1.telefone)