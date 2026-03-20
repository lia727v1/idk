#def is_pari(n):
  '''ritorna vero se e pari senno ritorna falso'''
  #for i in range(0,5):
   #   if last_digit(n)==2*i:        #let n be  even, let's say it's on the magnitude of 10^k, then we know the number can be expressed as 10^k*2*i,
   #                                 # where i is an integer between 0 and 4, so we can check if the last digit of n is equal to 2*i for some i in 
   #                                 #that range , hence the loop works
   #       return True
  #else:
   #   return False
#numero=int(input('numero'))

#is_pari(numero)
#print(is_pari(numero))
#
#
#
#
#
#
#
#
#
#
#
def collaz():                    #es 1,2 sequenza collaz
    n=int(input('gemme number'))
    a=0
    for i in range(0,100):
        a=a+1
        if n!=1 and n%2==0:
            n=n//2
            print(n)
        if n!=1 and n%2!=0:
            n=3*n+1
            print(n)
        if n==1: 
            
            print(f'iterations={a}')
            break
    if n==1:
        print('done')
    else:
        print('number too large or negative')


def analize_sequence():
    n=int(input('gemme number'))
    a=0
    number_list=[]
    for i in range(0,100):
        a=a+1
        if n!=1 and n%2==0:
            n=n//2
            print(n)
            number_list.append(n)
        if n!=1 and n%2!=0:
            n=3*n+1
            print(n)
            number_list.append(n)

        if n==1: 
            
            print(f'iterations={a}')
            number_list.append(n)
            break

    for i in range(0,a):
        c=0
    
        for p in range(0,a):
            if number_list[p]-number_list[i]<0 or number_list[p]-number_list[i]==0:
                c=c+1
            if c==a:
                print(f'{number_list[i]} is the largest number in the sequence')
    

    for i in range(0,a):
        c=0
    
        for p in range(0,a):
            if number_list[p]-number_list[i]>0 or number_list[p]-number_list[i]==0:
                c=c+1
            if c==a:
                print(f'{number_list[i]} is the smallest number in the sequence')
    
    for i in range(0,a):
        


                

    if n==1:
        print('done')
    else:
        print('number too large or negative')
    
analize_sequence()