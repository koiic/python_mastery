import socket
import time

class Client:
    
    def __init__(self, client_ip, client_mac):
        self.client_ip = client_ip
        self.client_mac = client_mac
    
    def connect(self):
        print('I got here ============>>>>>>>', self.client_ip, self.client_mac)
        import pdb; pdb.set_trace
    
        router = ("localhost", 8200)
        
        connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        time.sleep(1)

        connection.connect(router)

        while True:
            
            received_message = connection.recv(1024)
            recieved_message = received_message.decode("utf-8")
            
            source_mac = received_message[0:17]
            
            destination_mac = received_message[17:34]
            
            source_ip = recieved_message[34:45]
            
            destination_ip = recieved_message[45:56]
            
            message = recieved_message[56:]
            
            print(f'\nPacket integrity:\n destination MAC address matches {self.client_mac} MAC address: {self.client_mac == destination_mac}')
            print(f'\ndestination IP address matches {self.client_ip} MAC address: {self.client_ip == destination_ip}')
            print(f'\nThe Packet recieved:\n Source MAC address matches {source_mac} Destination MAC address: {destination_mac}')
            print(f'\nSource IP address: {source_ip} Destination IP address: {destination_ip}')
            
            print(f'\nMessage : {message}')
            

if __name__ == '__main__':
    client_1 = Client("92.10.10.15", "32:04:0A:EF:19:CF")
    client_1.connect()
