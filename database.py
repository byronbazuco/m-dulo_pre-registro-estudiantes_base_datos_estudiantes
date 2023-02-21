from pymongo import MongoClient
import certifi
# MONGO_URI = 'mongodb://127.0.0.1:27017/marianas'
MONGO_URI = 'mongodb+srv://Marianas:$JEn8JZ6xLD2wA7@cluster0.qzgddgn.mongodb.net/?retryWrites=true&w=majority'
# MONGO_URI = 'mongodb+srv://marianastest:flor190522Passp@cluster0.qjqtf.mongodb.net/?retryWrites=true&w=majority'
# MONGO_URI = 'mongodb+srv://marianas:marianas@cluster0.wzt9scj.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_estudiantes_resgistrados"]
    except ConnectionError:
        print("Error de conexción con a bbd")
    return db