import urllib.request
import urllib.parse
import re

url = 'https://pokemondb.net/pokedex/all'

values = {'s' : 'basics',
          'submit' : 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
respData = resp.read()
list_item = re.findall(r'<a class="ent-name"[^>]*>(.+?)</a>',str(respData))
name = list_item

lista = [a for a in name]
lista1 = []
j =1

for i in range(len(lista)-1):
    if lista[i] != lista[i+1]:
        lista1.append(str(j)+";"+lista[i]+"\n")
        j+=1
lista1.append(str(j)+";"+lista[i])

data = "".join(lista1)

listaPokemon = open("Lista de Pokemon.csv", "w",encoding='utf-8')
listaPokemon.write("Lista de Pokemon:\n" + "Numero;Nome\n" + data)
listaPokemon.close()

