import string
from home import db_functions
import re

class Check:

    error = ''

    def checkusername(uname):
        if len(uname) >= 12 or len(uname) == 0:
            return False
        elif any(c in uname for c in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            return False
        elif any(c in uname for c in string.punctuation):
            return False
        else:
            return True

    def checknickname(niname):
        if len(niname) > 16 or len(niname) == 0:
            return False
        for c in niname:
            if c.isdigit():
                return False
            if c in set(string.punctuation):
                return False

        return True

    def checkpassword(pword):
        if len(pword) > 16 or len(pword) < 8:
            return False
        elif any(c in pword for c in string.punctuation):
            return False
        elif not any(c.isupper() for c in pword):
            return False
        elif not any(c.islower() for c in pword):
            return False
        elif not any(c.isdigit() for c in pword):
            return False
        else:
            return True

    def checkdateofbirth(self, birth):
        if len(birth) != 8:
            return False
        month = int(birth[0:2])
        day = int(birth[2:4])
        year = int(birth[4:8])
        if month < 1 or month > 12:
            return False
        if any(month == c for c in(1, 3, 5, 7, 8, 10, 12)):
            if day > 31 or day < 1:
                return False
        if any(month == c for c in(4, 6, 9, 11)):
            if day > 30 or day < 1:
                return False
        if year > 2018:
            return False
        if month == 2 and (day != 28 or day != 29):
            return False
        if month == 2 and day == 28 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            return False
        if month == 2 and day == 29 and ((year % 4 != 0 or year % 100 == 0) or (year % 400 != 0)):
            return False
        return True

    def checkemail(self, email):
        while "@" and "." not in email:
            return False
        else:
            email_pattern = re.search("(^[a-z0-9A-Z-.]+\@[a-z0-9A-Z-.]+\.[a-zA-Z0-9-.])", email)
            return bool(email_pattern)

    def checkgender(self, gen):
        if len(gen) != 1:
            return False
        if any(gen == c for c in('m, M, f, F')):
            return True
        else:
            return False

    def checkhomepage(self, uname, pword):
        global error
        if (self.checkusername(uname) and self.checkpassword(pword)) is False:
            error = 'You entered invalid Username or Password!!!!!'
            return False
        if self.checkdatabasehomepage(uname, pword) is False:
            return False
        else:
            return True

    def checkdatabasehomepage(uname, pword):
        global error
        if db_functions.checkUsrName(uname):
            if db_functions.logIn(uname, pword) is False:
                error = 'You entered invalid Username or Password!!!!!'
                return False
            else:
                return True
        else:
            error = 'You need to sign Up!!!!!'
            return False

    def geterror(self):
        return error

    def checkeditpage(self, emailv, birthv):
        global error
        if self.checkemail(Check, emailv) and self.checkdateofbirth(Check, birthv):
            return True
        else:
            error = 'You have invalid input'
            return False

    def checksignuppage(self,uname,pword,email,birth, gen):
        global error
        if self.checkusername(uname) and self.checkpassword(pword) and self.checkgender(Check, gen) and self.checkemail(Check,email) and self.checkdateofbirth(Check, birth):
            if db_functions.checkUsrName(uname) is False:
                return True
            else:
                error = 'The username you have entered is already taken by someone!!!!'
                return False
        else:
            error = 'You have entered invalid information!!!!'
            return False
