# About The Project

### Objective
###### This project calculates a bullet's dynamics regarding to aerodynamic, gravitational and inertial a parameters with numerical approach. The program does not include any high level maths libraries(for linear and numeric calculations) and makes all calculations itself. The aim of the project is to calculate bullet's path in the air and physical properties such as force and velocity relations according to time parameter.

### Why Numerical Approach?
###### In engineering problems, sometimes anayltical solutions are not possible or they are hard to reach. Numerical methods are mathematical solutions for physical problems by using approximaitons and error check. This is my first complex python project in Numerical methods. In this project, the maximum tolerable error percantage is |ε| < 0.1%


# Mathematical Background
This project contains several approachs for numerical solutions. In this part, mathematical operations are explained. Program explanations for methods are given in the next part.

### Gauss Elimination
###### Gauss Elimination is a solution method for linear problem systems. It forms a triangular equation system by eliminating variables and then using back-substitution to find unkowns.
###### For more information: https://www.efunda.com/math/num_linearalgebra/num_linearalgebra.cfm?search_string=gauss%20elimination#Gaussian

### Curve Fitting
###### Least - squares parabola method is used  to perform curve fitting. This method uses gauss elimination to fit the given data into a 2nd degree polynomial (parabola). 
###### For more information: https://www.efunda.com/math/leastsquares/lstsqr2dcurve.cfm

### Euler Forward Method
###### The forward Euler method is an iterative method which starts at an initial point and walks the solution forward using the iteration. It is used to calculate bullet's orbit.
###### For more information: https://www.efunda.com/math/num_ode/num_ode.cfm#Euler


# Structure
There are 4 files in the project. `main.py` is to run the code and the others are explained below.

### Processing the data
`curve_fit.py` file manipulates the data for oncoming calculations and it makes the data useful by using gauss elimination and curve fitting.
###### `calculate()` function takes the data as parameter and return the necessary values for least-square parabola methods.
###### `gauss_elimination()` method takes 2 matrixes (a, b) and gives the solution set (x) as output. ( [A] x = B format)
###### `curve_fitting()` takes the data and calculates the coefficients for new parabola by using the functions above.
###### `draw_graph()` draws the calculated parabola.

### Dynamics
`euler_forward.py` is the file that calculates the mechanics all mechanical properties of the object.
###### `calculate_density()` calculates the air density according to room conditions (humidity, pressure etc.)
###### `v_x()` calculates x-axis speed  of the projectile at a specific position according to measurements.
###### `alpha()` Calculates alpha angle (angle between Vx and Vt) of the projectile at a specific position.
###### `f()`Calculates drag force acting on the projectile at a specific position.
###### `calculate_drag_coefficient()` Calculates drag coefficent by using euler forward method.

### Results and Graphs
`plot_graph.py` is used for final values and calculations, results and plotting of the graphs by using the functions in `euler_forward.py`
###### `get_model_pointset()` Calculates all points according to the model.
###### `draw_vx_graph()` Draws longitudinal velocity results versus distance graph for both theoretical and experimental values.
###### `draw_trajectory()` 'Draws trajectory of the round.




