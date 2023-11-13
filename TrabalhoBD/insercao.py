from pymongo import MongoClient

# Crie uma instância do cliente MongoDB
client = MongoClient()

# Conecte-se ao servidor MongoDB
db = client.local

# Cria a linha a ser inserida 
mydic = {"nome":"tela", "valor":1}

# Insere a linha na coleção telas
db.telas.insert_one(mydic)