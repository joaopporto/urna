from string import whitespace
from tkinter import image_names
from graphics import *

arq = open("urna.csv","r")
dados = arq.read()
lista = dados.split("\n")
lista = lista[:-1]
print(lista)
for ind in range(len(lista)):
    lista[ind] = lista[ind].split(";")

win = GraphWin("Urna", 950, 580)

def Urna():
    tela = Image(Point(315, 295), "Img urna/tela.png")
    tela.draw(win)
    topo = Image(Point(765, 121), "Img urna/topo.png")
    topo.draw(win)
    faixadir = Image(Point(929, 282), "Img urna/faixaDir.png")
    faixadir.draw(win)
    abaixotec = Image(Point(790, 558), "Img urna/abaixoTec.png")
    abaixotec.draw(win)
    ladodirtec = Image(Point(883, 360), "Img urna/ladoDirTec.png")
    ladodirtec.draw(win)
    ladoesqtec = Image(Point(649, 365), "Img urna/ladoEsqTec.png")
    ladoesqtec.draw(win)
    ptabaixo = Image(Point(699, 453), "Img urna/ptabaixo7.png")
    ptabaixo.draw(win)
    ptabaixo1 = Image(Point(838, 448), "Img urna/ptabaixo9.png")
    ptabaixo1.draw(win)

    n1 = Image(Point(699, 281), "Img urna/n1.png")
    n1.draw(win)
    n4 = Image(Point(699, 340), "Img urna/n4.png")
    n4.draw(win)
    n7 = Image(Point(699, 399), "Img urna/n7.png")
    n7.draw(win)
    n2 = Image(Point(770, 281), "Img urna/n2.png")
    n2.draw(win)
    n5 = Image(Point(770, 340), "Img urna/n5.png")
    n5.draw(win)
    n8 = Image(Point(770, 399), "Img urna/n8.png")
    n8.draw(win)
    n3 = Image(Point(838, 281), "Img urna/n3.png")
    n3.draw(win)
    n6 = Image(Point(838, 340), "Img urna/n6.png")
    n6.draw(win)
    n9 = Image(Point(838, 399), "Img urna/n9.png")
    n9.draw(win)
    n0 = Image(Point(775, 453), "Img urna/n0.png")
    n0.draw(win)
    confirma = Image(Point(855, 503), "Img urna/confirma.png")
    confirma.draw(win)
    branco = Image(Point(681, 508), "Img urna/branco.png")
    branco.draw(win)
    corrige = Image(Point(770, 508), "Img urna/corrige.png")
    corrige.draw(win)

def botao(position):
    x = position.getX()
    y = position.getY()
    if x >= 680 and x <= 725 and y >= 262 and y <= 293:
        return "1"
    elif x >= 748 and x <= 796 and y >= 260 and y <= 293:
        return "2"
    elif x >= 817 and x <= 864 and y >= 259 and y <= 293:
        return "3"
    elif x >= 680 and x <= 726 and y >= 318 and y <= 354:
        return "4"
    elif x >= 748 and x <= 794 and y >= 319 and y <= 354:
        return "5"
    elif x >= 816 and x <= 863 and y >= 319 and y <= 353:
        return "6"
    elif x >= 680 and x <= 726 and y >= 384 and y <= 416:
        return "7"
    elif x >= 749 and x <= 795 and y >= 381 and y <= 414:
        return "8"
    elif x >= 818 and x <= 861 and y >= 382 and y <= 413:
        return "9"
    elif x >= 747 and x <= 794 and y >= 436 and y <= 472:
        return "0"
    elif x >= 646 and x <= 714 and y >= 491 and y <= 527:
        return "BRANCO"
    elif x >= 735 and x <= 804 and y >= 494 and y <= 524:
        return "CORRIGE"
    elif x >= 820 and x <= 886 and y >= 481 and y <= 524:
        return "CONFIRMA"

        


def governadorNum():
    GovernadorText = Text(Point(250,260), 'Governador')
    GovernadorText.setSize(18)
    GovernadorText.draw(win)
    quadroNum1 = Rectangle(Point(123.0, 308.0), Point(160.0, 343.0))
    quadroNum1.draw(win)
    quadroNum2 = Rectangle(Point(163.0, 308.0), Point(200.0, 343.0))
    quadroNum2.draw(win)
    branco = Text(Point(320,340), 'VOTO EM BRANCO')
    #branco.draw(win)
    branco.setSize(26)
    aperte = Text(Point(100,470), 'Aperte a tecla: ')
    #aperte.draw(win)
    aperte.setSize(11)
    confirma_voto = Text(Point(200,488), 'CONFIRMA para CONFIRMAR este voto')
    #confirma_voto.draw(win)
    confirma_voto.setSize(11)
    corrige_voto = Text(Point(200,505), 'CORRIGE para REINICIAR este voto')
    #corrige_voto.draw(win)
    corrige_voto.setSize(11)
    linha = Line(Point(42,455), Point(592, 455))
    #linha.draw(win)
    Seuvoto = Text(Point(120, 220), 'SEU VOTO PARA')
    Seuvoto.setSize(12)
    #Seuvoto.draw(win)
    numero = Text(Point(78, 323), 'Número: ')
    #numero.draw(win)
    numero.setSize(11)
    numero_errado = Text(Point(142, 359), 'NÚMERO ERRADO ')
    #numero_errado.draw(win)
    numero_errado.setSize(16)
    nome = Text(Point(71, 373), 'Nome: ')
    #nome.draw(win)
    nome.setSize(11)
    nulo = Text(Point(350,402), 'VOTO NULO')
    #nulo.draw(win)
    nulo.setSize(26)
    partido = Text(Point(75, 423), 'Partido: ')
    #partido.draw(win)
    partido.setSize(11)
    


    cont=0
    num_partido = ''
    i = 1

    while cont <= 2:
        position = win.getMouse()
        tecla = botao(position)
        while tecla != '1' and tecla != '2' and tecla != '3' and tecla != '4' and tecla != '5' and tecla != '6' and tecla != '7' and tecla != '8' and tecla != '9' and tecla != '0' and tecla != 'CORRIGE' and tecla != 'CONFIRMA' and tecla != 'BRANCO':
            position = win.getMouse()
            tecla = botao(position)
        if cont == 0:
            GovText1 = Text(Point(141,325), ' ')
            GovText1.draw(win)
            GovText1.setSize(18)
            GovText1.setText(tecla)
        num_partido = num_partido + tecla
        if cont == 1:
            GovText2 = Text(Point(182,325), ' ')
            GovText2.draw(win)
            GovText2.setSize(18)
            GovText2.setText(tecla)
            while i < len(lista):
                print(i)
                lista1 = lista[i]
                if num_partido not in lista1:
                    i = i + 1
                else:
                    nome = Text(Point(85, 373), 'Nome: ' + lista1[1])
                    nome.draw(win)
                    nome.setSize(11)
                    partido = Text(Point(85, 423), 'Partido: ' + lista1[3])
                    partido.draw(win)
                    partido.setSize(11)
                    Seuvoto.draw(win)
                    linha.draw(win)
                    aperte.draw(win)
                    confirma_voto.draw(win)
                    corrige_voto.draw(win)
                    numero.draw(win)
                    break
            if i == len(lista) and num_partido not in lista:
                nulo.draw(win)
                numero_errado.draw(win)
                Seuvoto.draw(win)
                linha.draw(win)
                aperte.draw(win)
                confirma_voto.draw(win)
                corrige_voto.draw(win)
                numero.draw(win)
        if tecla == 'CONFIRMA':
            GovText1.undraw()
            GovText2.undraw()
            GovernadorText.undraw()
            nulo.undraw()
            numero_errado.undraw()
            Seuvoto.undraw()
            linha.undraw()
            aperte.undraw()
            confirma_voto.undraw()
            corrige_voto.undraw()
            numero.undraw()
            nome.undraw()
            partido.undraw()
            presidenteNum()
            break
        if tecla == 'CORRIGE':
            GovText1.undraw()
            GovText2.undraw()
            GovernadorText.undraw()
            nulo.undraw()
            numero_errado.undraw()
            Seuvoto.undraw()
            linha.undraw()
            aperte.undraw()
            confirma_voto.undraw()
            corrige_voto.undraw()
            numero.undraw()
            nome.undraw()
            partido.undraw()
            governadorNum()
            break
        cont = cont + 1
        

def presidenteNum():
    PresidenteText = Text(Point(250,260), 'Presidente')
    PresidenteText.setSize(18)
    PresidenteText.draw(win)
    quadroNum1 = Rectangle(Point(123.0, 308.0), Point(160.0, 343.0))
    quadroNum1.draw(win)
    quadroNum2 = Rectangle(Point(163.0, 308.0), Point(200.0, 343.0))
    quadroNum2.draw(win)
    branco = Text(Point(320,340), 'VOTO EM BRANCO')
    #branco.draw(win)
    branco.setSize(26)
    aperte = Text(Point(100,470), 'Aperte a tecla: ')
    #aperte.draw(win)
    aperte.setSize(11)
    confirma_voto = Text(Point(200,488), 'CONFIRMA para CONFIRMAR este voto')
    #confirma_voto.draw(win)
    confirma_voto.setSize(11)
    corrige_voto = Text(Point(200,505), 'CORRIGE para REINICIAR este voto')
    #corrige_voto.draw(win)
    corrige_voto.setSize(11)
    linha = Line(Point(42,455), Point(592, 455))
    #linha.draw(win)
    Seuvoto = Text(Point(120, 220), 'SEU VOTO PARA')
    Seuvoto.setSize(12)
    #Seuvoto.draw(win)
    numero = Text(Point(78, 323), 'Número: ')
    #numero.draw(win)
    numero.setSize(11)
    numero_errado = Text(Point(142, 359), 'NÚMERO ERRADO ')
    #numero_errado.draw(win)
    numero_errado.setSize(16)
    nome = Text(Point(71, 373), 'Nome: ')
    #nome.draw(win)
    nome.setSize(11)
    nulo = Text(Point(350,402), 'VOTO NULO')
    #nulo.draw(win)
    nulo.setSize(26)
    partido = Text(Point(75, 423), 'Partido: ')
    #partido.draw(win)
    partido.setSize(11)
    bolsonaro = Image(Point(541, 284), "Img Urna/FgYX3pJXkAISa95.png")
    #bolsonaro.draw(win)
    


    cont=0
    num_partido = ''
    i = 1

    while cont <= 2:
        position = win.getMouse()
        tecla = botao(position)
        while tecla != '1' and tecla != '2' and tecla != '3' and tecla != '4' and tecla != '5' and tecla != '6' and tecla != '7' and tecla != '8' and tecla != '9' and tecla != '0' and tecla != 'CORRIGE' and tecla != 'CONFIRMA' and tecla != 'BRANCO':
            position = win.getMouse()
            tecla = botao(position)
        if cont == 0:
            PreText1 = Text(Point(141,325), ' ')
            PreText1.draw(win)
            PreText1.setSize(18)
            PreText1.setText(tecla)
        num_partido = num_partido + tecla
        if cont == 1:
            PreText2 = Text(Point(182,325), ' ')
            PreText2.draw(win)
            PreText2.setSize(18)
            PreText2.setText(tecla)
            while i <= len(lista):
                print(i)
                lista1 = lista[i]
                if num_partido not in lista1:
                    i = i + 1
                else:
                    nome = Text(Point(85, 373), 'Nome: ' + lista1[1])
                    nome.draw(win)
                    nome.setSize(11)
                    partido = Text(Point(85, 423), 'Partido: ' + lista1[3])
                    partido.draw(win)
                    partido.setSize(11)
                    Seuvoto.draw(win)
                    linha.draw(win)
                    aperte.draw(win)
                    confirma_voto.draw(win)
                    corrige_voto.draw(win)
                    numero.draw(win)
                    break
            if i == len(lista) and num_partido not in lista:
                nulo.draw(win)
                numero_errado.draw(win)
                Seuvoto.draw(win)
                linha.draw(win)
                aperte.draw(win)
                confirma_voto.draw(win)
                corrige_voto.draw(win)
                numero.draw(win)
        if tecla == 'CONFIRMA':
            PreText1.undraw()
            PreText2.undraw()
            PresidenteText.undraw()
            presidenteNum()
            break
        if tecla == 'CORRIGE':
            PreText1.undraw()
            PreText2.undraw()
            PresidenteText.undraw()
            nulo.undraw()
            numero_errado.undraw()
            Seuvoto.undraw()
            linha.undraw()
            aperte.undraw()
            confirma_voto.undraw()
            corrige_voto.undraw()
            numero.undraw()
            nome.undraw()
            partido.undraw()
            presidenteNum()
            break
        cont = cont + 1
    
   

Urna()
governadorNum()



position = win.getMouse()
print(position)
