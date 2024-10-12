from typing import Tuple, Union
from math import sqrt


def solution(a, b, c) -> Union[Tuple[float, float], Tuple[float], None]:

    Dis=b**2-4*a*c

    if Dis > 0:
        x1=(-b+sqrt(Dis))/(2*a)
        x2=(-b-sqrt(Dis))/(2*a)

        return (x1,x2)

    elif Dis==0:
        x=(-b)/(2*a)

        return (x,)
    else:

        result = None
    # Add your code here or call it from here
    # a * x * x + b * x + c == 0 

        return result 

print(solution())