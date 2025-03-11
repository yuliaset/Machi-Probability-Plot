import math
import matplotlib.pyplot as plt

R_initial = 70
n_initial = 8

def P_k_correct(R, n, k):
    cumulative_p = 0.0
    prod = 1.0  
    for i in range(k):
        current_R = R - 4 * i
        if current_R < 4:
            break
        
        win_prob = n / current_R
        
        cumulative_p += prod * win_prob
        
        denom = math.comb(current_R - 1, 3)
        if current_R - 1 - n < 3:
            numerator = 0
        else:
            numerator = math.comb(current_R - 1 - n, 3)
        Q = (1 - win_prob) * (numerator / denom)
        
        prod *= Q
        
    return cumulative_p

max_cycles = R_initial // 4

cycles = list(range(max_cycles + 1))
P_values_correct = [P_k_correct(R_initial, n_initial, k) for k in cycles]

print("Cumulative win probabilities per cycle:")
for k, p in zip(cycles, P_values_correct):
    print(f"Cycle {k}: {p}")

P_one_draw = n_initial / R_initial

plt.figure(figsize=(8, 5))
plt.plot(cycles, P_values_correct, marker='o', linestyle='-', label='Win probability $P_k(70,8)$')
plt.title('Draw Probability vs. Number of Cycles')
plt.axhline(P_one_draw, color='red', linestyle='--', label=f'Single Draw: {P_one_draw:.2f}')
plt.xlabel('Number of cycles (k)')
plt.ylabel('Probability')
plt.xticks(cycles)
plt.legend()
plt.grid(True)
plt.savefig('graph.png')
plt.show()
