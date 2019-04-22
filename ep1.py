import json
import random
def carregar_cenarios():
    with open('cenarios.json','r')as arquivo:
        texto=arquivo.read()
    cenarios=json.loads(texto)

    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def main():
    print('Correndo da DP')
    print("--------------")
    print("'Para o final do mês? Ahh suave, depois eu faço...' foi oque ele, "
          "aluno de engenharia julgou como uma boa ideia quando o professor Raul "
          "comentou sobre o EP, mas um fato raro aconteceu, o dom da procrastinação "
          "abençoou o pobre aluno...")
    print()
    print("É o dia da entrega, e como de costume o desespero bate forte, em seu trabalho "
          "não havia um print. Como uma medida desesperada resolve ir voando para o Insper "
          "tentar o impossivel: Fazer Raul adiar a entrega do trabalho!")
    print()


    cenarios, nome_cenario_atual = carregar_cenarios()
    inventario=[]
    game_over = False
    
    
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print(cenario_atual['titulo'])
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual['descricao'])

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Fim do jogo")
            game_over = True
        else:
            print("Escolha sua opção!")
            for k,v in opcoes.items():
               print()
               if k==" ":
                   print("  ")
               else:
                   print("{0}:{1}".format(k,v))
               
             
            print()   
            escolha=input("Qual será a escolha? ")
            
            if escolha in opcoes:
                
                nome_cenario_atual = escolha
                
                hitus=100
                atus=20
                if nome_cenario_atual=="lutar":
                    hitpc=100
                    atpc=5
                    print("você possui {0} hit points e {1} de ataque".format(hitus,atus))
                    print("O inimigo possui {0} hit points e {1} de ataque".format(hitpc,atpc))
                    
                    while hitpc>0:
                        hitpc-=atus
                        hitus-=atpc
                    print("Você derrotou o inimigo! Ainda possui {0} hit points".format(hitus))
                    nome_cenario_atual="lutar"
                    
                    
                    
                if nome_cenario_atual=="jogar a partida":
                    atapc2=10
                    hitpc2=50
                    print("você possui {0} hit points e {1} de ataque".format(hitus,atus))
                    print("O inimigo possui {0} hit points e {1} de ataque".format(hitpc2,atapc2))
                     
                    while hitpc2>0:
                        hitpc2-=atus
                        hitus-=atapc2
                    print("Você derrotou o inimigo! Ainda possui {0} hit points".format(hitus))
                    nome_cenario_atual="jogar a partida"
                          
                if nome_cenario_atual=="fuga":
                    a=random.randint(1,3)
                    b=int(input("Escolha um número de 1 a 3:"))
                    if b==a:
                        print("Você conseguiu pegar o pen drive")
                        nome_cenario_atual="fuga"
                    else:
                        print("O veterano descobriu e devorou a sua alma")
                        print("Fim de Jogo")
                        game_over=True
                        
                if nome_cenario_atual==" ":
                   x=random.randint(1,3)
                   y=int(input("Você chegou ao covil do silêncio desesperador,"
                           "um ser ancestral esta lhe propondo uma viagem "
                           "épica entre dimensões, mas para isso, você deve "
                           "acertar um número entre 1 e 3, é fácil vai! Digite o número:"))
                   if x==y:
                       print("Voce foi teletransportado para a terrivel Ronanodax, "
                             "la tudo é escuro e sombrio..."
                             "Depois de muito tempo explorando as áreas voce chega "
                             "a uma sala extremamente secreta dentro da dimensão super secreta "
                             "e avista o que parece ser o rei daquele mundo sombrio... "
                             "O QUEEEEE, HUMBERTOO!!!! Lá estava ele, acariciando sua besta "
                             "aterrorizante do submundo que tinha como nome Floquinho. Depois de muito "
                             "conversar sobre receitas de doce e energia eólica ele resolve "
                             "mandar voce de volta para terra.") 
                   else:
                       print ('')
                       print("Voce acabou de perder um oportunidade unica") 
                   
                   nome_cenario_atual= "nerd box"
                        
                        
                        
                        
                        
                   
    
   
                if nome_cenario_atual=="jogar":
                    
                    
                    n=random.randint(1,21)
                    print("O mestre comprou uma carta, mas é secreta. Tente ganhar, mas saiba que é difícil")
                    s=0
                    p=input("Você quer comprar uma carta?")
                    while p=="sim"and s<22:
                        
                        x=random.randint(1,13)
                        print("você comprou o {0}".format(x))
                        s+=x
                        print("voce esta com {0}".format(s))
                        if s<22:
                            
                            p=input("você quer comprar uma carta?")
                    if s>n and s<=21:
                        
                        print("Você venceu")
                    
                    else:
                        
                        hitus=55

                        print("Você Perdeu o jogo, e, junto,20 hit points!Ainda possui {0} hit points".format(hitus))
                    nome_cenario_atual= "jogar"
                       
                if nome_cenario_atual=="quizz": 
                    print("Responta todas as perguntas seguintes com apenas sim ou nao.")
                    print("____________________")


                    a=input("A Watson,inteligência artificial da IBM, já atuou na culinária?  ")
                    if a=="sim":
                        print("Você acertou, Parabéns!")
                    else:
                        print("Você errou, estude mais!")
    
    
                    b=input("Já existe uma robô, primeira inteligência artificial, a ter uma documentação de cidadania?  ")
                    if b=="sim":
                        print("Você acertou, Parabéns!")
                    else:
                        print("Você errou, estude mais!")
    
    
                    c=input("Em 1950 a Inteligência Artificial já tinha sido considerada um um campo de estudo?  ")
                    if c=="nao":
                        print("Você acertou, Parabéns!")
                    else:
                        print("Você errou, estude mais!")

                    d=input("As tecnologias que são acopladas a roupas e peças de vestuário são chamadas de wearble?  ")
                    if d=="sim":
                        print("Você acertou, Parabéns!")
                    else:
                        print("Você errou, estude mais!")
    
                    d=input("Raul tem Facebook?  ")
                    if d=="sim":
                        print("Você acertou, Parabéns!")
                    else:
                        print("Procure direito, você vai achar!")
                    nome_cenario_atual= "quizz"
                
                if nome_cenario_atual=="sala dos supercomputadores":
                   v="sala dos supercomputadores"
                   c=input("Para se teletransportar você de saber o nome da sala que deve ir. Dica:"
                            "A sala tem um computador super-herói! Digite o nome da sala:")
                   tele=True
                   while tele:
                       if v==c:
                           print("Finalmente, finalmente você chegou ao estágio final, o grande chefão o aguarda e a preocupação com a segurança do seu professor"
                               " é a única coisa que lhe importa. Você vai até o supercomputador e o vírus maligno tenta manter você distante do mesmo através"
                               " de ondas de choque, mas você tem a benção dos pendrives sagrados, nosso herói alcança o painel do computador e introduz os "
                               " pendrives para conferir o seu conteúdo, ali estava, a salvação para o professor Raul estava o tempo todo dentro dos pendrives."
                               " cada um deles carregava parte de um antivírus místico extremamente potente! Você consegue escutar o vírus com seus gritos de ódio"
                                " e dor através das caixas de som. Uma luz forte lhe ofusca e finalmente o objetivo de nossa jornada foi alcançada, la estava ele "
                                " o inconfundível professor Raul!") 
                           tele=False
                       else:
                           c=input("tente novamente:")
                 
                   nome_cenario_atual= "sala dos supercomputadores"
                      
                elif nome_cenario_atual=="elevador":
                    inventario.append("doce")
                elif nome_cenario_atual=="help desk" or  nome_cenario_atual=="sala do wii" or  nome_cenario_atual=="quadra":
                    inventario.append("pen drive")
                
                            
                 
                       
            else:
                game_over = True


if __name__ == "__main__":
    main()