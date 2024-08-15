import SearchEmail
import SearchDomain
import SearchIp


class Menu:
    def __init__(self):
        self.selection = None
        self.searchType = None

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
        while searchType != "exit" or searchType != "-e" or selection != "exit" or selection != "-e":
            print("::::::: :::::::::: :: ::....        ::")
            print("::   :: ::            ::  ::        ::")
            print("::   :: :::::::::: :: ::  ::   :::::::")
            print("::::::: ::         :: ::  ::   ::   ::")
            print("     :: ::         :: ::  ::   :::::::")
            print("       ::")

            selection = input("Enter | search or -s | to display the Search options\n"
                              + "Enter | exit or -e | to exit the application\n" + ":").lower()
            if selection == "search" and selection == "-s":
                self.setSelection(selection)
                self.callSearch()
            elif selection == "exit" or selection == "-e":
                pass
            else:
                print("Entered wrong search option!")

    def callSearch(self):
        selection = self.getSelection()
        if selection == "search" or selection == "-s":
            searchType = input("Types of Searches\n"
                               + "Enter -ip :To Search a Ip Address of the pc\n"
                               + "Enter -d :To Search a Domain Name online\n"
                               + "Enter -m :To Search s Email Address\n"
                               + "Enter -e or exit To exit the application\n"
                               + ":").lower
            if searchType != "-e" or searchType != "exit":
                self.setSearchType(searchType)
                self.appMenu()
        elif self.selection == "-e" or self.selection == "exit":
            print("Thanks for using QFind app!")
        else:
            print("No Selection available error!")

    def appMenu(self):
        if str(self.getSearchType()) == "-ip":
            SearchIp.SearchIp().searcher()
        elif str(self.getSearchType()) == "-d":
            SearchDomain.SearchDomain().searchMenu()
        elif str(self.getSearchType()) == "-m":
            SearchEmail.SearchEmail().searcher()
        else:
            print("Error occurred try again later!")
