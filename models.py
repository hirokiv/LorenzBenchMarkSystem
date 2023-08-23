import numpy as np
import matplotlib.pyplot as plt
# nominal Lorenz attractor
# Originally Fetched from https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html

# shift Lorenz model by w in z axis depending on the regime
def lorenz(xyz, *, s=10, r=28, b=2.667, w=0, sigma_z=0):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Point of interest in three-dimensional space.
    s, r, b : float
       Parameters defining the Lorenz attractor.
    w : float
       swithcing behavior along z axis
    sigma_z : float
       random normal obs noise scale

    Returns
    -------
    xyz_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    x, y, z = xyz

    # Add observation noise in z direction
    z_obs = z + float(np.random.normal(loc=0, scale=sigma_z, size=1))

    x_dot = s*(y - x)
    y_dot = x * (r- z_obs + w) - y 
    z_dot = x*y - b*(z_obs - w)
    return np.array([x_dot, y_dot, z_dot])

# component-wise view 
def Plot_components_regime( dt, num_steps, xyzs, regime, figsize=(14,3)):
  fig = plt.figure(figsize=figsize)
  ax1 = fig.add_subplot(4,1,1)
  ax1.plot(dt * np.arange(num_steps+1), list([*xyzs.T[0]]), lw=0.5)
  ax1.set_ylabel("X")
  ax1.set_xlabel("Time")
  ax2 = fig.add_subplot(4,1,2)
  ax2.plot(dt * np.arange(num_steps+1), list([*xyzs.T[1]]), lw=0.5)
  ax2.set_ylabel("Y")
  ax2.set_xlabel("Time")
  ax3 = fig.add_subplot(4,1,3)
  ax3.plot(dt * np.arange(num_steps+1), list([*xyzs.T[2]]), lw=0.5)
  ax3.set_ylabel("Z")
  ax3.set_xlabel("Time")
  ax3 = fig.add_subplot(4,1,4)
  ax3.plot(dt * np.arange(num_steps+1), regime, lw=0.5)
  ax3.set_ylabel("Regime")
  ax3.set_xlabel("Time")
  plt.show()


def Plot3D_attractor_view(xyzs):
    # Plot attractor
    ax = plt.figure().add_subplot(projection='3d')
    
    ax.plot(*xyzs.T, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.show()
    