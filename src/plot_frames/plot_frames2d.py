# Copyright (c) 2023, drfknoble (Dr Frazer K. Noble)
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 


import matplotlib.pyplot as plt
import numpy as np

from spatialmath import *

def new_plot2d(dims=None, labels=None, steps=None, **kwargs):
    """
    Create new 2D plot

    Example:
    .. runblock:: pycon
        >>> from plot_frames import new_plot2d
        >>> new_plot2d(dims=[-2,2])
    """

    if dims is None:
        dims = [-2, 2]

    if labels is None:
        labels = ['X', 'Y']

    if steps is None:
        steps = 1.0

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot()
    ax.set_facecolor("white")
    ax.set_xlim(dims)
    ax.set_ylim(dims)
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.grid(True)
    ax.set_xticks(np.arange(min(dims), max(dims)+1, steps))
    ax.set_yticks(np.arange(min(dims), max(dims)+1, steps))
   
    return fig, ax


def plot_text2d(pos, text, ax=None, color=None, delta=None, **kwargs):
    """
    Plot 2D text

    Example:
    .. runblock:: pycon
        >>> from plot_frames import plot_text2d
        >>> plot_text2d((0, 0), color="black", text='A')
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
        >>> from plot_frames import plot_point2d
        >>> plot_point3d((-2, 2), (3, 4), color='r')
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    ax.scatter(pos[0], pos[1], color=color, **kwargs)
    plot_text2d(pos, delta=0.05, text=text, **kwargs)


def plot_arrow2d(start, end, ax=None, color=None, width=None, **kwargs):
    """
    Plot 2D arrow

    Example:
    .. runblock:: pycon
        >>> from plot_frames import plot_arrow2d
        >>> plot_arrow2d((-2, 2), (3, 4), color="red")
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    if width is None:
        width = 0.02

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


def plot_rot2d(T, ax=None, color=None, frame="", **kwargs):
    """
    Plot 2D rotation

    Example:
    ...runblock:: pycon
        >>> from plot_frames import plot_pose2d
        >>> from spatialmath import *
        >>> A = SO(2)
        >>> plot_rot2d(A, frame='A', color="blue")
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    o = T * np.array([0,0])
    x = T * np.array([1,0])
    y = T * np.array([0,1])

    o = o.flatten()
    x = x.flatten()
    y = y.flatten()

    plot_point2d(o, color=color, **kwargs)    
    plot_text2d(o, text=r"$\{$"+f"{frame}"+r"$\}$", color=color, delta=-0.25, **kwargs)
    
    plot_arrow2d(o, x, color=color, **kwargs)
    plot_text2d(x, text="X"+r"$_"+f"{frame}"+r"$", color=color, delta=[+0.1, -0.1, -0.1], **kwargs)

    plot_arrow2d(o, y, color=color, **kwargs)
    plot_text2d(y, text="Y"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, +0.1, -0.1], **kwargs)



def plot_pose2d(T, ax=None, color=None, frame="", **kwargs):
    """
    Plot 2D pose

    Example:
    ...runblock:: pycon
        >>> from plot_frames import plot_pose2d
        >>> from spatialmath import *
        >>> A = SE(2)
        >>> plot_pose2d(A, frame='A', color="blue")
    """

    if ax is None:
        ax = plt.gca()

    if color is None:
        color = "black"

    o = T * np.array([0,0])
    x = T * np.array([1,0])
    y = T * np.array([0,1])

    o = o.flatten()
    x = x.flatten()
    y = y.flatten()

    plot_point2d(o, color=color, **kwargs)    
    plot_text2d(o, text=r"$\{$"+f"{frame}"+r"$\}$", color=color, delta=-0.25, **kwargs)
    
    plot_arrow2d(o, x, color=color, **kwargs)
    plot_text2d(x, text="X"+r"$_"+f"{frame}"+r"$", color=color, delta=[+0.1, -0.1, -0.1], **kwargs)

    plot_arrow2d(o, y, color=color, **kwargs)
    plot_text2d(y, text="Y"+r"$_"+f"{frame}"+r"$", color=color, delta=[-0.1, +0.1, -0.1], **kwargs)
