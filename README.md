# 2D Heat Diffusion Simulation using RK4
A python code to simulate transient heat conduction on a 2D square plate using the heat equation and a 4th-Order Runge-Kutta (RK4) time integration and finite differences spatial discritezation. The simulation visualizes temperature evolution through an animated heatmap and records the average plate temperature over time.

## Background 
Heat conduction is the process by which thermal energy flows from regions of high temperature to regions of low temperature. The simulation provides a visual representation of heat diffusion across the plate and tracks the average temperature as the system approaches thermal equilibrium by solving the equation: 

$$\frac{\partial T}{\partial t}=\alpha\left(\frac{\partial^2 T}{\partial x^2}+\frac{\partial^2 T}{\partial y^2}\right)$$

Spatial derivatives are approximated using the finite differences method, transforming the partial differential equation into a system of ordinary differential equations. This system is then evolved in time using the fourth-order Runge-Kutta (RK4) method.

The simulation provides a visual representation of heat diffusion across the plate and tracks the average temperature as the system approaches thermal equilibrium.

## Simulation Parameters
<div align="center">

| Parameter  | Description           | Default Value |
| ---------- | --------------------- | ------------- |
| `T`        | Initial temperature   | 20            |
| `sides`    | Plate side length     | 25 mm         |
| `nodes`    | Number of grid nodes  | 100           |
| `simTime`  | Total simulation time | 3 s           |
| `a`        | Thermal diffusivity   | 100           |
| `CFL`      | Stability coefficient | 0.20          |

</div>

## Boundary Conditions 
By default, all four edges of the plate are assigned a fixed temperature of 250C. The boundary temperatures and the coordinates at which they are applied can be modified by the user to simulate different thermal scenarios.

```python
u[-1, :] = 250 # top boundary
u[0, :] = 250 # bottom boundary
u[:, -1] = 250 # left boundary
u[:, 0] = 250 # right boundary
```

## Current features
* View the simulation in real time
* Export the animation as an MP4 video
* Save temperature data to an Excel spreadsheet

## Prerequisites 
* numpy
* matplotlib
* pandas
* FFmpeg (for MP4 output)

## Output Files

The simulation generates two output files upon completion.

`heat_simulation.mp4` contains an animated visualization of the temperature distribution across the plate over time. 

`heat_simulation_data.xlsx` contains the recorded simulation data, including the simulation time and the corresponding average temperature of the plate at each time step. 



