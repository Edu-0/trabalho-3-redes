import socket
import time
HOST = "127.0.0.1"
PORTA = 5001
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:
    cliente.settimeout(0.8)
    for seq in range(1, 7):
        mensagem = f"AMOSTRA|{seq}|{20 + seq}".encode("utf-8")
        for tentativa in (1, 2):
            inicio = time.perf_counter()
            cliente.sendto(mensagem, (HOST, PORTA))
            try:
                dados, _ = cliente.recvfrom(1024)
                resposta = dados.decode("utf-8").strip()
                rtt_ms = (time.perf_counter() - inicio) * 1000
                print(f"UDP seq={seq} tentativa={tentativa} "
                      f"resposta={resposta} RTT={rtt_ms:.2f} ms")
                break
            except socket.timeout:
                print(f"UDP seq={seq} tentativa={tentativa}: TIMEOUT")
        else:
            print(f"UDP seq={seq}: sem resposta apos 2 tentativas.")
        time.sleep(0.15)
