x = 300

def closest(A, B, C):

    numA = abs(x - A); numB = abs(x - B); numC = abs(x - C)

    if A == B and B == C:
        print(f"A is {A}, B is {B}, C is {C}, hence, all numbers are equal.")

    elif numA < numB and numA < numC:
        print(f"\nThe closest number to {x} is the first number with a value of {A}")

    elif numB < numA and numB < numC:
        print(f"\nThe closest number to {x} is the second number with a value of {B}")

    elif numC < numA and numC < numB:
        print(f"\nThe closest number to {x} is the third number with a value of {C}")



A = int(input("Enter first number: "))
B = int(input("\nEnter second number: "))
C = int(input("\nEnter third number: "))

closest(A, B, C)
