import random
def guss(x):
   rand_num = random.randint( 1 , x )
   addad='0'
   k = 0
   while int(addad) !=rand_num :
       k = k + 1
       addad=input('Enter Number Between (0,'+str(x)+'):')
       
       if  int(addad) < rand_num :
            print ('less than...')
       else: 
            print  ('greater than ...')  
 
   print ('You Winned after step.')


guss(10)