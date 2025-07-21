
X1 = input("Number 1")

X2 = input ("number 2/Denominator")
x1 = float(X1)
x2 = float (X2)
def Addition():
      return x1 + x2 

def Multiplication():
     return x1 * x2

def Division():
      return x1 / x2

X = input("+,*./").strip()
if X == "+":
    print("Result:", Addition())
elif X == "*":
    print("Result:", Multiplication())
elif X == "/":
    print("Result:", Division())
else:
    print("Invalid operation.")
