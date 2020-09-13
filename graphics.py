# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D, proj3d
from unitary_calculus import coord_ind, coord_corr

from init import *


# Class to draw vectors in 2D
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


# Graphical represenation of individuals
def graph_ind(result_data, indiv_noms, nb_dim, liste_pct):
    coord = coord_ind(result_data)

    # Check the number of desired dimensions (if 3 -> 3D graph, else 2D)
    if (nb_dim == 3):
        fig = plt.figure()

        # Parameters of the graphcial window
        graph3d = fig.add_subplot(
            111,
            projection='3d',
            title='Coordinates of the individuals in the new base',
            xlabel='Dim 1 ({}%)'.format(str(liste_pct[0])),
            ylabel='Dim 2 ({}%)'.format(str(liste_pct[1])),
            zlabel='Dim 3 ({}%)'.format(str(liste_pct[2]))
        )

        graph3d.scatter(
            xs=coord[0],
            ys=coord[1],
            zs=coord[2],
            zdir='z',
            marker='o',
            s=50
        )

        # Legend points with individuals' names
        for label, i, j, k in zip(indiv_noms, coord[0], coord[1], coord[2]):
            graph3d.text(s=label, x=i, y=j, z=k)
    else:
        # Only take nb_dim-1 (so 1) dimensions because the 1st dimension is not
        # represented with herself
        fig = [plt.figure() for k in range(nb_dim-1)]

        for k in range(nb_dim-1):
            # Determine the bounds of the graph
            lim_x = max(abs(min(coord[0])), abs(max(coord[0])))
            lim_y = max(abs(min(coord[k+1])), abs(max(coord[k+1])))

            # Parameters of the graphical window
            rep2d = fig[k].add_subplot(
                111,
                title='Coordinates of the individuals in the new base',
                xlabel='Dim 1 ({}%)'.format(str(liste_pct[0])),
                ylabel='Dim {} ({}%)'.format(str(k+2), str(liste_pct[k+1])),
                xlim=[-lim_x*1.05, lim_x*1.05],
                ylim=[-lim_y*1.1, lim_y*1.1]
            )

            rep2d.scatter(x=coord[0], y=coord[k+1], marker='o', s=50)

            # Legend points with individuals' names
            for label, i, j in zip(indiv_noms, coord[0], coord[k+1]):
                rep2d.annotate(
                    s=label,
                    xy=(i, j),
                    xytext=(-10, 10),
                    textcoords='offset points'
                )

            # Puts axes on the figure
            ax = fig[k].gca()
            ax.spines['right'].set_position(('data', 0))
            ax.spines['top'].set_position(('data', 0))
            ax.xaxis.set_ticks_position('top')
            ax.yaxis.set_ticks_position('right')
            rep2d.grid()

    return fig


# Graphical representation of the correlation circle
def cercle_corr(result_data, old_data, var_noms, nb_dim, liste_pct):
    projv = coord_corr(result_data, old_data)

    # Check the number of desired dimensions (if 3 -> 3D graph, else 2D)
    if (nb_dim == 3):
        fig = plt.figure()

        # Parameters of the graphical window
        sphere = fig.add_subplot(
            111,
            projection='3d',
            title='Sphère de corrélation des variables avec les composantes',
            xlabel='Dim 1 ({}%)'.format(str(liste_pct[0])),
            ylabel='Dim 2 ({}%)'.format(str(liste_pct[1])),
            zlabel='Dim 3 ({}%)'.format(str(liste_pct[2]))
        )

        sphere.scatter(
            xs=projv[0],
            ys=projv[1],
            zs=projv[2],
            zdir='z',
            marker='o',
            s=50
        )

        # Legend points with variables' names
        for label, i, j, k in zip(var_noms, projv[0], projv[1], projv[2]):
            sphere.text(s=label, x=i, y=j, z=k)
            # 3D vector from the origin to the variable
            a = Arrow3D(
                xs=[0, i],
                ys=[0, j],
                zs=[0, k],
                mutation_scale=20,
                lw=1,
                arrowstyle='-|>',
                color='k'
            )
            sphere.add_artist(a)  # Draw the vector

        # Parameters and drawing of the sphere
        theta, phi = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x = np.sin(phi)*np.cos(theta)
        y = np.sin(phi)*np.sin(theta)
        z = np.cos(phi)
        sphere.plot_wireframe(x, y, z, color='g')
    else:
        fig = [plt.figure() for k in range(nb_dim-1)]

        for k in range(nb_dim-1):
            circle = fig[k].add_subplot(
                111,
                title='Correlation circle of the variables/components',
                xlabel='Dim 1 ({}%)'.format(str(liste_pct[0])),
                ylabel='Dim {} ({}%)'.format(str(k+2), str(liste_pct[k+1]))
            )

            circle.plot(projv[0], projv[k+1], 'ko')

            for label, i, j in zip(var_noms, projv[0], projv[k+1]):
                circle.annotate(
                    s=label,
                    xy=(i, j),
                    xytext=(-10, 10),
                    textcoords='offset points'
                )
                # 2D vector from the origin to the variable
                circle.arrow(
                    x=0, y=0,
                    dx=i, dy=j,
                    head_width=0.05, head_length=0.05,
                    fc='k', ec='k')

            # Circle's parameters
            theta = np.linspace(0, 2*np.pi, 100)
            c1 = np.cos(theta)
            c2 = np.sin(theta)

            # Draw the circle and puts axes
            ax = fig[k].gca()
            ax.spines['right'].set_position(('data', 0))
            ax.spines['top'].set_position(('data', 0))
            ax.xaxis.set_ticks_position('top')
            ax.yaxis.set_ticks_position('right')
            circle.plot(c1, c2, 'k')
            circle.axis('equal')
            circle.grid()

    return fig


def graph(result_data, old_data, nb_dim, liste_pct, indiv_noms, var_noms):

    fig_indiv = graph_ind(result_data, indiv_noms, nb_dim, liste_pct)

    fig_cercle_corr = cercle_corr(
        result_data, old_data, var_noms, nb_dim, liste_pct)

    plt.show()
