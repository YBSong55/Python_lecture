def root_func(a,b,c):
    r1 = (-b +(b**2-4*a*c)**(0.5))/(2*a)
    r2 = (-b -(b**2-4*a*c)**(0.5))/(2*a)
    return r1, r2

##리턴값을 그대로 출력하면?? 리턴 값이 여러개면 튜플!!로 제공
root = root_func(1,5,c=6)
print(root)

##리턴값을 각 각 반환받고 싶을땐?
root1, root2 = root_func(1,5,6)
print("첫번째 근 : ",root1,",  두번째 근 : ",root2)