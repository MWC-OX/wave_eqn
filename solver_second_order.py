import matplotlib.pyplot as plt


def step(u, up, DT, DX, c=1):

    u_new = []
    C = (c*DT)/(DX)

    for l in range(1, len(u) - 1):
        u_new.append( 2*u[l] - up[l] + C*C*(u[l+1] - 2*u[l] + u[l-1]) )
    
    return [0] + u_new + [0]


def plot_time(t, DT, DX, u, x, plotter=plt):

    up = u.copy()

    for _ in range( round(t/DT) ):
        u_new = step(u, up, DT, DX)
        up = u.copy()
        u = u_new.copy()

    plotter.plot(x, u, label=f"t={t}")