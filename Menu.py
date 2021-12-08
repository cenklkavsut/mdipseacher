import SearchEmail
import SearchDomain
import SearchIp


class Menu:
    def __init__(self):
        self.searchType = None
        self.selection = None

    def setSelection(self, value):
        self.selection = value

    def getSelection(self):
        return self.selection

    def setSearchType(self, value):
        self.searchType = value

    def getSearchType(self):
        return self.searchType

    def optionsMenu(self):
        searchType = str(self.getSearchType())
        selection = str(self.getSelection())
        while searchType != "exit" or searchType != "-e" or selection != "exit" or selection != "-e" :
            print("::::::: :::::::::: :: ::....        ::")
            print("::   :: ::            ::  ::        ::")
            print("::   :: :::::::::: :: ::  ::   :::::::")
            print("::::::: ::         :: ::  ::   ::   ::")
            print("     :: ::         :: ::  ::   :::::::")
            print("       ::")

            selection = input(
                                "Enter | search or -s | to display the Search options\n"
                              + "Enter | exit or -e | to exit the application\n"
                                ":").lower()
            if selection == "search" or selection == "-s":
                self.setSelection(selection)
                self.callSearch()
            elif selection == "exit" or selection == "-e":
                break
            else:
                print("Entered wrong search option!")

    def callSearch(self):
        selection = self.getSelection()
        if selection == "search" or selection == "-s":
            searchType = input("Types of Searches\n"
                               + "Enter -ip or ip :To Search a Ip Address of the pc\n"
                               + "Enter -d or domainname:To Search a Domain Name online\n"
                               + "Enter -m or email To Search s Email Address\n"
                               + "Enter -e or exit To exit the application\n"
                               + ":"
                               ).lower()
            self.setSearchType(searchType)
            if searchType != "-e" or searchType != "exit":
                self.basedOptions()
        elif self.selection == "exit" or self.selection == "-e" or self.selection == "" or self.selection is None:
            print("Thanks for using QFind app!")
        else:
            print("No Selection available error!")

    def basedOptions(self):
        searchOptRes = self.getSearchType()
        if searchOptRes == "-ip" or searchOptRes == "ip":
            SearchIp.SearchIp().searcher()
        elif searchOptRes == "-d" or searchOptRes == "domainname":
            SearchDomain.SearchDomain().searchMenu()
        elif searchOptRes == "-m" or searchOptRes == "email":
            SearchEmail.SearchEmail().searcher()
        else:
            print("Error occurred try again later!")
