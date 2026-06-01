import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd 

# Initialization
T = 20.0 # temperature
sides = 25  # plate dims 
nodes = 100  # lower = faster simulation
simTime = 3   # max simulation time (s) 
dx = sides / (nodes - 1)
dy = sides / (nodes - 1)
dx2 = dx**2

# Dataframe initialization
tValues = []
tMeanValues = [] 

# 2D plate parameters 
a = 100  # thermal diffusivity
u = np.full((nodes, nodes), T)  # initial temp

# Set boundary conditions (ex. [coords] = temp)
u[-1, :] = 250  # top boundary 
u[:, 0] = 250  # right boundary 
u[:, -1] = 250  # left boundary  
u[0, :] = 250  # bottom boundary 

tMax = np.max(u) # max value for heatmap

# CFL condition for stability using numerical approximation
CFL = 0.20  # CFL condition 
dt = CFL*(dx2/a)
step = int(simTime/dt)+1

def laplacian(u):
    lap = np.zeros_like(u)
    lap[1:-1, 1:-1] = (u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2] - 4*u[1:-1, 1:-1])/dx2
    return lap

def RK4(u, dt):
    k1 = dt * a * laplacian(u)
    k2 = dt * a * laplacian(u + 0.5 * k1)
    k3 = dt * a * laplacian(u + 0.5 * k2)
    k4 = dt * a * laplacian(u + k3)
    u_new = u + (k1 + 2*k2 + 2*k3 + k4) / 6
    return u_new

# Output, Animation, Save
fig, ax = plt.subplots()
heatmap = ax.imshow(u, cmap=plt.cm.jet, vmin=0, vmax=tMax, origin='lower', animated=True)
plt.colorbar(heatmap, label='Temperature')
ax.set_xlabel('x (mm)')
ax.set_ylabel('y (mm)')
title = ax.text(0.3,0.05,"",bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},transform=ax.transAxes, ha="center")

def update(frame):
    global u
    if frame < step - 1:
        u = RK4(u, dt)
        current_time = frame * dt
    else:
        dtf = simTime - (frame - 1) * dt
        u = RK4(u, dtf)
        current_time = simTime
        
    heatmap.set_array(u)
    avg_temp = np.mean(u)
    tValues.append(current_time)
    tMeanValues.append(avg_temp)
    title.set_text(f"t = {current_time:.5f} s,\nAverage Temp = {avg_temp:.3f} °C")
    print(f"Average temperature at t = {current_time:.5f} s: {avg_temp:.3f} °C")
    
    if frame >= step - 1:
        if ani.event_source is not None:
            ani.event_source.stop()
        print(f"Final average temperature at t = {current_time:.5f} s: {avg_temp:.3f} °C")
    
    return [heatmap, title]

choice = input("Do you want to view the animation [1] or save it as an MP4 [2]? \n").strip()

if choice not in ("1", "2"):
    print("Invalid input. Program terminated.")
    exit()

ani = animation.FuncAnimation(fig, update, frames=step, interval=1, blit=True)

if choice == "2":
    print("Saving animation as heat_simulation.mp4...")
    Writer = animation.FFMpegWriter(fps=60, metadata={'title': 'Heat Simulation'})
    ani.save("heat_simulation.mp4", writer=Writer)
    print("Animation saved as heat_simulation.mp4.")
else:
    print("Plotting animation...")
    plt.show()
    print("End of simulation.")

data = pd.DataFrame({"Time (s)": tValues, "Average Temperature (°C)": tMeanValues})
data.to_excel("heat_simulation_data.xlsx", index=False)
print("Temperature data saved to heat_simulation_data.xlsx")