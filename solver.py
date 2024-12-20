import math
import matplotlib.pyplot as plt

def f_x(x):
    if abs(x) > 1:
        return 0
    
    return math.exp(-((1)/(1 - (x*x))))

def g_x(x):
    if x < 0 or x > 1:
        return 0
    
    return x

def generate_series(func, upper, lower, delta_x):
    y = []
    x = []
    point = lower

    while point <= upper:
        x.append(point)
        y.append(func(point))
        point += delta_x

    return x, y


def step(func, u, DT, DX):

    u_new = []

    for l in range(1, len(u) - 1):
        u_new.append( func(u[l-1], u[l], u[l+1], DT, DX) )
    
    return [0] + u_new + [0]


def plot_time(t, DT, DX, u, x, step_func, plotter=plt):

    for _ in range( round(t/DT) ):
        u = step(step_func, u, DT, DX)

    plotter.plot(x, u, label=f"t={t}")