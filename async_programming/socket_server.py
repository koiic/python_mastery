import socket
import selectors
from selectors import SelectorKey




def stream_data(connection):
    try:
        buffer = b''

        while buffer[-2:] != b'\r\n':
            data = connection.recv(2)

            if not data:
                break
            else:
                print(f"I got data: ", {data})
                buffer += data

        print(f"All data is {buffer}")
        connection.send(buffer)
    except BlockingIOError:
        pass


def single_client_connection(server_socket):
    connection, client_address = server_socket.accept()
    print(f'I got a connection from {client_address}!')
    connection.setblocking(False)
    return connection
    # stream_data(connection)


def multiple_client_connection(server_socket: socket.socket):
    connections = []

    try:
        while True:
            try:
                # accept client conn, return the connection and client address
                connection, client_address = server_socket.accept()
                connection.setblocking(False)
                print(f'I got a connection from {client_address}!')

                connections.append(connection)
            except BlockingIOError:
                pass

            for connection in connections:
                stream_data(connection)


    finally:
        server_socket.close()


def main(selector):
    # create a new socket of INET address family using TCP
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )

    # set socket option to make port reusable after shutdown
    server_socket.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
    )

    address = '127.0.0.1', 8000,

    # set the socket address for the client to connet
    server_socket.bind(address)

    # listen to incoming request from client
    server_socket.listen()
    server_socket.setblocking(False)

    selector.register(server_socket, selectors.EVENT_READ)

    while True:
        events: list[tuple[SelectorKey, int]] = selector.select(timeout=1)

        if len(events) == 0:
            print('No events, waiting a bit more')

        for event, _ in events:
            event_socket = event.fileobj

            if event_socket == server_socket:
                connection = single_client_connection(server_socket)
                selector.register(connection, selectors.EVENT_READ)

            else:
                data = event_socket.recv(1024)
                print(f'I got some data: {data}')
                event_socket.send(data)





    multiple_client_connection(server_socket)


if __name__ == '__main__':
    selector = selectors.DefaultSelector()

    main(selector)
