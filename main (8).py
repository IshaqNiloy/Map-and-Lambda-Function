#For better explanation of lamda and map function see the problem statement

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    if n== 0:
        my_list = []
    elif n == 1:
        my_list = [0]
    elif n == 2:
        my_list = [0,1]
    else:
        my_list = [0,1] 
        for i in range(3,n+1):
            my_list.append(my_list[i - 3] + my_list[i - 2]) 
    
    return my_list
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
