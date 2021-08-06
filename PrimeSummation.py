import sys
def main():

    def isPrime(num):
        # If given number is greater than 1
        if num > 1:
        
            # Iterate from 2 to n / 2
            for i in range(2, int(num/2)+1):
        
                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    return False
            else:
                return True
        
        else:
            return False

    upper = int(sys.stdin.readline().rstrip())

    primes = []

    i = 0
    while i <= upper:
        if isPrime(i):
            primes.append(i)
        i +=1

    print(sum(primes))
main()
