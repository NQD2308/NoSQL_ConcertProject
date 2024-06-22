from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://cuong:Aa123456789@city.h5n38kc.mongodb.net/?retryWrites=true&w=majority&appName=City"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

def signin(user,password):
    db = client['ManageAsset']
    concert_collection = db['User']
    result = concert_collection.find_one({"name": user, "password": password})
    print(result)
    if result is not None:
        print("Đăng nhập thanh cong")
    else:
        print("Đăng nhập khong thanh cong")

def signup(user,password):
    db = client['ManageAsset']
    concert_collection = db['User']
    result = concert_collection.insert_one({"name": user, "password": password,"ticket":[]})
    print(True)
def getconcert (id):
    db = client['ManageAsset']
    concert_collection = db['Concert']
    result = concert_collection.find({"id":id})
    return result
def dashboard():
    print("1: Đăng nhập")
    print("2: Đăng ký")
    option = int(input("Vui lý nhap vao lua chon cua ban: "))
    match option:
        case 1:
            print("Đăng Nhập")
            username = input("username: ")
            password = input("password: ")
            signin(username,password)

        case 2:
            print("Đăng ký")
            username = input("username: ")
            password = input("password: ")
            signup(username,password)
    

def main():
    print("1: Đăng nhập")
    print("2: Đăng ký")
    option = int(input("Vui lý nhap vao lua chon cua ban: "))
    match option:
        case 1:
            print("Đăng Nhập")
            username = input("username: ")
            password = input("password: ")
            signin(username,password)

        case 2:
            print("Đăng ký")
            username = input("username: ")
            password = input("password: ")
            signup(username,password)
    
if __name__ == '__main__':
    main()