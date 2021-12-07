import Menu
from Search import Search as s
import socket


class SearchIp(s):

    def __init__(self):
        pass

    def searcher(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
        result = input("Enter menu or -m to go the menu\n Enter exit or -e to exit the application").lower()
        if result == "menu" or result == "-m":
            Menu.Menu.optionsMenu()
        elif result == "exit" or result == "-e" or result == "" or result is None:
            print("Thanks for using the application bye!")
            quit()
        else:
            print("wrong input you will be forwarded to the applications menu bye!")
            Menu.Menu.optionsMenu()

