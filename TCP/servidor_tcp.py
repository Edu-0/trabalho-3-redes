import socket
HOST = "127.0.0.1"
PORTA = 5100
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORTA))
    servidor.listen(1)
    print(f"Servidor TCP aguardando em {HOST}:{PORTA}", flush=True)
    conexao, endereco = servidor.accept()
    with conexao, conexao.makefile("rwb") as canal:
        print(f"Cliente conectado: {endereco}", flush=True)
        while True:
            linha = canal.readline()
            if not linha:
                break
            mensagem = linha.decode("utf-8").strip()
            if mensagem == "FIM":
                break
            print(f"Recebido via TCP: {mensagem}", flush=True)
            canal.write(f"RECEBIDO|{mensagem}\n".encode("utf-8"))
            canal.flush()
    print("Conexao TCP encerrada.", flush=True)
