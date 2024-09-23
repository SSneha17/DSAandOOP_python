def fizzBuzz(n):
    # Write your code here
   l = n+1
   for i in range(1, n+1):
       if(n % 5 == 0 and n% 3 == 0):
         print('FizzBuzz')
       elif(n % 5 == 0):
         print('Buzz')
       elif(n % 3 == 0):
         print('Fizz')
       else:
         print(i)
       

def GetReverseString(str):
   s = str.split(" ")
   print(s)
   s.reverse()
 
   print(s)
   final = " ".join(s)
   return final.swapcase()
   
if __name__ == '__main__':
    
    #n = int(input().strip())

    #fizzBuzz(n)


    print(GetReverseString("aWESOME iS cO   ding"))