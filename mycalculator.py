class Calculator:
    def __init__(self,input1,input2,input3):
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3
    def operation(self):
        if self.input3=="+":
            return("result",self.input1+self.input2)
        elif self.input3 == "-":
            return("result",self.input1-self.input2)
        elif self.input3 == "*":
            return("result",self.input1*self.input2)
        elif self.input3 == "/":
            if self.input2 == 0:
                raise ValueError("cannot divide by 0")
            return self.input1/self.input2
        else :
            raise ValueError("Invalid operation")
           
try:
  input1 =int(input("enter the first value "))
  input2 = int(input("enter the second value "))
  input3 = input("enter the operation ")
  calc = Calculator(input1,input2,input3)
  result = calc.operation()
  print(f"{result}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
       
