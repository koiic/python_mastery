from client import Client

class Client2(Client):
    pass

if __name__ == "__main__":
        
    client_2 = Client2("92.10.10.20", "10:AF:CB:EF:19:CF")
    client_2.connect()
    
        
