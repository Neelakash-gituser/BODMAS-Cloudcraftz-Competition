import numpy as np

class Solution:

    def new_problem(self):
        operators = ['-', '+', '*', '/']
        N1, N2, N3 = np.random.randint(0, 9, 3)
        x, y = np.random.randint(0, 3, 2)
        O1, O2 = operators[x], operators[y]

        ans = str(N1) + O1 + str(N2) + O2 + str(N3)
        N4 = eval(ans)

        return N1, O1, N2, O2, N3, N4



class BODMAS:
    """
    A mathematical game for geeks .
    """
    operator_stack = ['-', '+', '*', '/']
    operands = [i for i in range(10)]

    # Overloaded Constructor
    def __init__(self, N1, O1, N2, O2, N3, opt_N1, opt_O1, opt_N2, opt_O2, opt_N3, opt_N4, i):
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3 
        self.O1 = O1
        self.O2 = O2
        self.opt_N1 = opt_N1
        self.opt_N2 = opt_N2
        self.opt_N3 = opt_N3
        self.opt_N4 = opt_N4
        self.opt_O1 = opt_O1
        self.opt_O2 = opt_O2
        self.i = i

        # check whether the input is valid or not 
        self.check_input()


    def _cal_value(self):
        flag = 0

        # Checking for operator precedence according to BODMAS and calculating that part which has a higher priority .
        if self.operator_stack.index(self.O2) > self.operator_stack.index(self.O1):
            im = str(self.N2) + self.O2 + str(self.N3)
            temp = eval(im)
        else:
            im = str(self.N1) + self.O1 + str(self.N2)
            temp = eval(im)
            flag = 1 

        # Calculating the total equation .
        if flag == 1:
            res = eval(str(temp) + self.O2 + str(self.N3))
        elif flag == 0:
            res = eval(str(self.N1) + self.O1 + str(temp))

        return res


    def check_input(self):
        actual = True

        # checking if the input operators and operands are valid or not .
        if self.O1 not in self.operator_stack or self.O2 not in self.operator_stack:
            print("An operator must be among one of these - '+', '-', '*', '/'")
            actual = False
        elif self.N1 not in self.operands or self.N2 not in self.operands or self.N3 not in self.operands:
            print("Not a valid operand - operands must be between 0-9")
            actual = False
        
        # if all the operators as well as the operands are valid , check for RHS == LHS or not .
        if actual:
            val = self._cal_value()
            if val != self.opt_N4:
                print("Your RHS not equal to your LHS")
            else:
                self.check_positions()


    def check_positions(self):
        
        red, yellow, green = [], [], []

        print(f'Your entered equation is : {self.N1} {self.O1} {self.N2} {self.O2} {self.N3}')
        your_eq = [self.opt_N1, self.opt_O1, self.opt_N2, self.opt_O2, self.opt_N3]

        if self.N1 in your_eq:
            if self.N1 == self.opt_N1:
                green.append("N1")
            else:
                yellow.append("N1")
        else:
            red.append("N1")


        if self.N2 in your_eq:
            if self.N2 == self.opt_N2:
                green.append("N2")
            else:
                yellow.append("N2")
        else:
            red.append("N2")


        if self.N3 in your_eq:
            if self.N3 == self.opt_N3:
                green.append("N3")
            else:
                yellow.append("N3")
        else:
            red.append("N3")


        if self.O1 in your_eq:
            if self.O1 == self.opt_O1:
                green.append("O1")
            else:
                yellow.append("O1")
        else:
            red.append("O1")
        

        if self.O2 in your_eq:
            if self.O2 == self.opt_O2:
                green.append("O2")
            else:
                yellow.append("O2")
        else:
            red.append("O2")

        print(f"Red - {red}\nYellow - {yellow}\nGreen - {green}")

        if len(green) == 5:
            print("Congratulations !!! You've successfully guessed the right equation.")
            quit()
        if self.i == 2:
            print("You've exhausted all your chances, better luck next time\n")
            print(f"Original equation was - {str(self.opt_N1) + self.opt_O1 + str(self.opt_N2) + self.opt_O2 + str(self.opt_N3)}")

            


# The main body or the driver code:
obj = Solution()
A, B, C, D, E, F = obj.new_problem()

print("The magical number is: {}\n".format(F))

for i in range(3):
    if i == 2:
        print("This is your final try !!!")

    N1, N2, N3 = map(int, input('Enter N1, N2, N3 in the given order: ').split())
    O1, O2 = input('Enter O1 and O2 respectively: ').split()

    obj_new = BODMAS(N1, O1, N2, O2, N3, A, B, C, D, E, F, i)
    print("\n")




