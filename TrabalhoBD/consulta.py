from pymongo import MongoClient

# Crie uma instância do cliente MongoDB
client = MongoClient()

# Conecte-se ao servidor MongoDB
db = client.local

# Cria ou recebe a coleção 
mycol = db['telas']

# Mostra o ID, o nome e o valor em cada linha de telas
for x in mycol.find({},{ "_id": 1, "nome": 1, "valor": 1 }):
    print(x)