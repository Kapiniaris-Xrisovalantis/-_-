from math import sqrt
time =int(input())

q = (time-1)/2

 


prime_flag = 0    
if(q > 1):
    for i in range(2, int(sqrt(q)) + 1):
        if (q % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        pf = 0
        if(time > 1):
            for i in range(2, int(sqrt(time)) + 1):
                if (time % i == 0):
                    pf = 1
                    break
            if (pf == 0):
                print("It's safe")
            else:
                print("It's not safe")
        else:
            print("It's not safe")
    else:
        print("It's not safe")
else:
    print("It's not safe")