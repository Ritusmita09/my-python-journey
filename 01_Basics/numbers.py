x = 2
y = 3
z = 4
print(x+y) #addition
print(z-y) #subtraction
print(x*y) #multiplication
print(y/x) #Normal division

print(x**2) #to the power 2
print(x//z) #Floor division -- 2 ÷ 4 = 0.5--0[floor]
print(y%z) #Remainder

print((x+y)*z) #first we do the do work for parenthesis()
print(x+(y*z)) 

a = 40
b = 22.6
#But we should always do operations between same data type for precision and high level database management
print(a+b) #output = 62.6
#so our intent should be clear that we wanna convert it to same data type first 
print(int(22.6)) #output = 22 
print(float(40)) #output = 40.0

#operator overloading:
print('chai'+'code') #output = chaicode

print(x,y,z) # 2,3,4
