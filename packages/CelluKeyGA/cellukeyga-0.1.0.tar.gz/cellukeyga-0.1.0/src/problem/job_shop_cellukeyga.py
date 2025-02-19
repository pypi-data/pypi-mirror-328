from src.problem.abstract_problem import AbstractProblem
import numpy as np
import src.common as cm

class JobShop(AbstractProblem):
    """
    Represents the Job Shop Scheduling Problem (JSSP).
    
    This class models the JSSP by processing job scheduling data from a file
    and computing the makespan for a given sequence.
    
    Attributes
    ----------
    num_jobs : int
        The number of jobs in the scheduling problem.
    num_machines : int
        The number of machines available.
    processing_times : ndarray
        A matrix storing the processing times for each job on each machine.
    """

    def __init__(self, file_path: str):
        """
        Initializes the Job Shop Scheduling Problem instance.
        
        Parameters
        ----------
        file_path : str
            Path to the input file containing job scheduling data.
        """
        self.num_jobs, self.num_machines, self.processing_times = self.parse_job_shop_file(file_path)
        super().__init__(gen_type=cm.GeneType.REAL, n_var=self.num_jobs, xl=[0.00], xu=[1.00])

    @staticmethod
    def parse_job_shop_file(file_path):
        """
        Parses a job shop scheduling problem instance from a text file.
        
        Parameters:
            file_path (str): Path to the input file.
        
        Returns:
            tuple: (num_jobs, num_machines, processing_times)
        """
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            parts = line.strip().split()
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                num_jobs, num_machines = int(parts[0]), int(parts[1])
                data_start_index = i + 1
                break

        processing_times = np.zeros((num_jobs, num_machines), dtype=int)
        
        for job_index, line in enumerate(lines[data_start_index:data_start_index + num_jobs]):
            job_data = list(map(int, line.strip().split()))
            for step in range(num_machines):
                machine = job_data[2 * step]
                time = job_data[2 * step + 1]
                processing_times[job_index, machine] = time
        
        return num_jobs, num_machines, processing_times

    def f(self, schedule):
        """
        Computes the makespan for a given job shop scheduling sequence.
        
        Parameters:
            schedule (list): A permutation of job indices representing job execution order.
        
        Returns:
            int: The makespan of the given schedule.
        """
    # Decode chromosome values to integer values
        x = cm.decode(schedule)
        x_int= list (x)

        num_jobs, num_machines = self.processing_times.shape
        completion_time = np.zeros((num_jobs, num_machines))
        
        for job_pos, job_index in enumerate(x_int):
            for machine in range(num_machines):
                if job_pos == 0 and machine == 0:
                    completion_time[job_pos, machine] = self.processing_times[job_index-1, machine]
                elif job_pos == 0:
                    completion_time[job_pos, machine] = completion_time[job_pos, machine - 1] + self.processing_times[job_index-1, machine]
                elif machine == 0:
                    completion_time[job_pos, machine] = completion_time[job_pos - 1, machine] + self.processing_times[job_index-1, machine]
                else:
                    completion_time[job_pos, machine] = max(completion_time[job_pos - 1, machine], completion_time[job_pos, machine - 1]) + self.processing_times[job_index-1, machine]
        
        return int(completion_time[x_int.index(x_int[-1]), num_machines - 1])
