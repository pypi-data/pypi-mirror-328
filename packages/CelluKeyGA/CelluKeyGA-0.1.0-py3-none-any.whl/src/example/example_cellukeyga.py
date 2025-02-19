import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from mpmath import power as pw
from typing import List
from src.problem.job_shop_cellukeyga import *


from src.optimizer import cellukeyga
from src.problem.tsp_cellukeyga import *
from src.selection.tournament_selection_cellukeyga import TournamentSelection

from src.recombination.byte_one_point_crossover import ByteOnePointCrossover
from src.recombination.byte_uniform_crossover import ByteUniformCrossover
from src.mutation.byte_mutation_random import ByteMutationRandom
from src.mutation.byte_mutation import ByteMutation



def run_cga_example():

    # file_path = "src/benchmark/JSSP/Demirkol/cscmax_20_15_1.txt"  
    file_path = "src/benchmark/JSSP/instances/abz5.txt"  

    result = cellukeyga(
        n_cols=10,
        n_rows=10,
        n_gen=500,
        ch_size=10,
        p_crossover=1,
        p_mutation=0.9,
        problem=JobShop(file_path),
        selection=TournamentSelection,
        recombination=ByteUniformCrossover,
        mutation=ByteMutation,
        seed_par=100
    )

    # Print the results
    print("Best solution chromosome:", *(item for item in result.chromosome))
    print("Best fitness value:", result.fitness_value)

if __name__ == "__main__":
    run_cga_example()
