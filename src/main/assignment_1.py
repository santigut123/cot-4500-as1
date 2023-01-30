def double_pres_convert(binary):
    sign=(-1)**int(binary[0])
    exponent=binary[1:12]
    mantissa=binary[12:]
    result=0.0
    exponentRes = 0.0
    mantissaRes = 0.0
    for index, value in enumerate(exponent[::-1]):
        exponentRes+=float(value)*2**float(index)
    result = 2**(exponentRes - 1023)
    for index,value in enumerate(mantissa):
        mantissaRes+=float(value)*((1.0/2.0)**float(index+1))
    mantissaRes+=1.0

    return result*mantissaRes*sign
def three_digit_chop(number):
    index =0
    
    while(number>1.0):
        number/=10.0
        index+=1
    number = number-(number%0.001)
    return number*(10**index)
   

    
    
    
    


def three_digit_round(number):
    index =0
    round = 0
    while(number>1.0):
        number/=10.0
        index+=1
    number+= .0005
    number = number-(number%0.001)
    return number*(10**index)

def inf_series():
    value =1  
    index =0
    
    
    while(value>(10.0**-4.0)):
        index+=1
        value=series(index)
      
    return index -1

def series(index):
    return ((1**(index))/(index**(3.0)))


def bisect(function, a, b, tol):
    index =0
    c = a
    while ((b-a) >= tol):
        index+=1
        c = (a+b)/2
        if (function(c) == 0.0):
            break
        if (function(c)*function(a) < 0):
            b = c
        else:
            a = c
    return index

def function(x):
    return x*x*x + (4*(x*x)) -10
def function_prime(x):
    return 3*(x*x) + (8*x)
def newton(function,tol, estimation,max_iter):
    i = 1
    temp=0.0
    while(i<max_iter):
        if(function_prime(estimation)!=0):
            temp = estimation - (function(estimation)/function_prime(estimation))
            if(abs(temp-estimation)<tol):
                return i
            i+=1
            estimation = temp
        else:
            return "error"
    return i
        




        





def main():
    num = double_pres_convert("010000000111111010111001")
    round_abs_error = num-three_digit_round(num)
    round_rel_error = round_abs_error/num
    print(num,"\n")
    print(three_digit_chop(num),"\n")
    print(three_digit_round(num),"\n")    
    print(abs(round_abs_error))
    print(abs(round_rel_error),"\n")
    print(inf_series(),"\n")
    a = -4
    b = 7
    tolerance = (10.0**(-4.0))
    root = bisect(function, a, b, tolerance)
    newton_root = newton(function,tolerance,7,100)
    print("%.f \n"%root)
    print(newton_root)

        



main()


   
