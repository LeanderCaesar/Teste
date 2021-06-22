#Título         :  Sistema de análise Git
#Descrição      :  Sistema destinado a análise de rastreio de informações Git de projetos do GitHub
#Autor          :  Leandro César da Cruz
#E-mail         :  leandrocesardacruz@gmail.com
#Nick           :  LeanderCaesar
#Criação        :  05/2021
#Atualização    :  06/2021
#Versão         :  0.0.1
#Uso            :  00_Menu.py (Principal)
#Nota 1         :  Usar a versão 3 do Python (3.x.x)
#Instalações    :  PyDriller; Colorama
#Versão Python  :  3.x.x (3.9.5)
#Licença        :  Uso livre
#============================================================================

import sys, os, signal, colorama, git
from pydriller import Repository
from pathlib import Path

colorama.init()

# =======================
#    DEFINIÇÕES
# =======================

print("\x1b[2J\x1b[1;1H")
pass

cores = {
  "informacao":     "35m",       # Informação (Laranja)
  "erro":    "31m",              # Mensagem de erro (Vermelha)
  "ok":       "32m",             # Mensagem de sucesso (Verde)
  "menu_principal":  "\033[31m", # Menu (vermelho)
  "fechar":  "\033[0m" 
  }

cor_1 = "\033[0m"
cor_2 = "\033[101m"
cor_3 = "\033[41m"
cor_4 = cores["menu_principal"]

# =======================
#    CONFIGURAÇÕES
# =======================

titulo_do_programa="ProjetoGit"

menu_cores = {
  "cor_2":cor_2,
  "cor_3":cor_3,
  "opc":cor_4
}
opcoes_de_menu = {
  "titulo":  "MENU DE OPÇÕES",
  "1":      "Clonar Projeto",
  "2":      "Visualizar todos os arquivos Java",
  "3":      "Visualizar todos os arquivos de teste",
  "4":      "Visualizar todos os commit",
  "5":      "Visualizar todos os commits de teste",
  "6":      "Informações de commit de arquivo específico",
  "7":      "Informação de parents de commit específico",
  "8":      "Informação dos autores",
  "9":      "Opção livre", 
  "0":      "Sair (ou CTRL+C)",
}

# =======================
#       MENSAGENS
# =======================

def corDeImpressao(cor,texto):
  print("\033["+cores[cor]+" "+texto+cor_1)

def MensagemDeErro():
  corDeImpressao("erro","erro!!")
  print("\x1b[2J\x1b[1;1H")
  
  return 1

def MensagemDeSucesso():
  impressaoColorida("Operação realizada com successo!!")
  return 0

def sair():
  sys.exit()
  
# CTRL + C
def sigint_handler(signum, frame): ################################### mudar
  print("CTRL + C (sair))")
  sys.exit(0)

# =======================
#      AÇÕES
# =======================

class visual():

  def __init__(self,opcoes,cores):
    self.largura_menu = 50
    self.opcoes = opcoes
    self.cores = cores
    self.pasta = ''

# =======================
#      DESENHO DO MENU
# =======================

  def criarLinhas(self,letra,cor,comprimento,texto):
    menu = cor+" ["+letra+"] "+texto
    linha = " "*(comprimento-len(menu))
    return  menu+linha+cor_1

  def criarMenu(self,tamanho):
    linha = self.cores["cor_2"] + " "+titulo_do_programa
    linha += " "*(tamanho-len(titulo_do_programa)-6)
    linha += cor_1
    print (linha)
    linha = self.cores["cor_3"] + " "+self.opcoes["titulo"]
    linha += " "*(tamanho-len(self.opcoes["titulo"])-6)
    linha += cor_1
    print (linha)
    for x in self.opcoes:
      if(x != "titulo"):
        print (self.criarLinhas(x,self.cores["opc"],tamanho,self.opcoes[x]))

  def printMenu(self):
    self.criarMenu(self.largura_menu)

# =======================
#      CHAMADAS
# =======================

  def acao(self,chamada): 
    if   chamada == '1':

      pasta = self.clonar_projeto()
    elif chamada == '2':
      self.visualizar_arquivos()
    elif chamada == '3':
      self.visualizar_testes()
    elif chamada == '4':
      self.visualizar_commits()
    elif chamada == '5':
      self.visualizar_commits_teste()
    elif chamada == '6':
      self.visualizar_arquivo_especifico()
    elif chamada == '7':
      self.visualizar_parents()
    elif chamada == '8':
      self.visualizar_autor()
    # elif chamada == '9':
    #   self.metodo_extra()
    elif chamada == 'x':
      self.metodo_x()
    elif (chamada==''):
      MensagemDeErro()
    elif chamada == '0':
      sys.exit()
    else:
      MensagemDeErro()

# =======================
#      MÉTODOS
# =======================

  def clonar_projeto(self):

    local = '' #Nota : local = último arquivo onde o projeto estará
    diretorio = '' #Nota : diretório = caminho pacial de onde o projeto estará

    while True:
        local = str(input("Informe o nome do novo diretório onde o projeto será salvo em 'C:\': "))
        diretorio = 'C:\\' + local

        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            break
        else:
            print("O nome do diretório passado já existe!")
            continue

    repositorio = ''  #Nota : repositório = caminho para o projeto remoto

    while True:
        repositorio = str(input("Informe a URL (GitHub) do projeto: "))

        try:
            git.Git(diretorio).clone(repositorio)
            projeto = str(diretorio + "\\" + Path(repositorio).stem) #Nota : projeto = caminho total e final de onde o projeto estará
            break
        except:
            print("A URL (GitHub) está incorreta!")
            continue

    #os para os.path.exists, mkdir

    x = int(0)

    for raiz, dirs, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            x+=1    

    print("\nSalvos ", x, " arquivos no total.")
    print("O projeto %s foi salvo em %s" % (repositorio, projeto))
    print("Seu projeto foi salvo em: ", projeto)
    self.pasta = projeto
    print("asasas" + self.pasta)
    botao = input("Pressione qualquer botao para sair")
    print("\x1b[2J\x1b[1;1H")
    

    return self.pasta
    #pass
  
  def visualizar_arquivos(self):  #      https://github.com/LeanderCaesar/Teste.git

    contador = int(0)

    projeto = self.pasta

    for raiz, dirs, arquivos in os.walk(projeto):
        for arquivo in arquivos:
            if arquivo.endswith(".java"):
                print(os.path.join(raiz, arquivo))
                contador+=1    
    print("Encontrados ", contador, " arquivos .java")

    botao = input("Pressione qualquer botao para sair")
    print("\x1b[2J\x1b[1;1H")
    pass
  
  def visualizar_testes(self):

    x = int(0)

    diretorio = self.pasta
    for folder, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.java'):
                fullpath = os.path.join(folder, file)
                with open(fullpath, 'r') as f:
                    for line in f:
                        if "@Test" in line:
                            print(fullpath)
                            x+=1
                            break
    print("Encontrados ", x, " arquivos de teste.")
    
    botao = input("Pressione qualquer botao para sair")
    print("\x1b[2J\x1b[1;1H")
    pass
  
  def visualizar_commits(self):
    for commit in Repository("C:\\Users\\Leandro César\\Documents\\Nova pasta\\junit4").traverse_commits():
        print(
            'O commit de número {} foi modificado pelo autor {}, '
            'e comitado por {} na data {}'.format(
                commit.hash,
                commit.author.name,
                commit.committer.name,
                commit.committer_date
            )
        )

    botao = input("Pressione qualquer botao para sair")
    print("\x1b[2J\x1b[1;1H")    
    
    pass
  
  def visualizar_commits_teste(self):
    
    print("Fazer.")

    botao = input("Pressione qualquer botao para sair")
    
    print("\x1b[2J\x1b[1;1H")
    
    pass
  
  def visualizar_arquivo_especifico(self):

    caminho = "C:\\Users\\Leandro César\\Documents\\Nova pasta\\junit4"
    caminho_do_arquivo = input("Cole o caminho a partir do diretório src: ") #"\\src\\test\\java\\junit\\tests\\AllTests.java"

    for commit in Repository(caminho, filepath=caminho + caminho_do_arquivo).traverse_commits():
        print(commit.hash)
    
    botao = input("Pressione qualquer botao para sair")
    
    print("\x1b[2J\x1b[1;1H")
    
    pass

  def visualizar_parents(self):

    rm = Repository("C:\\Users\\Leandro César\\Documents\\Nova pasta\\junit4")

    for commit in rm.traverse_commits():
      if len(commit.parents) == 2:
        print(list[commit.parents])
      else:
        print(list[commit.parents])

    pass
  
  def visualizar_autor(self):
    pass
  
  def metodo_extra(self):
    pass
  
  def metodo_x(self):
    pass


# =======================
#      BACKEND
# =======================

class menu(visual):
  pass

# =======================
#      PROGRAMA PRINCIPAL
# =======================

class manipulador_menu:

  def __init__ (self):
    self.menu_atual="main"
    self.m1=menu(opcoes_de_menu, menu_cores)
    self.pasta = ''

  def menuDeExecucao(self):
    if(self.menu_atual=="main"):
      self.m1.printMenu()

    escolha = input(" >> ")
    if(self.menu_atual=="main"):
      if(escolha=="9"):
        self.menu_atual="second"
      else:
        self.actuator(0,escolha)
    else:
      if(escolha=='9'):
        self.menu_atual="main"
      else:
        self.actuator(1,escolha)
    print("\n")

  def actuator(self,type,chamada):
    if type == 0:
      self.m1.acao(chamada)

if __name__ == "__main__":
  x = manipulador_menu()
  signal.signal(signal.SIGINT, sigint_handler)
  while True:
    x.menuDeExecucao()