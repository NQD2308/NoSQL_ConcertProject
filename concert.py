from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import json_util
from datetime import datetime
import os,redis,json
r = redis.Redis(host='localhost', port=6379, db=0)
class Color:
    GREEN = '\033[92m'
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
def getRecommentByLocation(location):
    db = client['ManageAsset']
    db.Concert.find({ location: location }).pretty();

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
def generate_ticket(event_id, ticket_type, seat_number, total_ticket):
    ticket_id = f"{event_id}{ticket_type}{seat_number}"
    r.hset(ticket_id, 'event_id', event_id)
    r.hset(ticket_id, 'ticket_type', ticket_type)
    r.hset(ticket_id, 'seat_number', seat_number)
    r.hset(ticket_id, 'total_ticket', total_ticket)
    r.hset(ticket_id, 'status', 'available')
    return f"{ticket_id} was generated successfully." 

def generate_multiple_tickets(event_id, ticket_type, total_ticket):
    for i in range(1, total_ticket + 1):
        seat_number = str(i)
        print(generate_ticket(event_id, ticket_type, seat_number, total_ticket))

def sell_ticket(ticket_id):
    if r.exists(ticket_id) and r.hget(ticket_id, 'status').decode('utf-8') == 'available':
        r.hset(ticket_id, 'status', 'sold')
        return f"Ticket {ticket_id} sold successfully."
    elif r.exists(ticket_id):
        return f"Ticket {ticket_id} is already sold."
    else:
        return f"Ticket {ticket_id} does not exist."

def check_ticket(ticket_id):
    if r.exists(ticket_id):
        ticket_info = r.hgetall(ticket_id)
        status = ticket_info[b'status'].decode('utf-8')
        return f"Ticket {ticket_id} status: {status}"
    else:
        return f"Ticket {ticket_id} does not exist."

def getconcert(concert_id):
    db = client['ManageAsset']
    concert_collection = db['Concert']
    result = concert_collection.find({"id": concert_id})
    return json.loads(json_util.dumps(list(result)))
def menu_ticket():
    print("1. Generate tickets from concert")
    print("2. Sell ticket")
    print("3. Check ticket")
    print("4. Clear Screen")
    print("5. Exit")
def output_ticket():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Color.GREEN)
    menu_ticket()
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == 1:
            concert_id = input("Enter concert ID: ")
            res = getconcert(concert_id)
            if res:
                concert = res[0]
                event_id = concert['id']
                tickets = concert.get('ticket', {})
                for ticket_type, ticket_info in tickets.items():
                    total_ticket = ticket_info.get('totalticket', ticket_info.get('titalticket'))
                    print(f"Generating tickets for {ticket_type}...")
                    generate_multiple_tickets(event_id, ticket_type, total_ticket)
            else:
                print(f"No concert found with ID: {concert_id}")
        elif choice == 2:
            ticket_id = input("Enter ticket ID: ")
            print(sell_ticket(ticket_id))
        elif choice == 3:
            ticket_id = input("Enter ticket ID: ")
            print(check_ticket(ticket_id))
        elif choice == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_ticket()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")
def dashboard(user):
    while True:
        print("1: Quản lý vé")
        print("2: Đề xuất concert")
        print("3: Bình luận về concert")
        
        option = int(input("Vui lý nhap vao lua chon cua ban: "))
        match option:
            case 1:
                output_ticket()
            case 2:
                print("Đăng Nhập")
                username = input("username: ")
                password = input("password: ")
                signin(username,password)

            case 3:
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