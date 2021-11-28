class bank_acount:
    def __init__(self):
        self.name = None
        self.__password = int(input('Enter your password '))
        self.__credit = int(input('Enter your credit '))
        self.__bonouscredit = 2000
        self._protectedvalue = 5
        self.choseaction()

    def checkbalance(self, password):
        if password == self.__password:
            print(self.__credit)

    def addcredit(self, password):
        if password == self.__password:
            new_credit = int(input('Enter your desired credit '))
            self.__credit += new_credit
            self.__taxing()
            print('Operation went successfully, your new credit is,', self.__credit)

    def changepassword(self, password):
        if password == self.__password:
            new_password = int(input('Enter your new password '))
            self.__password = new_password
        else:
            print('Wrong passowrd')

    def withdraw(self, password):
        if password == self.__password:
            withdraw = int(input('Enter the amount of money you want to get '))
            if withdraw <= self.__credit:
                self.__credit -= withdraw
                print('You withdrawed successfully')
            else:
                print(
                    'You don\'t have enought money, please enter a value less than or equall to', self.__credit)

    # Creating a private function

    def __taxing(self):
        self.__credit -= 10

    def getbonous(self):
        password = int(input('Enter your password to know your bonous '))
        if password == self.__password:
            print(self.__bonouscredit)

    def setbonous(self):
        password = int(input('Enter your password to set your bonous '))
        if password == self.__password:
            self.__bonouscredit = int(input('Enter your new bonous credit '))

    def choseaction(self):
        password = int(
            input('Enter your password to proceed to the next step '))
        while True:
            option = int(input(
                'Choose one number: 1- Check Blanace 2- Add credit 3- Change Password 4- Withdraw '))
            if option == 1:
                self.checkbalance(password)
            elif option == 2:
                self.addcredit(password)
            elif option == 3:
                self.changepassword(password)
            elif option == 4:
                self.withdraw(password)
            else:
                break

# trying to inheret bank_account class into CIB class (CIB is a popular bank in Egypt)


class anything:
    anyvalue = 5


class CIB_account(bank_acount, anything):
    def Welcomuser(self):
        print('Welcome to CIB!')
# will not work beacuse self.__password is private
#  def makeempytcredit (self,password):
#      if password == self.__password:
#          self.__credit=0

    def checkprotected(self):
        value = int(
            input('Enter a value to check the validity of the procted method'))
        if value == self._protectedvalue:
            print('That works')

    def printanyvalueinmultibleinheritances(self):
        # ordinary variables are also printed with self.variable_name
        print(self.anyvalue)
#hendyz = CIB_account()

# polymorphism


class operations:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):  # add is now assigned to the second add function, if you add(a,b) this will give an error
        print(a+b+c)
# o = operations()
# o.add(1,2)

# composition


class composition:
    def __init__(self):
        self.__attributes = dict()
        self.methods = dict()

    def makeattritbute(self, attribtuename, attributevalue):
        self.__attributes[attribtuename] = attributevalue

    def getattribute(self, attributename):
        print(self.__attributes[attributename])

    def printallattributes(self):
        for i in self.__attributes:
            print(i, self.__attributes[i])

    def delteattribute(self, attributename):
        del self.__attributes[attributename]
        print(self.__attributes)

    def addmethod(self, methodname, method):
        self.methods[methodname] = method

    def callmethod(self, methodname):
        self.methods[methodname]()

    def printallmethod(self):
        for i in self.methods:
            print(i)


c = composition()


def power2():
    x = int(input('Enter a number to be squared'))
    print(x*x)


c.addmethod('power', power2)
c.callmethod('power')
c.callmethod('power')
c.printallattributes()
