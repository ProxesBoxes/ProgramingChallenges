import sys
def main():
    my_answer = 0
    X = int(sys.stdin.readline().rstrip())

    def Fib(n):
        if n <= 0:
            return 0
        
        if n ==1 or n ==2:
            return 1

        return Fib(n-1)+Fib(n-2)
        
    i = 2
    fib = 0
    while fib < X:
        fib = Fib(i)
        isEven = fib %2
        if isEven == 0:
            my_answer += fib
        i +=1
    print(my_answer)
main()