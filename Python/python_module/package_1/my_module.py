def my_factorial(x):

    """Bu fonksiyon girilen sayının faktoriyel sonucunu verir"""


    if x >= 0:
        sonuç = 1
        for i in range(1,x + 1):
            sonuç *= i

    return sonuç   

def my_len(x):
    
    
    counter = 0

    for i in x:
        counter += 1

    return counter    


def my_int_len(x):
    
    
    counter = 0

    for i in str(x):
        counter += 1

    return counter  







