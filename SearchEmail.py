from validate_email_address import validate_email
import re
]'
from Search import Search as s


class SearchEmail(s):

    def __init__(self):
        self.selection = str(s.getSelection())

    def searcher(self):
        self.selection = input("Enter -ip to check target email by ip\n"
                               "Enter -m email address to see if it exist the email address\n:")

        if self.selection == "-ip":
            value = input("Enter ip address to check if it matches a email\n:")

        elif self.selection == "-m":
            value = input("Enter email address to check if it exist\n | exampleEmail | \n:")
            self.emailComparer()
        else:
            quit()

    def emailComparer(self):
        domNames = ["@gmail.com", "@icloud.com","@outlook.com","@hotmail.fr" ,"@hotmail.com", "@hotmail.nl",
                     "@protonmail.com","@hotmail.co.uk", "@hotmail.de",".@hotmail.com.tr","@hotmail.net","@yahoo.com",
                    "@aim.com", "@aol.com", "@yandex.com", "@zohomail.com", "@pm.me", "@protonmail.ch","@example.org",
                    "@accountant.com", "@africamail.com", "@artlover.com", "@asia.com", "@cheerful.com", "@consultant.com",
                    "@contractor.net", "@dr.com", "@email.com", "@engineer.com", "@europe.com", "@execs.com", "@fastservice.com"
                    , "@hackermail.com", "@iname.com", "@homemail.com","@mail.com", "@musician.org", "@myself.com", "@planetmail.com",
                    "@accountant.com", "@post.com", "@techie.com", "@usa.com", "@writeme.com", "@workmail.com"]

        domains = [""] * len(domNames)
        k: int = 0
        for i in range(len(domNames)):
            domains.append(str(self.getSearchName()) + str(domNames[k]))
            k += 1
        emailNum = 0
        for num in domains:
            emailValid= self.emailResult(domains[emailNum])
            print(emailValid)
            emailNum += 1

    def emailResult(self, emailNum: object):
        isvalid = validate_email(str(emailNum), verify=True)
        return f"email:{emailNum} and email is registered:{isvalid}"



