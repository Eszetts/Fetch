import socket
import clinet_compnent
import os


def __main__():

    cli = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    try:
        os.remove('/var/run/shadowsocks-manager.sock')
        os.remove('/tmp/client.sock')
    except Exception as err:
        print("remove err occurs: ", err)

    cli.bind('/tmp/client.sock')  # address of the client
    cli.connect('/var/run/shadowsocks-manager.sock')  # address of Shadowsocks manager

    cli.send(b'ping')
    print(cli.recv(8105))  # You'll receive 'pong'

    cli.send(b'add: {"server_port":8001, "password":"7cd308cc059"}')
    print(cli.recv(8105))  # You'll receive 'ok'

    cli.send(b'remove: {"server_port":8001}')
    print(cli.recv(8105))  # You'll receive 'ok'

    while True:
        clinet_compnent.send(cli.recv(8105))
