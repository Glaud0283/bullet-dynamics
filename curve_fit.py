import matplotlib.pyplot as plt
import numpy as np

data_set = [
    (1, 109.5), (6, 90.0), (11, 76.8), (16, 65.2),
    (1, 110.0), (6, 88.5), (11, 73.6), (16, 64.0),
    (1, 109.3), (6, 88.0), (11, 74.6), (16, 63.6),
    (1, 112.4), (6, 88.5), (11, 76.2),
    (1, 108.0), (6, 87.5), (11, 76.1),
    (1, 112.7), (6, 88.5), (11, 81.0),
    (1, 107.4), (6, 87.9), (11, 75.9),
    (1, 106.9), (6, 89.6), (11, 74.9),
    (1, 105.2), (6, 91.0), (11, 76.4),
    (1, 106.9), (6, 88.9), (11, 78.9),
    ]

def calculate(data_set):
    '''Calculates the values for 2nd degree polynomial fitting.'''
    total_x = 0
    total_y = 0
    total_x2 = 0
    total_x3 = 0
    total_x4 = 0
    total_xy = 0
    total_x2y = 0
    n = 0
    for data in data_set:
        x = data[0]
        y = data[1]
        total_x += x
        total_y += y
        total_x2 += x ** 2
        total_x3 += x ** 3
        total_x4 += x ** 4
        total_xy += x * y
        total_x2y += (x ** 2) * y
        n += 1
    
    result = (total_x, total_y, total_x2, total_x3, total_x4, total_xy, total_x2y, n)
    return result

def gauss_elimination(a, b):
    '''Calculates the solution of a 3x3 matrix system'''
    multiplier1 = a[1][0] / a[0][0]
    a[1][0] = a[1][0] - a[0][0] * multiplier1
    a[1][1] = a[1][1] - a[0][1] * multiplier1
    a[1][2] = a[1][2] - a[0][2] * multiplier1
    b[1] = b[1] - b[0] * multiplier1

    multiplier2 = a[2][0] / a[0][0]
    a[2][0] = a[2][0] - a[0][0] * multiplier2
    a[2][1] = a[2][1] - a[0][1] * multiplier2
    a[2][2] = a[2][2] - a[0][2] * multiplier2
    b[2] = b[2] - b[0] * multiplier2

    multiplier3 = a[2][1] / a[1][1]
    a[2][1] = a[2][1] - a[1][1] * multiplier3
    a[2][2] = a[2][2] - a[1][2] * multiplier3
    b[2] = b[2] - b[1] * multiplier3

    x3 = b[2] / a[2][2]
    x2 = (b[1] - (a[1][2] * x3)) / a[1][1]
    x1 = (b[0] - (a[0][1] * x2) - (a[0][2] * x3)) / a[0][0]

    solution = [
                x1,
                x2,
                x3
                ]

    return solution

def curve_fitting(data_set):
    '''Uses least - squares parabola method to perform curve fitting.'''

    r = calculate(data_set)

    a = [
        [r[4], r[3], r[2]],
        [r[3], r[2], r[0]],
        [r[2], r[0], r[7]] 
        ]
    
    b = [
        r[6],
        r[5],
        r[1]
        ]

    coefs = gauss_elimination(a, b)
    return coefs


def draw_graph():
    '''Draws a graph for the given curve'''
    
    c1, c2, c3 = curve_fitting(data_set)
    x = np.linspace(1,16)
    y = c1 * (x**2) + c2 * (x) + c3
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.plot(x, y, color='red')
    plt.title("Movement of an Airsoft Round, Experimental Data", fontsize = 10)
    plt.ylabel("Longitudinal Velocity (Vx) [m/s]")
    plt.xlabel("Distance from Pistol (x) [m]")
    plt.show()


