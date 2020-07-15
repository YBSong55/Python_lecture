def div(a,b=2):
    result = round(a/b,2)
    return result

print('div(4)',div(4))
  
print('div(9,3)',div(9,3))

print('div(a=9,b=3)',div(a=9,b=3))

##키워드 인자끼리는 자리 바꾸기 쌉가능!
print('div(b=3,a=9)',div(b=3,a=9))

print('div(9,b=3)', div(9,b=3))

##위치 인자는 키워드 인자 뒤에 있어서는 안된다.

## div(b=4,16) ===> Error!!!!!!!!!!!!!!

