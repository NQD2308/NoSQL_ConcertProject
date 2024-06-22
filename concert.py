from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from pprint import pprint

# Get the current datetime


uri = "mongodb+srv://cuong:Aa123456789@city.h5n38kc.mongodb.net/?retryWrites=true&w=majority&appName=City"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
def signin(user,password):
    db = client['ManageAsset']
    concert_collection = db['User']
    user = concert_collection.find_one({"name": user, "password": password})
    if user is not None:
        print("Đăng nhập thanh cong")
        
        dashboard(user)
    else:
        print("Đăng nhập khong thanh cong")

def signup(user,password):
    db = client['ManageAsset']
    concert_collection = db['User']
    now = datetime.now()
    id_str = now.strftime("%Y%m%d%H%M%S")
    result = concert_collection.insert_one({"id":id_str,"name": user, "password": password,"ticket":[]})
    print(True)

def getconcert (id):
    db = client['ManageAsset']
    concert_collection = db['Concert']
    result = concert_collection.find_one({"id":id})
    return result

def getRecommentByLocation(location):
    db = client['ManageAsset']
    concert_collection = db['Concert']
    results = concert_collection.find({"location": location})
    for concert in results:
        pprint(concert)
    return results

def comment(id_user ,id):
    db = client['ManageAsset']
    concert_collection = db['Concert']
    concert = concert_collection.find_one({"id":id})
    if concert is not None:
        print(concert["forum"])
        print("_________________________________-")

        comment = input("your comment: ")
        new_forum_entry = {"_id": id_user, "content": comment}
        concert_collection.update_one(
                {"id": id},  # The filter to find the document
                {"$push": {"forum": new_forum_entry}}  # The update to push the new entry to the Forum array
            )
    else :
        print("Khong tim thay")
def dashboard(user):
    while True:
        print("1: Mua vé")
        print("2: Xem vé đã mua")
        print("3: Đề xuất concert")
        print("4: Bình luận về concert")
        
        option = int(input("Vui lý nhap vao lua chon cua ban: "))
        match option:
            case 1:
                print("Mua Vé")
                id = input("Nhap id concert: ")
                print("Recomemt concert")
                concert = getconcert(id)
                if concert:
                    location = concert.get("location")
                    print(f"Các concert tại {location}:")
                    getRecommentByLocation(location)
                else:
                    print("Không tìm thấy concert")
                
            case 2:
                print("Xem vé đã mua")
                if len(user["ticket"]) == 0:
                    print("__________________________________________________")
                    print("Chua co ve")
                    print("__________________________________________________")
                else :
                    print("__________________________________________________")
                    print(user["ticket"])
                    print("__________________________________________________")

            case 3:
                print("Đề xuất concert theo địa điểm")
                id = input("Nhập id concert: ")
                concert = getconcert(id)
                if concert:
                    location = concert.get("location")
                    print(f"Các concert tại {location}:")
                    getRecommentByLocation(location)
                else:
                    print("Không tìm thấy concert")

            case 4:
                print("Nhap concert muốn comment")
                id = input("id concert: ")
                
                comment(user["_id"],id)

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
    while True:
        main()