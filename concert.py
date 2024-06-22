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

def getRecommentByLocation(location):
    db.Concert.find({ location: location }).pretty();


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



    # db.Concert.insertMany([{name: "Music Night",location: "Hoa Sen University",address: "456, Q3",datetimestart: ISODate("2024-07-15T19:00:00Z"),datetimeend: ISODate("2024-07-15T22:00:00Z"),totalTicket: 2500,ticket: {basic: {price: 400,totalticket: 1200},vip: {price: 1000,totalticket: 1000},vip2: {price: 1500,totalticket: 300}}},{ name: "Sports Gala",location: "Sân Mỹ Đình",address: "789, Q5",datetimestart: ISODate("2024-08-05T18:00:00Z"),datetimeend: ISODate("2024-08-05T22:00:00Z"),totalTicket: 5000,ticket: {basic: {price: 800,totalticket: 3000},vip: {price: 1500,totalticket: 1500},vip2: {price: 2200,totalticket: 500}}},{name: "Concert Night",location: "Sân Mỹ Đình",address: "456, Q2",datetimestart: ISODate("2024-09-20T19:30:00Z"),datetimeend: ISODate("2024-09-20T23:30:00Z"),totalTicket: 6000,ticket: {basic: {price: 700,totalticket: 3500},vip: {price: 1600,totalticket: 2000},vip2: {price: 2500,totalticket: 500}}},{name: "Cultural Festival",location: "Sân Phú Thọ",address: "321, Q11",datetimestart: ISODate("2024-10-10T10:00:00Z"),datetimeend: ISODate("2024-10-10T22:00:00Z"),totalTicket: 4500,ticket: {basic: {price: 600,totalticket: 2500},vip: {price: 1300,totalticket: 1500},vip2: {price: 2000,totalticket: 500}}}]);