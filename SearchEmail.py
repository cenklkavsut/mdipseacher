from Search import Search as s


class SearchEmail(s):

    def __init__(self):
        self.selection = None

    def setSelection(self, value):
        self.selection = value

    def getSelection(self):
        return self.selection

    def searcher(self):
         selection =str(self.getSelection())
         print("Email Search")
         selection = input("Enter ip of target:")