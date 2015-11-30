# -*- coding: utf-8 -*-


"""
SSD 2016 plot script
"""

import pickle

import pylab as pl
import numpy as np
from IPython import embed as IPS
import symb_tools as st
import sympy


fname = "nb2_sim_res1.pcl"
with open(fname) as pfile:
    C = pickle.load(pfile)


t = list(C.xyt_traj.s)[0]
xyt_traj_func = st.expr_to_func(t, C.xyt_traj)
X, Y, x1, x2, x3, x4, x5, x6, VP = C.res.T


X_ref, Y_ref = xyt_traj_func(C.tt)[:, :2].T


mm = 1./25.4 #mm to inch
scale = 2
fs = [75*mm*scale, 35*mm*scale]
pl.rcParams['figure.subplot.bottom']=.2
pl.rcParams['legend.fontsize']='medium'

fnts = 12


labels = list('abcdefg')

def figlabel():
    s = labels.pop(0)
    pl.text(0.04, 0.85, s+')', transform=pl.gca().transAxes, fontsize=fnts)

#IPS()

print "Plotting simulation results from ", C.timestamp

ax = pl.figure(figsize=fs)
pl.plot(X_ref, Y_ref, 'k--', label='reference path')
pl.plot(X, Y, 'k', label='simulation')
pl.xlabel('$x$ in m')
pl.ylabel('$y$ in m')
pl.axis('equal')
pl.axis([-.1, 2.1, -.1, 1.17])
pl.legend(loc='lower right')
figlabel()


pl.savefig('plots/xy.pdf')

if 1:
    pl.figure(figsize=fs)
    pl.plot(C.tt, X_ref, 'k--')
    pl.plot(C.tt, X, 'k')
    pl.xlabel('$t$ in s')
    pl.ylabel('$x$ in m')
    #pl.text(0.1, 0.8, 'b)', transform=pl.gca().transAxes, fontsize=fnts)
    figlabel()
    pl.savefig('plots/xt.pdf')

    pl.figure(figsize=fs)
    pl.plot(C.tt, Y_ref, 'k--')
    pl.plot(C.tt, Y, 'k')
    pl.xlabel('$t$ in s')
    pl.ylabel('$y$ in m')
    pl.axis([0, C.tt[-1], -.1, 1.17])
    figlabel()
    pl.savefig('plots/yt.pdf')

    pl.figure(figsize=fs)
    pl.plot(C.tt, C.tt*0, 'k--')
    pl.plot(C.tt, x3/np.pi*180, 'k')
    pl.xlabel('$t$ in s')
    pl.ylabel('$\\alpha$ in deg')
    pl.axis([0, C.tt[-1], -9, 8.8])
    figlabel()
    pl.savefig('plots/alpha_t.pdf')

pl.show()
