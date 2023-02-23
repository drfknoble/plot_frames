# Copyright (c) 2023, drfknoble (Dr Frazer K. Noble)
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 


import matplotlib.pyplot as plt
import numpy as np

from spatialmath import *


def plot_text2d(pos, ax=None, color=None, delta=None, text=None, **kwargs):
    """
    Plot 2D text

    Example:
    .. runblock:: pycon
        >>> from my_graphics import plot_text2d
        >>> plot_text3D((0, 0), color="black", text='A')
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    if delta is None:
        delta = np.array([0.0, 0.0])
    elif isinstance(delta, float):
        delta = np.array([delta, delta])

    ax.text(pos[0]+delta[0], pos[1]+delta[1], text, color=color, **kwargs)



def plot_point2d(pos, ax=None, color=None, text=None, **kwargs):
    """
    Plot 2D point

    Example:
    .. runblock:: pycon
        >>> from my_graphics import plot_point2d
        >>> plot_point3d((-2, 2), (3, 4), color='r')
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    ax.scatter(pos[0], pos[1], color=color, **kwargs)
    plot_text2d(pos, delta=0.05, text=text, **kwargs)


def plot_arrow2d(start, end, ax=None, color=None, width=0.02, **kwargs):
    """
    Plot 2 arrow

    Example:
    .. runblock:: pycon
        >>> from my_graphics import plot_arrow2d
        >>> plot_arrow3d((-2, 2), (3, 4), color='r')
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    ax.arrow(
        start[0],
        start[1],
        end[0] - start[0],
        end[1] - start[1],
        color=color,
        length_includes_head=True,
        width=width,
        **kwargs
    )


def plot_pose2d(
    T,
    ax=None,
    color=None,
    frame="",
    **kwargs,
):
    """
    Plot 2D pose

    Example:
    ...runblock:: pycon
        >>> from my_graphics import plot_pose2d
        >>> from spatialmath import *
        >>> A = SE(2)
        >>> plot_pose3d(A, frame='A', color="blue")
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    o = T * SE2([0,0])
    x = T * SE2([1,0])
    y = T * SE2([0,1])

    plot_point2d(o.t, color=color)    
    plot_text2d(o.t, text=r"$\{$"+f"{frame}"+r"$\}$", color=color, delta=-0.25, **kwargs)
    
    plot_arrow2d(o.t, x.t, color=color, **kwargs)
    plot_text2d(x.t, text="X"+r"$_"+f"{frame}"+r"$", color=color, delta=[+0.1, -0.1, -0.1], **kwargs)

    plot_arrow2d(o.t, y.t, color=color, **kwargs)
    plot_text2d(y.t, text="Y"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, +0.1, -0.1], **kwargs)
