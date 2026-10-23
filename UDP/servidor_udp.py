import socket
HOST = "127.0.0.1"
PORTA = 5001
SIMULAR_FALHA = False  # Na terceira rodada, altere para True.
silenciadas = set()
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
    servidor.bind((HOST, PORTA))
    print(f"Servidor UDP em {HOST}:{PORTA} (falha={SIMULAR_FALHA})", flush=True)
    try:
        while True:
            dados, endereco = servidor.recvfrom(1024)
            mensagem = dados.decode("utf-8").strip()
            partes = mensagem.split("|")
            if len(partes) != 3 or partes[0] != "AMOSTRA":
                continue
            seq = partes[1]
            print(f"Recebido via UDP: {mensagem}", flush=True)
            if SIMULAR_FALHA and seq == "3" and seq not in silenciadas:
                silenciadas.add(seq)
                print("Simulacao: resposta da amostra 3 nao enviada.", flush=True)
                continue
            resposta = f"RECEBIDO|{mensagem}".encode("utf-8")
            servidor.sendto(resposta, endereco)
    except KeyboardInterrupt:
        print("Servidor UDP encerrado.")
