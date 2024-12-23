import matplotlib.pyplot as plt
from solver import plot_time, generate_series, f_x, g_x

def FTCS(up, u, un, DT, DX, c=1):
    return (-1) * ((c * DT)/(2 * DX)) * (un - up) + u

def lax_freidman(up, u, un, DT, DX, c=1):
    C = (c*DT)/DX 
    return 0.5*(1-C)*un + 0.5*(1+C)*up

def upwind(up, u, un, DT, DX, c=1):
    C = (c*DT)/DX 
    return u - C * (u - up)

def lax_wendoff(up, u, un, DT, DX, c=1):
    C = (c*DT)/DX
    return u - C*0.5*(un - up) + C*C*0.5*(un - 2*u + up)



if __name__ == "__main__":

    DX = 0.01
    DT = 0.0001
    TIME = [1]
    METHOD = FTCS
    C = DT/DX

    _, axes = plt.subplots(1, 2, figsize=(15, 5))

    x, u = generate_series(f_x, 3, -3, DX)
    axes[0].plot(x, u, label="t=0")
    for i in TIME:
        plot_time(i, DT, DX, u, x, METHOD, axes[0])
    
    axes[0].legend()
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("u")
    axes[0].set_title("f(x)")

    x, u = generate_series(g_x, 3, -3, DX)
    axes[1].plot(x, u, label="t=0")
    for i in TIME:
        plot_time(i, DT, DX, u, x, METHOD, axes[1])
    axes[1].legend()
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("u")
    axes[1].set_title("g(x)")

    plt.suptitle(f"Solved With {METHOD.__name__}: DX={DX}, DT={DT}, C={C:.2f}")
    plt.tight_layout()
    plt.show()