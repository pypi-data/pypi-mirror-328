from src.problem.abstract_problem import AbstractProblem
import numpy as np
import src.common as cm

class JobShop(AbstractProblem):
    """
    Represents the Job Shop Scheduling Problem (JSSP).
    
    This class models the JSSP by processing job scheduling data from a file
    and computing the makespan for a given sequence.
    """

    def __init__(self, file_path: str):
        """
        Initializes the Job Shop Scheduling Problem instance.
        
        Parameters
        ----------
        file_path : str
            Path to the input file containing job scheduling data.
        """
        self.num_jobs, self.num_machines, self.jobs_dic = self.parse_job_shop_file(file_path)
        super().__init__(gen_type=cm.GeneType.PERMUTATION, n_var=self.num_jobs, xl=[0], xu=[self.num_jobs - 1])

    @staticmethod
    def parse_job_shop_file(file_path):
       
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            parts = line.strip().split()
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                num_jobs, num_machines = int(parts[0]), int(parts[1])
                data_start_index = i + 1  
                break

        
        jobs_dic = {}

        
        for job_index, line in enumerate(lines[data_start_index:data_start_index + num_jobs]):
            job_data = list(map(int, line.strip().split()))
            operations = []
            for step in range(num_machines):
                machine = job_data[2 * step]  
                time = job_data[2 * step + 1]  
                operations.append((machine, time))  
            jobs_dic[job_index + 1] = operations  

        return num_jobs, num_machines, jobs_dic

    def f(self, schedule):
        """
        Computes the makespan for a given job shop scheduling sequence.
        
        Parameters:
            schedule (list): A permutation of job indices representing job execution order.
        
        Returns:
            int: The makespan of the given schedule.
        """
        completion_time = np.zeros((self.num_jobs, self.num_machines))
    
        for job_pos, job_index in enumerate(schedule):
            for machine_index, (machine, duration) in enumerate(self.jobs_dic[job_index]):
                if job_pos == 0 and machine_index == 0:
                    completion_time[job_pos, machine] = duration
                elif job_pos == 0:
                    completion_time[job_pos, machine] = completion_time[job_pos, machine_index - 1] + duration
                elif machine_index == 0:
                    completion_time[job_pos, machine] = completion_time[job_pos - 1, machine] + duration
                else:
                    completion_time[job_pos, machine] = max(completion_time[job_pos - 1, machine], completion_time[job_pos, machine_index - 1]) + duration

        job_index = np.where(schedule == schedule[-1])[0][0]
        return int(completion_time[job_index, self.num_machines - 1])
