from Search import Search as s
import whois


class SearchDomain(s):

    def __init__(self):
        self.searchName =None

    def setSearchName(self, value):
        self.searchName = value

    def getSearchName(self):
        return self.searchName

    def searchMenu(self):
        searchName = input("Enter domain name you are searching for\n" +
                           " Example | shearcher | " + "\n:").lower()
        searchName = "www." + searchName
        self.setSearchName(searchName)

    def searcher(self):
        domains = []
        domNames = [".COM", ".DE", ".NET", ".CN", ".UK", "TR", ".ORG", ".INFO", ".NL", ".EU ", ".RU", ".aero", ".asia",
                    ".biz ", ".cat ", ".com", ".coop",
                    ".edu", ".gov", ".info", ".int ", ".jobs", ".mil", ".mobi ", ".museum", ".name ", ".net ", ".org ",
                    ".pro ", ".te", ".travel"]
        i = 0
        for domNames in domNames:
            temp = self.getSearchName() + str(domNames[i])
            domains[i].push(temp)
            i += 1
        if self.getSearchName() != "" or self.getSearchName() is not None:
            number = 0
            for domain in domains:
                number += 1
                print(domain[number], "is registered" if self.is_registered(domain[number]) else "is not registered")
        else:
            quit()

    def is_registered(self, domain_name):
        try:
            w = whois.whois(domain_name)
        except Exception:
            return False
        else:
            return bool(w.domain_name)


"""
    def is_registered(self, domain_name):
        domNames = [".COM", ".DE", ".NET", ".CN", ".UK", ".ORG", ".INFO", ".NL", ".EU ", ".RU",".aero",".asia" ,".biz ",".cat ",".com" ,".coop" ,
                    ".edu" ,".gov" ,".info",".int ",".jobs",".mil" ,".mobi ",".museum",".name ",".net ",".org ",".pro ",".te" , ".travel"]
        domains = []
        domResult = []
        domNameExt = None
        i = 0
        for domNames in domNames:
            #checks if domain name is registered
            try:
                domNameExt = domNames[i].lower()
                i += 1
                w = str(domain_name) + str(domNameExt)
                w = whois.whois(domain_name)
                domains = [w].push()
            except Exception:
                print("Not registered")
            else:
               x = 0
               for domain in domains:
                  print(f"result:{domains[x]}")
                  x +=1
                  domains=[x]
                  print(domains[x] + "is registered" )

"""
