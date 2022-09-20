def is_prime(num):
  if (num<2):
    return False
  elif(num == 2):
    return True
  elif(num%2 == 0):
    return False
  i=2  
  while i<int(num/2):
    if(num%i == 0):
      return False
    i=i+1
  return True

my_prime_list = [2]
def my_primes(threepoints, num=3):
  for i in range(1,100):
    if(is_prime(num)):
      my_prime_list.append(num)
      if(len(my_prime_list) == threepoints):
        print(my_prime_list)
        break
    if(i == 99):
      my_primes(threepoints,num+2)
    num+=2

my_primes(101)