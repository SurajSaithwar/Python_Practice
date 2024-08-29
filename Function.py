# Function is block of statements that perform a specific task.\

def sum(a,b): # Function defined and (a and b are parameters)
    sum=a+b
    print(sum)

sum(5,9) # function call (3,5 are arguments)

# Assigning a default parameter,which is used when no arguments is passed

def greater(a,b=5):
    if a>b:
        print(a,"is greater")
    else:
        print(b,"is greater")
greater(8)

# parameter without a default follows parameter with a default
'''def greater(a=7,b):  #this program throw an error because we use default value in parameter1 but not on Parameter
    if a>b:
        print(a,"s greater")   
    else:
        print(b,"is greater")
greater(8)'''

#WAF to print the length of a string.(List is the parameter)
li=[1,2,3,4,6]
def list_len(lst):
    len_lst=len(lst)
    print(len_lst)
list_len(li)

#WAF to print the elements of a list in a single line.(list is the parameter)
li=[1,2,3,4,6]
def lst(li_):
    for i in li_:
        print(i,end=" ")
        i+=1
lst(li)

#WAF to find the factorial of n.(n is the parameter)


def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
fact(4)

#WAF to convert USD to INR
def exchange_rate(USD):
    usd=80*USD
    print(usd)
exchange_rate(5)
#WAF to find the factorial of n using recursion
def rec_fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*rec_fact(n-1)
print(rec_fact(5))

#Write a recursive function to calculate the sum of first n natural number
def sum(n):
    if n==0:
        return 0
    return sum(n-1)+n
print(sum(8))
 


