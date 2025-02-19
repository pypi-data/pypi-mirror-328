import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.optimizer import cga
from src.recombination.pmx_crossover import PMXCrossover
from src.mutation.shuffle_mutation import ShuffleMutation
from src.mutation.swap_mutation import SwapMutation
from src.selection.tournament_selection_cga import TournamentSelection
from src.selection.roulette_wheel_selection import RouletteWheelSelection
from src.problem.tsp import *
from src.problem.job_shop import *


def run_cga_example():

    # file_path = "src/benchmark/JSSP/Demirkol/cscmax_20_15_1.txt"  
    file_path = "src/benchmark/JSSP/instances/abz5.txt"  

    result = cga(
        n_cols=15,
        n_rows=15,
        n_gen=500,
        ch_size=10,
        p_crossover=1,
        p_mutation=0.9,
        problem=JobShop(file_path),
        selection=TournamentSelection,
        recombination=PMXCrossover,
        mutation=SwapMutation,
        seed_par=100
    )

    # Print the results
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)

if __name__ == "__main__":
    run_cga_example()
