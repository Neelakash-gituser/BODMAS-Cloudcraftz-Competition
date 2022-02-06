from classFiles import BODMAS, Solution


# The main body or the driver code:
while True:
    print("\nNote: If you don't want the final answer that is R.H.S to be a negative number press - [Y/y]")
    print("Disallow Negative numbers as result ? [Y - Yes]\t")
    disallow = input('-> ').lower()

    print('\n')

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
