from typing import List
import numpy.random as randomgenerator

from src.individual import *
from src.problem.abstract_problem import AbstractProblem
from src.recombination.recombination_operator import RecombinationOperator

class UniformCrossover(RecombinationOperator):
    """
    UniformCrossover performs a uniform crossover on a pair of parent individuals
    to produce offspring individuals.

    Parameters
    ----------
    parents : list
        A list containing two parent individuals.
    problem : AbstractProblem
        The problem instance that provides the fitness function.
    """

    def __init__(self, parents: list, problem: AbstractProblem):
        """
        Initialize the UniformCrossover object.

        Parameters
        ----------
        parents : list
            A list containing two parent individuals.
        problem : AbstractProblem
            The problem instance that provides the fitness function.
        """
        self.parents = parents
        self.problem = problem

    def combine(self, p1: Individual, p2: Individual, locationsource: Individual) -> Individual:
        """
        Combine two parent individuals using uniform crossover to produce a single offspring.

        Parameters
        ----------
        p1 : Individual
            The first parent individual.
        p2 : Individual
            The second parent individual.
        locationsource : Individual
            The individual from which to copy positional information for the offspring.

        Returns
        -------
        Individual
            The resulting offspring individual.
        """
        chsize = len(p1.chromosome)
        child = [0 for i in range(chsize)]
        for i in range(chsize):
            if randomgenerator.rand() < 0.5:
                child[i] = p1.chromosome[i]
            else:
                child[i] = p2.chromosome[i]

        indv = Individual(p1.gen_type, p1.ch_size)
        indv.position = locationsource.position
        indv.neighbors_positions = locationsource.neighbors_positions
        indv.chromosome = list(child)
        indv.fitness_value = self.problem.f(child)
        return indv

    def get_recombinations(self) -> List[Individual]:
        """
        Perform the uniform crossover on the parent individuals to produce offspring.

        Returns
        -------
        List[Individual]
            A list containing the offspring individuals.
        """
        p1 = self.parents[0]
        p2 = self.parents[1]

        return [
            self.combine(p1, p2, p1),
            self.combine(p1, p2, p2)
        ]
