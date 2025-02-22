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
    comp = len(derivative.atoms())
    comp += s.count_ops(derivative)
    if comp<100:
     derivative = s.simplify(derivative)
    return derivative
def critical_points(function):
    function = s.sympify(function)
    derivative1 = derivative(function)

    # ✅ Convert Abs() to piecewise (fixes SymPy crashing)
    derivative1 = derivative1.rewrite(s.Piecewise)
    derivative1 = derivative1.replace(s.Abs(x), s.Piecewise((-x, x < 0), (x, x >= 0)))

    # ✅ Use numerical solving instead of slow symbolic solving
    try:
        cp = s.solve(s.Eq(derivative1, 0), x)
    except NotImplementedError:
        cp = []
        for guess in [-5, -2, 0, 2, 5, 10]:  # Adjust guesses if needed
            try:
                root = s.nsolve(derivative1, x, guess)
                if root not in cp:
                    cp.append(root)
            except:
                continue

    return cp if cp else "No extreme points"

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
    if isinstance(value, (int, float)):  # ✅ Handles normal numbers
        return True
    if not isinstance(value, s.Basic):  # ✅ Ensure it's a SymPy object
        return False
    return value.is_real and not value.has(s.zoo, s.nan)

def graph(function):
    function = s.sympify(function, evaluate=False)  # ✅ Prevents excessive simplification
    print("✅ Function Loaded Without Auto-Simplification!")

    # Convert function to a fast NumPy function
    print("⏳ Converting to NumPy-compatible function...")
    try:
        y_func = s.lambdify(x, function, 'numpy')  # ✅ Avoids symbolic processing
    except Exception as e:
        print(f"❌ ERROR Converting to NumPy: {e}")
        return
    print("✅ NumPy Function Ready!")

    # Generate x values
    print("⏳ Generating X values...")
    x_vals = np.linspace(-10, 10, 300)  # Reduce number of points
    print("✅ X values Generated!")

    # Compute y-values
    print("⏳ Evaluating Y-values...")
    try:
        y_vals = y_func(x_vals)
    except Exception as e:
        print(f"❌ ERROR Evaluating Y-values: {e}")
        return
    print("✅ Y-values Evaluated!")

    # Prevent stretching from extreme values
    print("⏳ Clipping extreme Y-values...")
    y_vals = np.clip(y_vals, -10, 10)
    print("✅ Extreme values clipped!")

    # Plot the function
    print("⏳ Plotting Graph...")
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=str(function), color='b')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.title(f"Graph of {function}")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    print("✅ Graph Successfully Plotted!")
    plt.show()





    

