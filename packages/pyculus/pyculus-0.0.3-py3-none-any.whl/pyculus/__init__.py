import matplotlib.pyplot as plt
import numpy as np
import sympy as s
from sympy import S
from sympy.calculus.util import continuous_domain 
from sympy import sin, cos, tan, cot, pi, E
__all__ = ['symbols', 'sin', 'cos', 'tan', 'cot'] 


# ad built-in support for symbols (x,y,z,pi,E)
#############################################
x = s.symbols('x')
y = s.symbols('y')
z = s.symbols('z')

# Trigonometric functions
sin = sin
cos = cos
tan = tan
cot = cot

# Mathematical constants
pi = pi  # π
e = E    # e

# Injecting into the global namespace
def _inject_globals():
    import builtins
    # Symbols
    builtins.x = x
    builtins.y = y
    builtins.z = z

    # Trigonometric functions
    builtins.sin = sin
    builtins.cos = cos
    builtins.tan = tan
    builtins.cot = cot

    # Mathematical constants
    builtins.pi = pi
    builtins.e = e

_inject_globals()
#############################################


def symplify(function):
    function = s.sympify(function)
    simplified = s.sympify(function)
    return simplified
def domain(function):
    function = s.sympify(function)
    domain = continuous_domain(function,x,S.Reals)
    return domain
def derivative(function):
    function = s.sympify(function)
    derivative = s.diff(function)
    derivative = s.simplify(derivative)
    return derivative
def critical_points(function):
    function = s.sympify(function)
    derivative1 = derivative(function)
    cp = s.Eq(derivative1,0)
    cp = s.solve(cp,x)
    if len(cp)>0:
       return cp
    else:
       return "No extreme points"
def _table_code(function):
        yf = s.sympify(function)
        D = domain(function)
        f = derivative(function)
        ex = critical_points(function)
        ea=(len(ex))
        tc=2*ea+1
        t=np.empty((3,tc+1),dtype=object)
        t[0,0]='X'
        t[1,0]='Y'
        t[2,0]="Y'"
        for i in range(1,len(ex)+1):
            t[0,2*i]=ex[i-1]
            if i<1 or i>1:
               aex=ex[i-2]+ex[i-1]
               aex=aex/2
               t[0,2*i-1]=aex
        t[0,tc]=ex[-1]+1
        t[0,1]=ex[0]-1

        ey=[]
        for i in range(len(ex)):
            ey.append(yf.subs(x,ex[i]))
        for i in range(1,len(ey)+1):
            t[1,2*i]=ey[i-1]
        yf1=s.sympify(f)
        yf1=s.simplify(yf1)
        for i in range(1,tc+1):
            t[2,i]=yf1.subs(x,t[0,i])
            if t[2,i]>0:
               t[1,i]="U"
            if t[2,i]<0:
               t[1,i]="D"

            u=""
            d=""
            if t[1,1]=="U":
               u+="x<"+str(t[0,2])
            if t[1,1]=="D":
               d="x<"+str(t[0,2])
            if t[1,-1]=="U":
               u+=", "+"x>"+str(t[0,-2])
            if t[1,-1]=="D":
               d+=", "+"x>"+str(t[0,-2])
        for i in range(3,tc-1):
            if t[1,i]=="U":
                u+=", "+str(t[0,i-1])+"<x<"+str(t[0,i+1])
            if t[1,i]=="D":
                d+=", "+str(t[0,i-1])+"<x<"+str(t[0,i+1])
            if d=="":
                u=D
                d="No decreasing intervals"
            if u=="":
                d=D
                u="No increasing intervals"

        exy=[]
        for i in range(len(ex)):
            i="("+str(ex[i])+","+str(ey[i])+")"
            exy.append(i)
        ep=[]
        for i in range(1,len(ex)+1):
            if t[1,2*i-1]=="U" and t[1,2*i+1]=="D":
                ep.append(str(exy[i-1])+"max")
            if t[1,2*i-1]=="D" and t[1,2*i+1]=="U":
                ep.append(str(exy[i-1])+"min")
        return t,d,u,ep
def table(function):
    return _table_code(function)[0]
def extreme(function):
    return _table_code(function)[3]
def decreasing(function):
    return _table_code(function)[1]
def increasing(function):
    return _table_code(function)[2]

def is_finite(value):
    """Helper function to check if a value is finite (not NaN or complex)."""
    return value.is_real and not value.has(s.zoo, s.nan)

def graph(function):
    function = s.sympify(function)

    # Compute x-limits
    ex = critical_points(function)
    x_min = float(min(ex)) - 1 if ex else -10
    x_max = float(max(ex)) + 1 if ex else 10

    # Compute y-values at important points
    y_vals = []
    for val in [x_min, x_max] + ex:
        y_val = function.subs(x, val)
        if is_finite(y_val):  # ✅ Only keep valid values
            y_vals.append(float(y_val))

    if not y_vals:  # ✅ If no valid y-values, set default limits
        y_min, y_max = -10, 10
    else:
        y_min = min(y_vals) - 1
        y_max = max(y_vals) + 1

    # Generate x values
    x_vals = np.linspace(x_min, x_max, 1000)
    y_vals = [s.lambdify(x, function, 'numpy')(val) for val in x_vals]

    # Remove NaN values
    y_vals = np.array(y_vals)
    y_vals = y_vals[np.isfinite(y_vals)]  # ✅ Filters out NaN and infinite values

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, [s.lambdify(x, function, 'numpy')(val) for val in x_vals], label=str(function), color='b')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.title(f"Graph of {function}")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()

    

