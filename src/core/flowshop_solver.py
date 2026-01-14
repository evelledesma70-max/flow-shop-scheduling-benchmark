from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

class FlowShopSolver(ABC):
    """
    Clase base abstracta para algoritmos de Flow Shop Scheduling
    """

    def __init__(self, times: Dict[int, List[float]]):
        self.times = times
        self.job_ids = list(times.keys())
        self.n_jobs = len(times)
        self.n_machines = 4
        self.best_sequence = None
        self.best_makespan = float('inf')
        self.best_completion_times = None
        self.execution_time = 0

    def evaluate_sequence(self, sequence: List[int]) -> Tuple[float, List[float]]:
        n = len(sequence)
        m = self.n_machines
        C = [[0] * m for _ in range(n)]

        C[0][0] = self.times[sequence[0]][0]
        for j in range(1, m):
            C[0][j] = C[0][j-1] + self.times[sequence[0]][j]

        for i in range(1, n):
            C[i][0] = C[i-1][0] + self.times[sequence[i]][0]
            for j in range(1, m):
                C[i][j] = max(C[i-1][j], C[i][j-1]) + self.times[sequence[i]][j]

        completion_times = [C[i][m-1] for i in range(n)]
        return completion_times[-1], completion_times

    def calculate_metrics(self, completion_times, makespan):
        avg_flow_time = sum(completion_times) / len(completion_times)
        throughput = len(completion_times) / makespan
        return avg_flow_time, throughput

    @abstractmethod
    def solve(self):
        pass
