from pymongo import MongoClient

def database():
    CONNECTION_STRING = "mongodb+srv://maxguo2014:M4nimany@gladiator.fos7r.mongodb.net/?retryWrites=true&w=majority&appName=Gladiator"
    client = MongoClient(CONNECTION_STRING)

    return client["gladiator_go"]

if __name__ == "__main__":
    dbname = get_user_profiles()