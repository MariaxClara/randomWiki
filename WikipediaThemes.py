import requests 

def Encontrar_Na_Pagina(n, word):
    aux = 0
    titulos = []
    
    while aux != n:
        site = requests.get('https://en.wikipedia.org/wiki/Special:Random')
        pagina = (site.content).decode("UTF8")
        linkSite = (site.url)
        tituloDesformatado = linkSite.replace("https://en.wikipedia.org/wiki/", "")
        titulo = tituloDesformatado.replace("_", " ")
        if (word in pagina.lower()):
            titulos.append(f"{titulo}\n")
        aux+= 1
        
    arquivo = open(f"{word}{n}.txt", "a")        
    arquivo.writelines(titulos)

n = int(input())
word = input()
Encontrar_Na_Pagina(n, word)













