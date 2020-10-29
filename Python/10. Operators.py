class Operators:

    def __init__(self, a, b):
        self.first = a
        self.second = b

    def Addition(self):
        return  self.first + self.second

    def Subtraction(self):
        return self.first - self.second

    def Multiplication(self):
        return self.first * self.second

    def Division(self):
        return self.first / self.second

    def Modulus(self):
        return self.first % self.second

    def Exponentiation(self):
        return self.first ** self.second

    def Floor_division(self):
        return self.first // self.second

if __name__ == '__main__':
    x = int(input())
    y = int(input())

    choice = int(input("""
1. Addition         === +
2. Subtraction      === -
3. Multiplication   === *
4. Division         === /
5. Modulus          === %
6. Exponentiation   === **
7. Floor division   === //

..."""))

    oops = Operators(x, y)

    if choice == 1:
        print(oops.Addition())
    elif choice == 2:
        print(oops.Subtraction())
    elif choice == 3:
        print(oops.Multiplication())
    elif choice == 4:
        print(oops.Division())
    elif choice == 5:
        print(oops.Modulus())
    elif choice == 6:
        print(oops.Exponentiation())
    elif choice == 7:
        print(oops.Floor_division())
    else:
        print("Wrong choice")