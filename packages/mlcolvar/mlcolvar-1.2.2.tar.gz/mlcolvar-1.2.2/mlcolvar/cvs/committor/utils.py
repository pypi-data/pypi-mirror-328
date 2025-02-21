import torch
import numpy as np
from typing import List
from mlcolvar.core.loss.committor_loss import SmartDerivatives, compute_descriptors_derivatives
from mlcolvar.data import DictDataset

__all__ = ["KolmogorovBias", "compute_committor_weights", "initialize_committor_masses"]

class KolmogorovBias(torch.nn.Module):
    """Wrappper class to compute the Kolmogorov bias $$V_K = -$$ from a committor model"""

    def __init__(self,
                 input_model : torch.nn.Module,
                 beta : float,
                 epsilon : float = 1e-6,
                 lambd : float = 1) -> None:
        """Compute Kolmogorov bias from a committor model

        Parameters
        ----------
        input_model : torch.nn.Module
            Model to compute the bias from
        beta: float
            Inverse temperature in the right energy units, i.e. 1/(k_B*T)
        epsilon : float, optional
            Regularization term in the logarithm, by default 1e-6
        lambd : float, optional
            Multiplicative term for the whole bias, by default 1
        """
        super().__init__()
        self.input_model = input_model
        self.beta = beta
        self.lambd = lambd
        if type(epsilon) is not torch.Tensor:
            epsilon = torch.Tensor([epsilon])
        self.epsilon = epsilon

    def forward(self, x):
        x.requires_grad = True
        q = self.input_model(x)
        grad_outputs = torch.ones_like(q)
        grads = torch.autograd.grad(q, x, grad_outputs, retain_graph=True)[0]
        grads_squared = torch.sum(torch.pow(grads, 2), 1)
        bias = - self.lambd*(1/self.beta)*(torch.log( grads_squared + self.epsilon ) - torch.log(self.epsilon))
        return bias

def compute_committor_weights(dataset, 
                              bias: torch.Tensor, 
                              data_groups: List[int], 
                              beta: float):
    """Utils to update a DictDataset object with the appropriate weights and labels for the training set for the learning of committor function.

    Parameters
    ----------
    dataset : 
        Labeled dataset containig data from different simulations, the labels must identify each of them. 
        For example, it can be created using `mlcolvar.utils.io.create_dataset_from_files(filenames=[file1, ..., fileN], ... , create_labels=True)`
    bias : torch.Tensor
        Bias values for the data in the dataset, usually it should be the committor-based bias
    data_groups : List[int]
        Indices specyfing the iteration each labeled data group belongs to. 
        Unbiased simulations in A and B used for the boundary conditions must have indices 0 and 1.
    beta : float
        Inverse temperature in the right energy units

    Returns
    -------
        Updated dataset with weights and updated labels
    """

    if bias.isnan().any():
        raise(ValueError('Found Nan(s) in bias tensor. Check before proceeding! If no bias was applied replace Nan with zero!'))
    
    n_labels = len(torch.unique(dataset['labels']))
    if n_labels != len(data_groups):
        raise(ValueError(f'The number of labels ({n_labels}) and data groups ({len(data_groups)}) do not match! Ensure you are correctly mapping the data in your training set!'))

    # TODO sign if not from committor bias
    weights = torch.exp(beta * bias)
    new_labels = torch.zeros_like(dataset['labels'])

    data_groups = torch.Tensor(data_groups)

    # correct data labels according to iteration
    for j,index in enumerate(data_groups):
        new_labels[torch.nonzero(dataset['labels'] == j, as_tuple=True)] = index

    for i in np.unique(data_groups):
        # compute average of exp(beta*V) on this simualtions
        coeff = 1 / torch.mean(weights[torch.nonzero(new_labels == i, as_tuple=True)])
        
        # update the weights
        weights[torch.nonzero(new_labels == i, as_tuple=True)] = coeff * weights[torch.nonzero(new_labels == i, as_tuple=True)]
    
    # update dataset
    dataset['weights'] = weights
    dataset['labels'] = new_labels

    return dataset

def initialize_committor_masses(atom_types: list, masses: list, n_dims: int = 3):
    """Initialize the masses tensor with the right shape for committor learning

    Parameters
    ----------
    atoms_map : list[int]
        List to map the atoms in the system to the corresponing types, which are specified with the masses keyword. e.g, for water [0, 1, 1]
    masses : list[float]
        List of masses of the different atom types in the system, e.g., for water [15.999, 1.008]
    n_dims : int
        Number of spatial dimensions, by default, 3
    Returns
    -------
    atomic_masses
        Atomic masses tensor ready to be used for committor learning.
    """
    if n_dims > 3:
        raise(ValueError(f"Number of dimension should be less than 3! Found {n_dims}"))
    
    # put number of atoms for each type and the corresponding atomic mass
    atom_types = np.array(atom_types)

    atomic_masses = []
    for i in range(len(atom_types)):
        # each mass has to be repeated for the number of dimensions
        for n in range(n_dims):
            atomic_masses.append(masses[atom_types[i]])

    # make it a tensor
    atomic_masses = torch.Tensor(atomic_masses)

    return atomic_masses

def get_descriptors_and_derivatives(dataset,
                                 descriptor_function, 
                                 n_atoms : int, 
                                 separate_boundary_dataset=True, 
                                 setup_device='cpu'):
    """Wrapper function to setup a faster calculation of derivatives computing only once the derivatives of descriptors wrt positions.

    Parameters
    ----------
    dataset : DictDataset
        Dataset to be updated. Dataset['data'] must be positions
    descriptor_function :
        Transform function to compute the descriptors from the positions.
    n_atoms : int
        Number of atoms in the system
    separate_boundary_dataset : bool, optional
        Switch to exculde boundary condition labeled data from the variational loss, by default True
    setup_device : str, optional
        Device on which to perform the expensive calculations. Either 'cpu' or 'cuda', by default 'cpu'
    
    Returns
    -------
    smart_derivatives : torch.nn.Module
        SmartDerivatives object for faster computation of derivatives.
    smart_dataset : DictDataset
        Updated dataset. Dataset['data'] are the computed descriptors
    """
    # apply preprocessing and compute derivatives of descriptors
    pos, desc, d_desc_d_x = compute_descriptors_derivatives(dataset=dataset, 
                                                            descriptor_function=descriptor_function, 
                                                            n_atoms=n_atoms, 
                                                            separate_boundary_dataset=separate_boundary_dataset)

  # this sets up the fixed part of the calculation of the derivatives
    smart_derivatives = SmartDerivatives(d_desc_d_x, 
                                        n_atoms=n_atoms, 
                                        setup_device=setup_device)

    # update dataset with the descriptors as data
    smart_dataset = DictDataset({'data' : desc.detach(), 
                                'labels': torch.clone(dataset['labels']), 
                                'weights' : torch.clone(dataset['weights'])})
    
    return smart_dataset, smart_derivatives