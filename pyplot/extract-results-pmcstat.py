import re
import matplotlib.pyplot as plt

# Define the PerformanceMetrics class
class PerformanceMetrics:
    def __init__(self, l1d_tlb_rd, l2d_tlb_rd, l1d_tlb_refill, cpu_cycles, dtlb_walk, stall_backend, ll_cache_miss_rd):
        self.l1d_tlb_rd = l1d_tlb_rd
        self.l2d_tlb_rd = l2d_tlb_rd
        self.l1d_tlb_refill = l1d_tlb_refill
        self.cpu_cycles = cpu_cycles
        self.dtlb_walk = dtlb_walk
        self.stall_backend = stall_backend
        self.ll_cache_miss_rd = ll_cache_miss_rd

    def __repr__(self):
        return (f"PerformanceMetrics(l1d_tlb_rd={self.l1d_tlb_rd}, l2d_tlb_rd={self.l2d_tlb_rd}, "
                f"l1d_tlb_refill={self.l1d_tlb_refill}, cpu_cycles={self.cpu_cycles}, "
                f"dtlb_walk={self.dtlb_walk}, stall_backend={self.stall_backend}, "
                f"ll_cache_miss_rd={self.ll_cache_miss_rd})")

def extract_headers_and_values(input_text):
    lines = input_text.strip().split('\n')
    headers = re.split(r'\s+', lines[0].strip('#').strip())
    values = [list(map(int, re.split(r'\s+', line.strip()))) for line in lines[1:]]
    return headers, values

def create_performance_metrics(values):
    return [PerformanceMetrics(*value_set) for value_set in values]

def transpose_values(metrics):
    return list(zip(*[[
        metric.l1d_tlb_rd,
        metric.l2d_tlb_rd,
        metric.l1d_tlb_refill,
        metric.cpu_cycles,
        metric.dtlb_walk,
        metric.stall_backend,
        metric.ll_cache_miss_rd
    ] for metric in metrics]))

def plot_metrics(headers, transposed_values):
    num_metrics = len(headers)
    fig, axes = plt.subplots(num_metrics, 1, figsize=(12, 3*num_metrics), sharex=True)
    
    for i, (ax, header) in enumerate(zip(axes, headers)):
        ax.plot(transposed_values[i])
        ax.set_title(header)
        ax.set_ylabel('Value')
        ax.grid(True)
    
    plt.xlabel('Sample Index')
    plt.tight_layout()
    plt.show()

def main(input_text):
    headers, values = extract_headers_and_values(input_text)
    metrics = create_performance_metrics(values)
    for metric in metrics:
        print(metric)
    transposed_values = transpose_values(metrics)
    plot_metrics(headers, transposed_values)

# Input text
input_text = """# p/l1d_tlb_rd p/l2d_tlb_rd p/l1d_tlb_refill p/cpu_cycles p/dtlb_walk p/stall_backend p/ll_cache_miss_rd
             0            0                0            0           0               0                  0
    2337052346       141483           140443   4312946424      132736      1198102014            5435801
    1596637344        93704            57709   2911064777       53544       794993953            3666801"""

# Run the main function
main(input_text)