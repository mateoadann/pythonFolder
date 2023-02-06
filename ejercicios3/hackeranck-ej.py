n = 3
if n%2 == 0 and 2<n<5:
    print('Not Weird')
elif n%2 == 0 and 6<n<20:
    print('Weird')
elif n%2 == 0 and n>20:
    print('Not Weird')
elif n%2 != 0:
    print('Weird')
else:
    print(f'mal')
    
def backward_string(val: str) -> str:
    # your code here
    # for i in range(len(val)):
    #     result =[]
    #     result.append([val(i)])
    #     print(result)
    result = slice(0,val,1)
    return f'nice \n', result


print(backward_string('val'))
a = [1, 2, 3]