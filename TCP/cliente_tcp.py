import socket
import time
HOST = "127.0.0.1"
PORTA = 5100
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORTA))
    with cliente.makefile("rwb") as canal:
        for seq in range(1, 7):
            mensagem = f"AMOSTRA|{seq}|{20 + seq}"
            inicio = time.perf_counter()
            canal.write((mensagem + "\n").encode("utf-8"))
            canal.flush()
            resposta = canal.readline().decode("utf-8").strip()
            rtt_ms = (time.perf_counter() - inicio) * 1000
            print(f"TCP seq={seq} resposta={resposta} RTT={rtt_ms:.2f} ms")
            time.sleep(0.15)
        canal.write(b"FIM\n")
        canal.flush()
