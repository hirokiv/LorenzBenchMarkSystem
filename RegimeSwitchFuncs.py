import numpy as np
from scipy import integrate
import random
import matplotlib.pyplot as plt

def SwitchProb(xyz, t_lastswitched, t, const):
    alpha = const['alpha']
    R2 = const['R2']
    tau = const['tau']
    x,y,z = xyz
    t_elapsed = t - t_lastswitched # costant since the last swithced time
    r2 = x*x + y*y

    dTdt = lambda tdash : alpha * np.exp(- r2 / R2 - (t - tdash) / tau )
    
    prob, error = integrate.quad(dTdt, 0, t_elapsed)
    return prob, r2, t_elapsed

def RegimeSwitch(preregime, probability, lastswitched_idx, i):
    # assume regime swithcing between 2

    if random.random() < probability:
        lastswitched_idx = i
        if preregime == 0:
            regime = 1
        else:
            regime = 0
    else:
        regime = preregime

    return regime, lastswitched_idx

def Plot_SwitchingBehavior(dt, num_steps, prob, r2, t_elapsed, switch_const, figsize=(14,3)):
    # Plot swithcing probability
    fig = plt.figure(figsize=figsize)
    ax1 = fig.add_subplot(3,1,1)
    ax1.plot(dt * np.arange(num_steps+1), prob, lw=0.5)
    ax1.set_ylabel("probability")
    ax1.set_xlabel("Time")
    ax2 = fig.add_subplot(3,1,2)
    ax2.plot(dt * np.arange(num_steps+1), r2 / switch_const['R2'], lw=0.5)
    ax2.set_ylabel("r2/R2")
    ax2.set_xlabel("Time")
    ax3 = fig.add_subplot(3,1,3)
    ax3.plot(dt * np.arange(num_steps+1), t_elapsed / switch_const['tau'], lw=0.5)
    ax3.set_ylabel("dt / tau")
    ax3.set_xlabel("Time")
    plt.show()
     