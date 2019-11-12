import json
from difflib import get_close_matches

data = json.load(open("data.json", "r")) #o r de leitura é default então não é preciso colcar

"""Função que recebe uma palavra e busca no dicionário data a definição da mesma"""
def lerPalavra(palavra):
	s = palavra.lower()
	if s in data:
		return data[s]
	elif len(get_close_matches(palavra, data.keys(), n=1,cutoff = 0.8)) > 0:
		teste = input("Você quiz dizer %s? Se for digite s caso contrário digite n." % get_close_matches(palavra, data.keys(), n=1,cutoff = 0.8)[0])
		if teste == "s":
			return data[get_close_matches(palavra, data.keys(), n=1,cutoff = 0.8)[0]]
		elif teste == "n":
			return "Desculpas não sabemos qual palavra desejo."
		else:
			return "Desculpas não entendemos o comando."
	else:
		return "Essa palavra não existe, por favor confirme."

palavra = input("Digite uma palavra :")

resultado = lerPalavra(palavra)

if type(resultado) == list:
	for significado in resultado:
		print (significado)
else:
	print(resultado)
