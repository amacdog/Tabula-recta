# para a conversão é preciso fazer as letras do texto para numeros senod o A = 0

def conv(a):
    codigo =[]
    for e in a :
        if e == "a":
            codigo.append(0)
        elif e == "b":
            codigo.append(1)
        elif e == "c":
            codigo.append(2)
        elif e == "d":
            codigo.append(3)
        elif e == "e":
            codigo.append(4)
        elif e == "f":
            codigo.append(5)
        elif e == "g":
            codigo.append(6)
        elif e == "h":
           codigo.append(7)
        elif e == "i":
            codigo.append(8)
        elif e == "j":
            codigo.append(9)
        elif e == "k":
            codigo.append(10)
        elif e == "l":
            codigo.append(11)
        elif e == "m":
            codigo.append(12)
        elif e == "n":
            codigo.append(13)
        elif e == "o":
            codigo.append(14)
        elif e == "p":
            codigo.append(15)
        elif e == "q":
            codigo.append(16)
        elif e == "r":
            codigo.append(17)
        elif e == "s":
            codigo.append(18)
        elif e == "t":
            codigo.append(19)
        elif e == "u":
            codigo.append(20)
        elif e == "v":
            codigo.append(21)
        elif e == "w":
            codigo.append(22)
        elif e == "x":
            codigo.append(23)
        elif e == "y":
            codigo.append(24)
        elif e == "z":
            codigo.append(25)
    return codigo
        
# Calculo da cripto grafia: mensagem + chave = letra criptografada
# a = msg b = chave
def criptografia(a,b):
    x =0
    r = []
    for i in a :
        l = i + b[x]
        if x == (len(b)-1) :
            x=0    
        else:
            x+=1 
        r.append(l)
        
    return (r)
#de numero para letra
def transcricao(a):
    c = 0
    for g in a:
        if g > 26 :
            a[c] = g - 26
        c+=1    
    trans =[]
    for e in a :
        if e == 0:
            trans.append("a")
        elif e == 1:
            trans.append("b")
        elif e == 2:
            trans.append("c")
        elif e == 3:
            trans.append("d")
        elif e == 4:
            trans.append("e")
        elif e == 5:
            trans.append("f")
        elif e == 6:
            trans.append("g")
        elif e == 7:
           trans.append("h")
        elif e == 8:
            trans.append("i")
        elif e == 9:
            trans.append("j")
        elif e == 10:
            trans.append("k")
        elif e == 11:
            trans.append("l")
        elif e == 12:
            trans.append("m")
        elif e == 13:
            trans.append("n")
        elif e == 14:
            trans.append("o")
        elif e == 15:
            trans.append("p")
        elif e == 16:
            trans.append("q")
        elif e == 17:
            trans.append("r")
        elif e == 18:
            trans.append("s")
        elif e == 19:
            trans.append("t")
        elif e == 20:
            trans.append("u")
        elif e == 21:
            trans.append("v")
        elif e == 22:
            trans.append("w")
        elif e == 23:
            trans.append("x")
        elif e == 24:
            trans.append("y")
        elif e == 25:
            trans.append("z")
    tex = ''.join(trans)
    return tex


def verif (a): 
    for k in a:
        if k ==" " or k==int :
            m = print("ERRO: Nao e aceito espacos nem numeros na chave ou no texto, tente novamente. ")
            return m 
            
    
def descriptografia(a,b):
    x =0
    r = []
    for i in a :
        l =  i - b[x]
        if x == (len(b)+1) :
            x=0    
        else:
            x+=1 
        r.append(l)
        
    return (r)