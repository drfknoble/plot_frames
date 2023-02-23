# Copyright (c) 2023, drfknoble (Dr Frazer K. Noble)
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 


import matplotlib.pyplot as plt
import numpy as np

from spatialmath import *
from mpl_toolkits.mplot3d import Axes3D
  

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

    o = T * SO3([0,0,0])
    x = T * SO3([1,0,0])
    y = T * SO3([0,1,0])
    z = T * SO3([0,0,1])

    plot_point3d(o.t)    
    plot_text3d(o.t, text=r"$\{$"+f"{frame}"+r"$\}$", color=color, delta=-0.25, **kwargs)
    
    plot_arrow3d(o.t, x.t, color=color, **kwargs)
    plot_text3d(x.t, text="X"+r"$_"+f"{frame}"+r"$", color=color, delta=[+0.1, -0.1, -0.1], **kwargs)

    plot_arrow3d(o.t, y.t, color=color, **kwargs)
    plot_text3d(y.t, text="Y"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, +0.1, -0.1], **kwargs)

    plot_arrow3d(o.t, z.t, color=color, **kwargs)
    plot_text3d(z.t, text="Z"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, -0.1, +0.1], **kwargs)
  


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

    o = T * SE3([0,0,0])
    x = T * SE3([1,0,0])
    y = T * SE3([0,1,0])
    z = T * SE3([0,0,1])

    plot_point3d(o.t)    
    plot_text3d(o.t, text=r"$\{$"+f"{frame}"+r"$\}$", color=color, delta=-0.25, **kwargs)
    
    plot_arrow3d(o.t, x.t, color=color, **kwargs)
    plot_text3d(x.t, text="X"+r"$_"+f"{frame}"+r"$", color=color, delta=[+0.1, -0.1, -0.1], **kwargs)

    plot_arrow3d(o.t, y.t, color=color, **kwargs)
    plot_text3d(y.t, text="Y"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, +0.1, -0.1], **kwargs)

    plot_arrow3d(o.t, z.t, color=color, **kwargs)
    plot_text3d(z.t, text="Z"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, -0.1, +0.1], **kwargs)
  