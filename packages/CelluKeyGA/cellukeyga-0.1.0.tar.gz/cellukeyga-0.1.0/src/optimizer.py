from src.byte_operators import * 
from src.population import *
from src.individual import *
from src.mutation.bit_flip_mutation import *
from src.selection.tournament_selection_cga import *
from src.recombination.one_point_crossover import *
from src.problem.abstract_problem import AbstractProblem
from dataclasses import dataclass
from typing import List
import src.common as cm
import numpy as np
import random


@dataclass
class Result:
    chromosome: List[float]
    fitness_value: float
    generation_found: int

def cga(
    n_cols: int,
    n_rows: int,
    n_gen: int,
    ch_size: int,
    p_crossover: float,
    p_mutation: float,
    problem: AbstractProblem,
    selection: SelectionOperator,
    recombination: RecombinationOperator,
    mutation: MutationOperator,
    seed_par: int = None
) -> Result:
    """
    Optimize the given problem using a genetic algorithm.

    Parameters
    ----------
    n_cols : int
        Number of columns in the population grid.
    n_rows : int
        Number of rows in the population grid.
    n_gen : int
        Number of generations to evolve.
    ch_size : int
        Size of the chromosome.
    gen_type : str
        Type of the genome representation (e.g., 'Binary', 'Permutation', 'Real').
    p_crossover : float
        Probability of crossover (between 0 and 1).
    p_mutation : float
        Probability of mutation (between 0 and 1).
    problem : AbstractProblem
        The problem instance used for fitness evaluation.
    selection : SelectionOperator
        Function or class used for selecting parents.
    recombination : RecombinationOperator
        Function or class used for recombination (crossover).
    mutation : MutationOperator
        Function or class used for mutation.
    mins : list[float]
        List of minimum values for each gene in the chromosome (for real value optimization).
    maxs : list[float]
        List of maximum values for each gene in the chromosome (for real value optimization).
    seed_par : int
        Ensures the random number generation is repeatable.

    Returns
    -------
    Result
        A Result object containing the best solution found, with its chromosome, fitness value, and generation.
    """

    if seed_par is not None:
        np.random.seed(seed_par)
        random.seed(seed_par)

    pop_size = n_cols * n_rows
    best_solutions = []
    best_objectives = []
    avg_objectives = []
    method_name = OptimizationMethod.CGA

    # Generate Initial Population
    pop_list = Population(
                method_name, 
                ch_size, 
                n_rows, 
                n_cols,
                gen_type = problem.gen_type, 
                problem = problem,
                mins = problem.xl,
                maxs = problem.xu).initial_population()

    pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)

    best_solutions.append(pop_list_ordered[0].chromosome)
    best_objectives.append(pop_list_ordered[0].fitness_value)
    
    best_ever_solution = Result(
        chromosome=[int(gene) for gene in pop_list_ordered[0].chromosome],
        fitness_value=pop_list_ordered[0].fitness_value,
        generation_found=0
    )

    mean = sum(ind.fitness_value for ind in pop_list) / len(pop_list)
    avg_objectives.append(mean)

    # Evolutionary Algorithm Loop
    generation = 1
    while generation != n_gen + 1:
        for c in range(pop_size):
            offsprings = []
            parents = selection(pop_list, c).get_parents()
            rnd = np.random.rand()

            if rnd < p_crossover:
                offsprings = recombination(parents, problem).get_recombinations()
            else:
                offsprings = parents

            for p in range(len(offsprings)):
                mutation_cand = offsprings[p]
                rnd = np.random.rand()

                if rnd < p_mutation:
                    mutated = mutation(mutation_cand, problem).mutate()
                    offsprings[p] = mutated

                # Replacement: Replace if better
                if offsprings[p].fitness_value < parents[p].fitness_value:
                    index = pop_list.index(parents[p])
                    pop_list[index] = offsprings[p]

        pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)
        best_solutions.append(pop_list_ordered[0].chromosome)
        best_objectives.append(pop_list_ordered[0].fitness_value)

        if pop_list_ordered[0].fitness_value < best_ever_solution.fitness_value:
            best_ever_solution = Result(
            chromosome=[int(gene) for gene in pop_list_ordered[0].chromosome], 
            fitness_value=pop_list_ordered[0].fitness_value,  
            generation_found=generation
            )

        mean = sum(ind.fitness_value for ind in pop_list) / len(pop_list)
        avg_objectives.append(mean)

        # Print progress (optional)
        print(
            f"{generation} - {best_ever_solution.chromosome} - {best_ever_solution.fitness_value}"
        )

        generation += 1
    
    return best_ever_solution


def cellukeyga(
    n_cols: int,
    n_rows: int,
    n_gen: int,
    ch_size: int,
    p_crossover: float,
    p_mutation: float,
    problem: AbstractProblem,
    selection: SelectionOperator,
    recombination: RecombinationOperator,
    mutation: MutationOperator,
    seed_par: int = None
) -> Result:
    """
    Optimize the given problem using a genetic algorithm.

    Parameters
    ----------
    n_cols : int
        Number of columns in the population grid.
    n_rows : int
        Number of rows in the population grid.
    n_gen : int
        Number of generations to evolve.
    ch_size : int
        Size of the chromosome.
    gen_type : str
        Type of the genome representation (e.g., 'Binary', 'Permutation', 'Real').
    p_crossover : float
        Probability of crossover (between 0 and 1).
    p_mutation : float
        Probability of mutation (between 0 and 1).
    problem : AbstractProblem
        The problem instance used for fitness evaluation.
    selection : SelectionOperator
        Function or class used for selecting parents.
    recombination : RecombinationOperator
        Function or class used for recombination (crossover).
    mutation : MutationOperator
        Function or class used for mutation.
    mins : list[float]
        List of minimum values for each gene in the chromosome (for real value optimization).
    maxs : list[float]
        List of maximum values for each gene in the chromosome (for real value optimization).
    seed_par : int
        Ensures the random number generation is repeatable.

    Returns
    -------
    Result
        A Result object containing the best solution found, with its chromosome, fitness value, and generation.
    """

    if seed_par is not None:
        np.random.seed(seed_par)
        random.seed(seed_par)

    pop_size = n_cols * n_rows
    best_solutions = []
    best_objectives = []
    avg_objectives = []
    method_name = OptimizationMethod.CGA

    # Generate Initial Population
    pop_list = Population(
                method_name, 
                ch_size, 
                n_rows, 
                n_cols,
                gen_type = problem.gen_type, 
                problem = problem,
                mins = problem.xl,
                maxs = problem.xu).initial_population()

    pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)

    best_solutions.append(pop_list_ordered[0].chromosome)
    best_objectives.append(pop_list_ordered[0].fitness_value)
    best_ever_solution = Result(
        chromosome=pop_list_ordered[0].chromosome,
        fitness_value=pop_list_ordered[0].fitness_value,
        generation_found=0
    )

    mean = sum(ind.fitness_value for ind in pop_list) / len(pop_list)
    avg_objectives.append(mean)

    # Evolutionary Algorithm Loop
    generation = 1
    while generation != n_gen + 1:
        for c in range(pop_size):
            offsprings = []
            parents = selection(pop_list, c).get_parents()
            rnd = np.random.rand()

            if rnd < p_crossover:
                offsprings = recombination(parents, problem).get_recombinations()
            else:
                offsprings = parents

            for p in range(len(offsprings)):
                mutation_cand = offsprings[p]
                rnd = np.random.rand()

                if rnd < p_mutation:
                    mutated = mutation(mutation_cand, problem).mutate()
                    offsprings[p] = mutated

                # Replacement: Replace if better
                if offsprings[p].fitness_value < parents[p].fitness_value:
                    index = pop_list.index(parents[p])
                    pop_list[index] = offsprings[p]

        pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)
        best_solutions.append(pop_list_ordered[0].chromosome)
        best_objectives.append(pop_list_ordered[0].fitness_value)

        if pop_list_ordered[0].fitness_value < best_ever_solution.fitness_value:
            ch_int_list = cm.decode(pop_list_ordered[0].chromosome)
            best_ever_solution = Result(
                chromosome=ch_int_list,
                fitness_value=pop_list_ordered[0].fitness_value,
                generation_found=generation
            )

        mean = sum(ind.fitness_value for ind in pop_list) / len(pop_list)
        avg_objectives.append(mean)

        # Print progress (optional)
        print(
            f"{generation} - {best_ever_solution.chromosome} - {best_ever_solution.fitness_value}"
        )

        generation += 1
    
    return best_ever_solution
