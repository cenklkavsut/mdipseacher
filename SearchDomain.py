from Search import Search as s
import whois
import socket


class SearchDomain(s):

    def __init__(self):
        self.searchName = None
        self.clientSocket = socket.socket()


    def setSearchName(self, value):
        self.searchName = value

    def getSearchName(self):
        return self.searchName

    def searchMenu(self):
        searchName = input("Enter domain name you are searching for or -e to exit\n" +
                           " Example | shearcher | " + "\n:").lower()
        searchName = "www." + searchName
        self.setSearchName(searchName)
        self.searcher()

    def searcher(self):
        domNames = [".com", ".de", ".net", ".cn", ".uk", "tr", ".org", ".info", ".nl", ".eu ", ".ru", ".aero", ".asia",
                    ".biz ", ".cat ", ".com", ".coop",
                    ".edu", ".gov", ".info", ".int ", ".jobs", ".mil", ".mobi ", ".museum", ".name ", ".net ", ".org ",
                    ".pro ", ".te", ".travel"]

        domains = [""] * len(domNames)
        k: int = 0
        for i in range(len(domNames)):
            domains.append(str(self.getSearchName()) + str(domNames[k]))
            k += 1

        if self.getSearchName() != "":
            number = 0
            for l in range(len(domains)):
                print(domains[number], "is registered" if self.is_registered(domains[number]) else "is not registered")
                number += 1
        elif self.getSearchName() == "-e":
            quit()
        else:
            self.searchMenu()

    def is_registered(self, domain_name):
        try:
            print(whois.whois(domain_name))
        except Exception:
            return False
        else:
            return bool(domain_name)