# Copyright (c) 2023, drfknoble (Dr Frazer K. Noble)
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 


import matplotlib.pyplot as plt
import numpy as np

from spatialmath import *
from mpl_toolkits.mplot3d import Axes3D
  

def new_plot3d(dims=None, labels=None, steps=None, **kwargs):
    """
    Create new 3D plot

    Example:
    .. runblock:: pycon
        >>> from plot_frames import new_plot3d
        >>> new_plot3d(dims=[-2,2])
    """

    if dims is None:
        dims = [-2, 2]

    if labels is None:
        labels = ['X', 'Y', 'Z']

    if steps is None:
        steps = 1.0

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor("white")
    ax.set_proj_type('ortho')
    ax.set_xlim(dims)
    ax.set_ylim(dims)
    ax.set_zlim(dims)
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])
    ax.grid(True)
    ax.set_xticks(np.arange(min(dims), max(dims)+1, steps))
    ax.set_yticks(np.arange(min(dims), max(dims)+1, steps))
    ax.set_zticks(np.arange(min(dims), max(dims)+1, steps))


def plot_text3d(pos, ax=None, color=None, delta=None, text=None, **kwargs):
    """
    Plot 3D text

    Example:
    .. runblock:: pycon
        >>> from my_graphics import plot_text3d
        >>> plot_text3D((0, 0, 0), color="black", text='A')
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    if delta is None:
        delta = np.array([0.0, 0.0, 0.0])
    elif isinstance(delta, float):
        delta = np.array([delta, delta, delta])

    ax.text(pos[0]+delta[0], pos[1]+delta[1], pos[2]+delta[2], text, color=color, **kwargs)


def plot_point3d(pos, ax=None, color=None, text=None, **kwargs):
    """
    Plot 3D point

    Example:
    .. runblock:: pycon
        >>> from my_graphics import plot_arrow3d
        >>> plot_point3d((-2, 2, 2), (3, 4, 3), color='r', width=0.1)  # red arrow
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    ax.scatter(pos[0], pos[1], pos[2], color=color, **kwargs)
    plot_text3d(pos, delta=0.05, text=text, **kwargs)


def plot_arrow3d(start, end, ax=None, color=None, **kwargs):
    """
    Plot 3D arrow

    Example:
    .. runblock:: pycon
        >>> from my_graphics import plot_arrow3d
        >>> plot_arrow3d((-2, 2, 2), (3, 4, 3), color='r', width=0.1)  # red arrow
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    length = np.linalg.norm(end - start)

    ax.quiver(
        start[0],
        start[1],
        start[2],
        end[0] - start[0],
        end[1] - start[1],
        end[2] - start[2],
        color=color,
        arrow_length_ratio=(0.2 / length), 
        **kwargs
    )
    plot_point3d(start, color=color)



def plot_rot3d(
    T,
    ax=None,
    color=None,
    frame="",
    **kwargs,
):
    """
    Plot 3D rotation

    Example:
    ...runblock:: pycon
        >>> from my_graphics import plot_pose3d
        >>> from spatialmath import *
        >>> A = SO(3)
        >>> plot_rot3d(A, frame='A', color="blue");
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    o = T * np.array([0,0,0])
    x = T * np.array([1,0,0])
    y = T * np.array([0,1,0])
    z = T * np.array([0,0,1])

    o = o.flatten()
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()

    plot_point3d(o)    
    plot_text3d(o, text=r"$\{$"+f"{frame}"+r"$\}$", color=color, delta=-0.25, **kwargs)
    
    plot_arrow3d(o, x, color=color, **kwargs)
    plot_text3d(x, text="X"+r"$_"+f"{frame}"+r"$", color=color, delta=[+0.1, -0.1, -0.1], **kwargs)

    plot_arrow3d(o, y, color=color, **kwargs)
    plot_text3d(y, text="Y"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, +0.1, -0.1], **kwargs)

    plot_arrow3d(o, z, color=color, **kwargs)
    plot_text3d(z, text="Z"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, -0.1, +0.1], **kwargs)
  


def plot_pose3d(
    T,
    ax=None,
    color=None,
    frame="",
    **kwargs,
):
    """
    Plot 3D pose

    Example:
    ...runblock:: pycon
        >>> from my_graphics import plot_pose3d
        >>> from spatialmath import *
        >>> A = SE(3)
        >>> plot_pose3d(A, frame='A', color="blue");
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    o = T * np.array([0,0,0])
    x = T * np.array([1,0,0])
    y = T * np.array([0,1,0])
    z = T * np.array([0,0,1])

    o = o.flatten()
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()

    plot_point3d(o)    
    plot_text3d(o, text=r"$\{$"+f"{frame}"+r"$\}$", color=color, delta=-0.25, **kwargs)
    
    plot_arrow3d(o, x, color=color, **kwargs)
    plot_text3d(x, text="X"+r"$_"+f"{frame}"+r"$", color=color, delta=[+0.1, -0.1, -0.1], **kwargs)

    plot_arrow3d(o, y, color=color, **kwargs)
    plot_text3d(y, text="Y"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, +0.1, -0.1], **kwargs)

    plot_arrow3d(o, z, color=color, **kwargs)
    plot_text3d(z, text="Z"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, -0.1, +0.1], **kwargs)
  