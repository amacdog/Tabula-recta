import Conversao

print('Tabula Recta:')

key = input("Insira a chave:\n")
key =key.lower()
list(key)
Conversao.verif(key)
key =Conversao.conv(key)


while True :
    select = input("Deseja criptar ou descriptar a mensagem?\n")
    if select == "criptar":
        texto = input("Insira a mensagem para criptar:\n")
        list(texto)
        texto = texto.lower()
        Conversao.verif(texto)
        S = True
        break    
    elif select == "descriptar": 
        texto = input("Insira a mensagem criptografada:\n")
        list(texto)
        texto = texto.lower()
        Conversao.verif(texto)
        S= False
        break    
    else :
        print('Resposta negada, escreva "criptar" ou "descriptar" para selecionar.')

texto = Conversao.conv(texto)

if S == True:
    p =Conversao.criptografia(texto,key)
    print("Mensagem criptografada com sucesso!")
    print(Conversao.transcricao(p))
else :
    d = Conversao.descriptografia(texto,key)
    print("Mensagem descriptografada com sucesso!")
    print(Conversao.transcricao(d))