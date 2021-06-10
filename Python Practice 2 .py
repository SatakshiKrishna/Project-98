introString = int( input('Enter Your Choice 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division'))
firstNumber = int(input('Enter First Number'))
secondNumber = int(input('Enter Second Number'))
if(introString==1):
  total = firstNumber+secondNumber
if(introString==2):
  total = firstNumber-secondNumber
if(introString==3):
  total = firstNumber*secondNumber
if(introString==4):
  total = firstNumber/secondNumber 
print ("Output is")
print (total) 