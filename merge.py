import heapq
import matplotlib.pyplot as plt
import time
import numpy as np

# Function to merge sorted lists and calculate cost
def merge_sorted_lists(list_sizes):
    heap = list(list_sizes)
    heapq.heapify(heap)
    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        cost = first + second
        total_cost += cost
        heapq.heappush(heap, cost)

    return total_cost

# Experimental Analysis
input_sizes = [10, 100, 1000, 10000, 100000]
experimental_times = []

def generate_list_sizes(n):
    return np.random.randint(1, 100, size=n)

for n in input_sizes:
    list_sizes = generate_list_sizes(n)
    start_time = time.time()
    merge_sorted_lists(list_sizes)
    end_time = time.time()
    experimental_times.append((end_time - start_time) * 1e6)  # Convert to microseconds

# Theoretical Analysis (Scaling)
theoretical_values = [n * np.log2(n) for n in input_sizes]  # Approximate cost for merging sorted lists
scaling_constant = sum(experimental_times) / sum(theoretical_values) 
print(scaling_constant) # Calculate scaling constant based on experimental data
theoretical_scaled_values = [v * scaling_constant for v in theoretical_values]

# Output Numerical Data
print("\nInput Size\tExperimental Time (microseconds)\tTheoretical Scaled Time (microseconds)")
for i in range(len(input_sizes)):
    print(f"{input_sizes[i]}\t\t{experimental_times[i]:.2f}\t\t\t\t{theoretical_scaled_values[i]:.2f}")

# Graph
plt.plot(input_sizes, experimental_times, label='Experimental Time', marker='o')
plt.plot(input_sizes, theoretical_scaled_values, label='Theoretical Scaled Time', marker='x')
plt.xlabel('Input Size')
plt.ylabel('Time (microseconds)')
plt.title('Experimental vs Theoretical Scaled Time for Merging Sorted Lists')
plt.legend()
plt.grid(True)
plt.show()
