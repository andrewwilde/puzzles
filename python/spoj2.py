
def calculate_primes(s, n):
    fragment = 10000
    while True: 
        primes = [False] * 2 + [True] * (fragment-1)
        for x in xrange(int(n**0.5 + 1.5)):
            if primes[x]:
                for i in range(x * x, fragment + 1, x):
                    primes[i] = False

        for v in xrange(fragment + 1):
            if v >= s and primes[v]:
                yield v

        s = s + 10000

cases = raw_input()

for x in range(0, int(cases)):
    my_input = raw_input().split(" ")

    prime_list =  calculate_primes( int(my_input[0]), int(my_input[1]) )
    print str(list(prime_list))
