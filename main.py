import math

from sympy.utilities.lambdify import lambdify
import sympy as sp
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def separate(start_Point,end_Point,steps):
    """

    :param start_Point:start point
    :param end_Point:  end point
    :param steps: steps between two numbers
    :return: separate the start point and end point by steps (example :start=0 ,end =1 ,steps=0.1 so now 0,0.1,0.2,..,1)
    """
    r = start_Point
    while r < end_Point:
        yield r
        r += steps
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def save(start_Point,end_Point,steps):
    """

    :param start_Point: start point
    :param end_Point: end point
    :param steps: steps between two numbers
    :return: arr with steps jump (example :start=0 ,end =1 ,steps=0.1 return  [0,0.1,0.2,..,1])
    """
    i0=separate(start_Point,end_Point,steps)
    y=["%g" % x for x in i0]
    for i in range(len(y)):
        y[i]=float(y[i])
        if(y[i]<0.1 and y[i]>-0.1):
            y[i]=0
    size=len(y)
    if(y[size-1] != end_Point):
        y.append(end_Point)
    return y
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def calculate_Bisection_Method_Eror(eror,a,b):
    x=math.log((eror)/(b-a))
    x=math.ceil((-x)/math.log(2))
    return x

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def Bisection_Method(func, start, end, epsilon):
    '''

    :param func: func
    :param start: start point
    :param end: end point
    :param epsilon: epsilon
    :return: solution by bisection method and how many iteration to find the solution
    '''
    x = sp.symbols('x')
    func = lambdify(x, func)
    b=end
    a=start
    counter=0
    c = b
    while (b - a) > epsilon:
        c=(a+b)/2
        if func(a) * func(c) > 0:
            a = c
        else:
            b = c
        counter+=1
    return c,counter

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def Newton_Raphson(func,start,end,epsilon):
    '''
        :param func: func
        :param start: start point
        :param end: end point
        :param epsilon: epsilon
        :return: solution by newton raphson method and how many iteration to find the solution
    '''
    xr=(end+start)/2
    xr1=end+2
    x = sp.symbols('x')
    g=func
    f_prime = g.diff(x)
    func = lambdify(x, func)
    f_prime = lambdify(x, f_prime)
    tempxr=xr
    count=0
    while abs(xr1-xr)>epsilon:
        xr=tempxr
        xr1=xr-((func(xr))/(f_prime(xr)))
        tempxr=xr1
        count+=1
    return xr1,count
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def secant_method(func,start,end,epsilon):
    '''
        :param func: func
        :param start: start point
        :param end: end point
        :param epsilon: epsilon
        :return: solution by scenat methoddand how many iteration to find the solution
    '''
    func = lambdify(x, func)
    xi1=end
    xi=start
    xr=(end+start)/2
    tempxi1=xi1
    count=0
    while abs(xi1-xi)>epsilon :
        xi1=tempxi1
        xr=((xi*func(xi1))-xi1*func(xi))/(func(xi1)-func(xi))
        xi=xi1
        tempxi1=xr
        xi1=xr
        count+=1
    return xr,count
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def main_Menu(func,start,end,epsilon):
    temp=func
    g = lambdify(x, func)
    arr = save(start, end, 0.1)
    sol = []
    iteration = []
    answer = int(input("Enter 1 for Bisection Method / 2 for Newton Raphson / 3 for Secant Method\n"))
    for i in range(len(arr)):
        if (g(arr[i]) == 0):
            sol.append(arr[i])
            iteration.append(0)
    for i in range((len(arr)-1)):
        if g(arr[i])*g(arr[i+1])<0:
            if answer==1:
                s, c = Bisection_Method(func, arr[i], arr[i + 1], epsilon)
                check=calculate_Bisection_Method_Eror(epsilon,start,end)
                if c>=check:
                    raise Exception("Bisection Method dose not good for this function")
                sol.append(s)
                iteration.append(c)
            elif answer==2:
                s,c=Newton_Raphson(func,arr[i],arr[i+1],epsilon)
                sol.append(s)
                iteration.append(c)
            elif answer==3:
                s,c=secant_method(func,arr[i],arr[i+1],epsilon)
                sol.append(s)
                iteration.append(c)

    f_prime = temp.diff(x)
    f_prime1=temp.diff(x)
    f_prime = lambdify(x, f_prime)

    for i in range((len(arr)-1)):
        if f_prime(arr[i])*f_prime(arr[i+1])<0:
            if answer==1:
                s, c = Bisection_Method(f_prime1, arr[i], arr[i + 1], epsilon)#check bisection method for prime func
                check=calculate_Bisection_Method_Eror(epsilon,start,end)
                if c>=check:
                    raise Exception("Bisection Method dose not good for this function")

                sol.append(s)
                iteration.append(c)
            elif answer==2:
                s,c=Newton_Raphson(f_prime1,arr[i],arr[i+1],epsilon)#check Newton Raphson for prime func
                sol.append(s)
                iteration.append(c)
            elif answer==3:
                s,c=secant_method(f_prime1,arr[i],arr[i+1],epsilon)#check Secant method for prime func
                sol.append(s)
                iteration.append(c)

    if len(sol)>0:
        print("[", end=" ")
        for i in range(0,len(sol)):
            print("Solution num {0}: {1}".format(i+1,iteration[i]), end=" ")
            if i != (len(iteration) - 1):
                print("iteration,", end=" ")
            else:
                print("iteration", end=" ")
        print("]", end=" ")
        print(" ")
        print("Solution: ")
        print(sol)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
x = sp.symbols('x')
cos=sp.cos
f=4*x**3-48*x+5   #function to check
l=cos(x)+1  #function to check
m=x**3-4.4*x**2+12.619
k=x**2  #function to check
temp=math.pow(10,-10)   #epsilon
main_Menu(f,-5,5,temp)