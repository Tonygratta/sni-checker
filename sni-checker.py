import socket
import ssl
import datetime
DEF_SERVER_IP = "142.250.185.206"

def quick_check(ip, hostname, port=443):
    """Быстрая проверка подключения"""
    try:
        # Создаем socket и подключаемся
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((ip, port))
        
        # Создаем SSL контекст с SNI
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        ssl_sock = context.wrap_socket(sock, server_hostname=hostname)
        ssl_sock.close()
        return True
        
    except Exception as e:
        return False
#
if __name__ == "__main__":
    #
    now = datetime.datetime.now()
    fname = "checked-"+now.strftime("%Y-%m-%d_%H-%M-%S")+".txt"
    wl_file = open("names.txt","r")
    wl_lines = wl_file.readlines()
    wl_len  = len (wl_lines)
    checks = 0
    success_checks = 0
    with  open(fname,"w") as checkedlist:
        for line in wl_lines:
            checks = checks + 1
            line = line.strip()
            print (f'{success_checks}/{checks}/{wl_len} (found/checked/all) SNI={line}...', end = '')
            if quick_check(DEF_SERVER_IP, line):
                success_checks = success_checks + 1
                print("Success!")
                checkedlist.write(line+'\n')
            else:
                print("Error.")
        print (success_checks, " addresses found")
