import sys
def main():
    def Fib(n):
        if n <= 0:
            return 0
        
        if n ==1 or n ==2:
            return 1

        return Fib(n-1)+Fib(n-2)

    want = int(sys.stdin.readline().rstrip())
    found =False
    fibNum = 1
    while not found:
        fibVal = Fib(fibNum)
        count=0
        n = fibVal
        while(n>0):
            count=count+1
            n=n//10

        if count==want:
            print("F%d"%fibNum)
            return
        fibNum += 1


main()