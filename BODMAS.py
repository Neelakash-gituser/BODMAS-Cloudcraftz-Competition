import numpy as np

# This is the class which generates the random equation along with the random output i.e. N4 .
class Solution:

    def new_problem_neg(self, disallow=True):
        # disallow negative results .
        while disallow:
            operators = ['-', '+', '*', '/']
            N1, N2, N3 = np.random.randint(0, 9, 3)
            x, y = np.random.randint(0, 3, 2)
            O1, O2 = operators[x], operators[y]

            ans = str(N1) + O1 + str(N2) + O2 + str(N3)
            N4 = eval(ans)

            if N4 >= 0:
                disallow = False

        return N1, O1, N2, O2, N3, N4

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

    # default Constructor
    def __init__(self, N1, O1, N2, O2, N3, opt_N1, opt_O1, opt_N2, opt_O2, opt_N3, opt_N4):
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

        # check whether the input is valid or not
        self.check_input()


    # function calculating the output of the equation entered by the user.
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
        blank = " "

        # checking if the input operators and operands are valid or not .
        if self.O1 not in self.operator_stack or self.O2 not in self.operator_stack:
            print("An operator must be among one of these - '+', '-', '*', '/'")
            actual = False
        elif self.N1 not in self.operands or self.N2 not in self.operands or self.N3 not in self.operands:
            print("Not a valid operand -> operands must be between 0-9")
            actual = False

        # if all the operators as well as the operands are valid , check for RHS == LHS or not .
        if actual:
            val = self._cal_value()
            if val != self.opt_N4:
                print("Your RHS not equal to your LHS")
            else:
                self.check_positions()

    # checks for the positions of the entered values and gives a feedback .
    def check_positions(self):

        red, yellow, green = [], [], []
        blank = " "

        print(f'Your entered equation is : {self.N1} {self.O1} {self.N2} {self.O2} {self.N3}')
        your_eq = [self.opt_N1, self.opt_O1, self.opt_N2, self.opt_O2, self.opt_N3]

        if self.N1 in your_eq:
            if self.N1 == self.opt_N1:
                green.append(f"N1: {self.N1}")
            else:
                yellow.append(f"N1: {self.N1}")
        else:
            red.append(f"N1: {self.N1}")


        if self.N2 in your_eq:
            if self.N2 == self.opt_N2:
                green.append(f"N2: {self.N2}")
            else:
                yellow.append(f"N2: {self.N2}")
        else:
            red.append(f"N2: {self.N2}")


        if self.N3 in your_eq:
            if self.N3 == self.opt_N3:
                green.append(f"N3: {self.N3}")
            else:
                yellow.append(f"N3: {self.N3}")
        else:
            red.append(f"N3: {self.N3}")


        if self.O1 in your_eq:
            if self.O1 == self.opt_O1:
                green.append(f"O1: {self.O1}")
            else:
                yellow.append(f"O1: {self.O1}")
        else:
            red.append(f"O1: {self.O1}")


        if self.O2 in your_eq:
            if self.O2 == self.opt_O2:
                green.append(f"O2: {self.O2}")
            else:
                yellow.append(f"O2: {self.O2}")
        else:
            red.append(f"O2: {self.O2}")

        print(f"Red - {red}\nYellow - {yellow}\nGreen - {green}")

        if len(green) == 5:
            print("\nCongratulations !!! You've successfully guessed the right equation.")
            quit()



# The main body or the driver code:
while True:
    print("\nNote: If you don't want the final answer that is R.H.S to be a negative number press - [Y/y]")
    print("Disallow Negative numbers as result ? [Y - Yes]\t")
    disallow = input('-> ').lower()
    obj = Solution()

    if disallow == 'y':
        A, B, C, D, E, F = obj.new_problem_neg()
    else:
        A, B, C, D, E, F = obj.new_problem()


    print("The magical number is: {}\n".format(F))
    print("Input Format:\n1. Enter N1, N2, N3 each of them must be a single digit positive integer between 0 and 9.\n2. O1 and O2 are operators -> '+', '-', '*' or '/'\n")


    # loops until the players have exhausted all their chances or they've guessed it correctly whichever comes first.
    while True:
        blank = " "
        try:
            N1, N2, N3 = map(int, input('Enter N1, N2, N3 in the given order: ').split())
        except:
            print("A numerical value is expected")
            continue

        O1, O2 = input('Enter O1 and O2 respectively: ').split()

        obj_new = BODMAS(N1, O1, N2, O2, N3, A, B, C, D, E, F)

        print("\nWant to try Again? 1 - Yes , 0 - No")
        ans = int(input('-> '))
        if ans != 1:
            print(f"\nOriginal equation was -> {str(A) + blank + B + blank + str(C) + blank + D + blank + str(E) + ' = ' + str(F)}")
            print("\n======================================================================================================================================")
            break
        
    print("\nStart new game ? [Y/N]")
    new = input('-> ').lower()
    if new != 'y':
        break
