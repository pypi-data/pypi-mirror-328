from enum import Enum 
import numpy as np
class GeneType(Enum):
    """
    GeneType is an enumeration class that represents the type of genome representation for an individual in an evolutionary algorithm.
    The three types of genome representation are BINARY, PERMUTATION, and REAL.
    """
    BINARY = 1
    PERMUTATION = 2
    REAL = 3


def encode (int_ch:int) -> list:

    real_chromosome =[]

    integer_chromoseme =[]

    return real_chromosome

def decode(real_ch:list)-> np.ndarray:
        # Decode chromosome values to integer values
        return np.argsort(real_ch) + 1