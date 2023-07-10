import math
import curve_fit

# Values
mass = 0.24 # kg
diameter = 0.006 # m
temperature = 16  # C
humidity = 58 # %
pressure = 1024 # mbar

Cd = 1.2 # Initial Guess


air_density = 1.22892 #

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

def calculate_density(t, rh, p):
    '''Calculates moist air's density'''
    vp =  10.53 # calculated by room conditions
    air_density = ((p / (287.05 * (t + 273))) + (vp / (461.495 * (t + 273)))) * 100
    air_density = round(air_density, 5)
    return air_density


def v_x(x):
    '''Calculates x-axis speed  of the projectile at a specific position according to measurements'''
    c1, c2, c3 = curve_fit.curve_fitting(data_set)
    v = c1 *  x**2 + c2 * x + c3
    return v

def alpha(x, y):
    '''Calculates alpha angle (angle between Vx and Vt) of the projectile at a specific position'''

    alpha = math.atan(y / x)
    return alpha


def f(x, Cd, v):
    '''Calculates drag force acting on the projectile at a specific position'''
    rho = calculate_density(temperature, humidity, pressure)
    a = ((diameter * math.pi)**2) / 4
    f_x = round(rho * Cd * a * v ** 2, 5)  
    return f_x

def calculate_drag_coefficent():
    '''Calculates drag coefficent by using euler forward method'''
    c = 1
    error_max = 1 / 1000
    drag_coef = 1.2 # Initial guess
    dt = 0.01
    ds = 0.01
    x = 0 
    while True:
        velocity_x = v_x(1) #Initial condition
        velocity_y = 0
        v_total = velocity_x #Initial condition
        i = 1.0
        while True:
            v_total = round(math.sqrt(velocity_x ** 2 + velocity_y ** 2), 5)
            force = round(f(i, drag_coef, v_total), 5)
            alph = alpha(velocity_x, velocity_y)
            velocity_y = round((force * math.sin(alph) / mass) * dt + velocity_y, 5)
            velocity_x = round(-1 * (force * math.cos(alph) / mass) * dt + velocity_x, 5)

            if i == 6:
                v_exp = v_x(i)
                error = abs(velocity_x - v_exp) / velocity_x

                if(error > error_max):
                    i = 1.0
                    if (velocity_x < v_exp):
                        drag_coef = round(drag_coef - ds, 2)
                        break

                    elif (velocity_x > v_exp):
                        drag_coef = round(drag_coef + ds, 2)
                        break
                else:
                    print(f"\nCoefficent found!\nValue:{drag_coef}\nError:{error * 100}%")
                    return drag_coef
            
            i += dt
            i = round(i,2)
            x += dt

        c += 1
