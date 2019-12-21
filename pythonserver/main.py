import time
from http.server import HTTPServer
from server import Server


HOST_NAME = 'localhost'
PORT_NUMBER = 8900

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)   #create a new http object
    print(time.asctime(), f'Server Up - {HOST_NAME}, {PORT_NUMBER}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), f'Server Down - {HOST_NAME}, {PORT_NUMBER}')

