N = int(input("Please enter your number:")) 
def ifFibonacci(N):
    b3 = 0
    b1 = 1
    b2 = 1
    # 0 and 1 both are fibonacci numbers
    if (N == 0 or N == 1):
        print("Given number is a fibonacci number")
     
    else:
        # check to confirm if generated fibonacci series is less than provided number N
        while b3 < N:
            b3 = b1 + b2
            b2 = b1
            b1 = b3
        if b3 == N:
            print("It is a fibonacci number")
        else:
            print("It is not a fibonacci number")
ifFibonacci(N);

            

