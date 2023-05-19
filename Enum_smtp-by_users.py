import socket
import sys
import time
        
def enumer_smtp(ip_address):
        """wyszukiwania poprawnych kont użytkowników"""
        #Ścieżka do wordlisty
        user_file_path = "/usr/share/metasploit-framework/data/wordlists/unix_users.txt"
        with open(user_file_path, "r") as user_file:
            for user in user_file:
                user = user.strip()
                if user == "":
                    continue
                try:
                    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sok.connect((ip_address,25))
                    sok.recv(1024)
                    sok.send('VERF ' + user + '\r\n')
                    time.sleep(1)
                    results = sok.recv(1024)
                    if (not "rejected" in results):
                          print("%s: Istneije " % user)
                except Exception:
                      print('wystapił problem')
                finally:
                      sok.close()
        print("\r\n Program sie zakonczył \r\n")

def main():
      print("Witaj w skanerze do wyliczania smtp")
      print("===================================")
      #Adres IP hosta którego enumerujemy 
      enumer_smtp(sys.argv[1])
if __name__ == '__main__':
      main()

