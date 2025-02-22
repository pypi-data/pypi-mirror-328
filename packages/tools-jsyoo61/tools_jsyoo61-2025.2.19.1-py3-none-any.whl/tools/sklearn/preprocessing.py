from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

from .. import numpy as tnumpy

def standardize(x, scaler=None):
    """
    Standardize (z-score/gaussian normalization) x without having to make a StandardScaler() object.

    Parameters
    ----------
    x : ndarray of shape (n_observation, n_channel) or (n_batch, n_observation, n_channel)
        data to be standardized.
        if x.ndim==3, then the first 2 dimensions are collapsed to standardize then resized to original shape
    scaler: sklearn.preprocessing.StandardScaler(), default=None
        scaler to use (that has already fit())

    Returns
    -------
    x_standardized : ndarray of shape (n_observation, n_channel) or (n_batch, n_observation, n_channel)
        Normalized data
    scaler : sklearn.preprocessing.StandardScaler()
        Scaler used for normalization
    """
    squeezer = tnumpy.Squeezer()
    x = squeezer.squeeze(x)

    if scaler is None:
        scaler = StandardScaler()
        x_standardized = scaler.fit_transform(x)
    else:
        x_standardized = scaler.transform(x)
    
    x_standardized = squeezer.unsqueeze(x_standardized)
        
    return x_standardized, scaler

def project_pca(x, var_threshold=None, n_pc=None, solver=None, random_state=0):
    """
    Standardize (z-score/gaussian normalization) x without having to make a StandardScaler() object.

    Parameters
    ----------
    x : ndarray of shape (n_observation, n_channel) or (n_batch, n_observation, n_channel)
        data to be standardized.
        if x.ndim==3, then the first 2 dimensions are collapsed to standardize then resized to original shape
    solver: sklearn.decomposition.PCA(), default=None
        solver to use (that has already fit())

    Returns
    -------
    x_projected : ndarray of shape (n_observation, n_channel) or (n_batch, n_observation, n_channel)
        Normalized data
    solver : sklearn.decomposition.PCA()
        Solver used for PCA projection
    """
    assert (var_threshold is None) ^ (n_pc is None), 'Only one of var_threshold or n_pc must be specified'

    squeezer = tnumpy.Squeezer()
    x = squeezer.squeeze(x)

    # If svd_solver is not full, result is random
    if solver is None:
        solver = PCA(svd_solver='full', random_state=random_state)
        x_pc = solver.fit_transform(x)
    else:
        x_pc = solver.transform(x)

    if var_threshold is not None:
        n_pc = np.argmax(np.cumsum(solver.explained_variance_ratio_) > var_threshold) + 1
    elif n_pc is not None:
        pass
    x_pc = x_pc[:n_pc] # (n_neurons, n_samples*n_time)

    x_pc = squeezer.unsqueeze(x_pc)
    return x_pc, solver

