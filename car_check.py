class car:
  def __init__(self):
    self.name = input('enter the name of your car: ')
    self.speed = 100
    self.__openlock = 123
    self.defaultoil = 50

  def changespeed(self):
      desire = input('Do you want to change the speed of your car? ')
      if desire == 'yes':
        self.speed = int(input('Enter your new speed for the car: '))
        
  def openlock(self,locknumber):
      if locknumber==self.__openlock:
        print('Opened successfully!!')
      else:
        print('Wrong lock number')

  def checkoil(self):
     print(self.defaultoil)

  def charge(self, name):
      if self.name == "Tesla":
        print('This car is chargable')
      else:
        print('This car is not electrically chargable')

  def filltank(self,name):
      if name == 'BMW':
        print("This car's tank is fillable")
      else:
        print('We can not fill the tank of an electric car')

    
## Chceck the code for Tesla 
Tesla = car() 
Tesla.changespeed()
Tesla.openlock(123)
Tesla.checkoil()
Tesla.charge(Tesla)
Tesla.filltank(Tesla)

## Check the code for BMW

BMW = car() 
BMW.changespeed()
BMW.openlock(123)
BMW.checkoil()
BMW.charge(Tesla)
BMW.filltank(Tesla)

        
