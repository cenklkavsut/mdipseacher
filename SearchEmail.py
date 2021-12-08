from Search import Search as s


class SearchEmail(s):

    def __init__(self):
        self.selection = None

    def searcher(self):
         selection =str(s.getSelection())
         print("Email Search")
         selection = input("Enter ip of target:")