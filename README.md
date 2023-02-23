# **Introduction**

Plotting 2D and 3D coordinate systems can be time-consuming and difficult. As such, I created this repository to help make things a bit easier.


# **Getting Started**

The following code:
* Imports the `numpy` library as `np` for convenience,
* Imports the plot_frames library,
* Imports the `pyplot` module from the `matplotlib` library as `plt` for convenience, and
* Imports all of the modules from the `spatialmath` library.

```python
import numpy as np
import plot_frames

from matplotlib import pyplot as plt
from spatialmath import *
```


# **Plotting 2D Systems**

The following code:
* Creates a new figure,
* Configures the figure's axes,
* Creates a 2D system, and
* Puts text at an X,Y position, draws a 2D arrow, and draws the coordinate system.

```python
fig = plt.figure()
ax = fig.add_subplot()

dims = [0,2]
ax.set_xlim(dims)
ax.set_ylim(dims)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
ax.set_xticks(np.arange(min(dims), max(dims)+1, 0.5))
ax.set_yticks(np.arange(min(dims), max(dims)+1, 0.5))

T = SE2([0.5,0.5])
print(f"T=\n{T}")

plot_frames.plot_text2d(np.array([0.5,0.5]), text='A')
plot_frames.plot_arrow2d(np.array([0.0,0.0]), np.array([0.5,0.5]))
plot_frames.plot_pose2d(T, frame='A', color="blue")
```  
Afterwards, something similar to the following will be displayed:

![height:320](doc/img/figure_01.png)  
*Figure*: Plot of a 2D pose.


# **Plotting 3D Systems**

The following code:
* Creates a new figure,
* Configures the figure's axes,
* Creates a 3D system, and
* Puts text at an X,Y,Z position, draws a 3D arrow, and draws the coordinate system.

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

dims=[0,2]
ax.set_xlim(dims)
ax.set_ylim(dims)
ax.set_zlim(dims)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.grid(True)
ax.set_xticks(np.arange(min(dims), max(dims)+1, 0.5))
ax.set_yticks(np.arange(min(dims), max(dims)+1, 0.5))
ax.set_zticks(np.arange(min(dims), max(dims)+1, 0.5))

T = SE3([0.5,0.5,0.0])
print(f"T=\n{T}")

plot_frames.plot_text3d(np.array([0.5,0.5,0.0]), text='A')
plot_frames.plot_arrow3d(np.array([0.0,0.0,0.0]), np.array([0.5,0.5,0.0]))
plot_frames.plot_pose3d(T, frame='T', color="blue")
```
Afterwards, something similar to the following will be displayed:

![height:320](doc/img/figure_02.png)  
*Figure*: Plot of a 3D pose.

# **References**

1. [https://github.com/petercorke/spatialmath-python](https://github.com/petercorke/spatialmath-python).

# **Credit**

Dr Frazer K. Noble  
Department of Mechanical and Electrical Engineering  
Massey University    
Auckland  
New Zealand    
L: https://www.linkedin.com/in/drfknoble/  
G: https://github.com/drfknoble  
