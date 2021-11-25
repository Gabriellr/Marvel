import time
import requests
import hashlib
import json
import pandas as pd

particular="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
publica="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


m = hashlib.md5()
ts = str(time.time())




m.update(bytes(ts, 'utf-8'))
m.update(bytes(particular,'utf-8'))
m.update(bytes(publica,'utf8'))
hasht  = m.hexdigest()

 
base ="https://gateway.marvel.com"
personagem = "Iron Man"
requisicao = "/v1/public/characters?name=" + personagem + "&orderBy=name&limit=100"


URL1 = "https://gateway.marvel.com/v1/public/characters?name=" + personagem + "/1009368/stories?ts=thesoer&apikey=001ac6c73378bbfff488a36141458af2&hash=72e5ed53d1398abb831c3ceec263f18b"

URL = base + requisicao + "&ts=" + ts + "&apikey=" + publica + "&hash=" + hasht

dados = requests.get(URL).json()

descricao = dados

df = pd.read_json(descricao, orient ='index')

df.to_csv('heroes.csv', index=False, sep=';')
