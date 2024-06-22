from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://cuong:Aa123456789@city.h5n38kc.mongodb.net/?retryWrites=true&w=majority&appName=City"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


def main():
    print("1: Đăng nhập")
    print("2: Đăng ký")
    option = int(input("Vui lý nhap vao lua chon cua ban: "))
    match option:
        case 1:
            print("Đăng Nhập")
            username = input("username: ")

        case 2:
            print("Đăng ký")
    
if __name__ == '__main__':
    main()