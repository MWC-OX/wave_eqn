import matplotlib.pyplot as plt
from solver import f_x, g_x, generate_series
from solver_second_order import plot_time


if __name__ == "__main__":
    DX = 0.01
    DT = 0.001
    TIME = [0.5, 2.5]
    C = DT/DX

    _, axes = plt.subplots(1, 2, figsize=(15, 5))

    x, u = generate_series(f_x, 3, -3, DX)
    axes[0].plot(x, u, label="t=0")
    for i in TIME:
        plot_time(i, DT, DX, u, x, axes[0])
    
    axes[0].legend()
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("u")
    axes[0].set_title("f(x)")

    x, u = generate_series(g_x, 3, -3, DX)
    axes[1].plot(x, u, label="t=0")
    for i in TIME:
        plot_time(i, DT, DX, u, x, axes[1])
    axes[1].legend()
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("u")
    axes[1].set_title("g(x)")

    plt.suptitle(f"Second Order: DX={DX}, DT={DT}, C={C:.2f}")
    plt.tight_layout()
    plt.show()