import socket

# TCPサーバの実装

# AF_INETでIPv4, SOCK_STREAMでTCP/IP
""" with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 50007))
    # 1接続
    s.listen(1)

    while True:
        # 接続ができたら、connectionとaddressを取得
        conn, addr = s.accept()
        with conn:
            while True:
                # chunk1024で受け取る
                data = conn.recv(1024)
                if not data:
                    break
                print(f'{data=}, {addr=}')
                # 接続先にレスポンスをbytesで返す必要がある
                conn.sendall(b'Received:' + data) """


# UDPサーバの実装
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data, addr = s.recvfrom(1024)
        print(f'{data=}: {addr=}')
