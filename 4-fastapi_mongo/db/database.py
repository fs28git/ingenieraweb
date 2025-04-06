from pymongo import MongoClient

class Database:
    def __init__(self):  # 👈 OJO: init con doble guión bajo
        self.client = MongoClient(
            "mongodb+srv://admin:1234@cluster0.plvtpgk.mongodb.net/",
            tlsAllowInvalidCertificates=True
        )
        self.db = self.client["umb"]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Instancia única de la base de datos
database = Database()
