import euler_forward
import math
import matplotlib.pyplot as plt
import numpy as np
import curve_fit

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

drag_coef = euler_forward.calculate_drag_coefficent()

def get_model_pointset(data_set):
    '''Calculates all points according to the model'''
    point_set_x= []
    point_set_y= []
    velocity_x = euler_forward.v_x(1) #Initial condition
    v_total = velocity_x #Initial condition
    velocity_y = 0
    i = 1.0
    dt = 0.01
    x = 0
    while i <= 16:
        v_total = round(math.sqrt(velocity_x ** 2 + velocity_y ** 2), 5)
        force = round(euler_forward.f(i, drag_coef, v_total), 5)
        alph = euler_forward.alpha(velocity_x, velocity_y)
        velocity_y = round((force * math.sin(alph) / euler_forward.mass) * dt + velocity_y, 5)
        velocity_x = round(-1 * (force * math.cos(alph) / euler_forward.mass) * dt + velocity_x, 5)
        point_set_x.append(i)
        point_set_y.append(velocity_x)
        i += dt
        i = round(i,2)
        x += dt
    return point_set_x, point_set_y

def draw_vx_graph():
    '''Draws longitudinal velocity results versus distance graph for both theoretical and experimental values '''
    x_list, y_list = get_model_pointset(data_set)
    c1, c2, c3 = curve_fit.curve_fitting(data_set)
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
    plt.plot(x, y, color = 'red')
    plt.plot(x_list, y_list, color = "blue")
    plt.title("Movement of an Airsoft Round, Theoretical vs Experimental", fontsize = 10)
    plt.ylabel("Longitudinal Velocity (Vx) [m/s]")
    plt.xlabel("Distance from Pistol (x) [m]")
    plt.show()

def draw_trajectory():
    '''Draws trajectory of the round '''
    point_set_x= []
    point_set_y= []
    velocity_x = euler_forward.v_x(1) #Initial condition
    v_total = velocity_x #Initial condition
    velocity_y = 0
    dt = 0.01
    x = 0
    y = 1.5
    t = 0
    while True:    
        point_set_x.append(x)
        point_set_y.append(y)
        v_total = round(math.sqrt(velocity_x ** 2 + velocity_y ** 2), 5)
        force = round(euler_forward.f(t, drag_coef, v_total), 5)
        alph = euler_forward.alpha(velocity_x, velocity_y)
        velocity_y = round(-1 * (force / euler_forward.mass) * dt + velocity_y, 5)
        velocity_x = round((force / euler_forward.mass) * dt + velocity_x, 5)
        t = round(dt + t, 3)

        x = round(x + velocity_x * dt, 5)
        y = round(y + velocity_y * dt, 5)

        if y <= 0:
            print(f"It takes {t} seconds to hit the ground.\nFinal Speeds:  X: {velocity_x}, Y: {velocity_y}\nFinal Coordinates:   X: {x}, Y: 0")
            break

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.plot(point_set_x, point_set_y, color = "blue")
    plt.title("Movement of an Airsoft Round, Trajectory", fontsize = 10)
    plt.ylabel("Y Position [m]")
    plt.xlabel("X Position [m]")
    plt.show()



   