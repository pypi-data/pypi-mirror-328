Min = -1000
Max = 1000

def min_max(d, ni, a, b, v, m, path):
    if d == 3:
        return v[ni], path + [ni]
    
    if m:  # Maximizing player
        best = Min
        best_path = []
        for i in range(2):
            val, p = min_max(d + 1, ni * 2 + i, a, b, v, False, path + [ni])
            if val > best:
                best = val
                best_path = p
            a = max(a, best)
            if a >= b:
                break  # Beta cutoff
        
        return best, best_path
    
    else:  # Minimizing player
        best = Max
        best_path = []
        for i in range(2):
            val, p = min_max(d + 1, ni * 2 + i, a, b, v, True, path + [ni])
            if val < best:
                best = val
                best_path = p
            b = min(b, best)
            if a >= b:
                break  # Alpha cutoff
        
        return best, best_path

values = [1,2,3,45,6,1,3,7]
opt, path = min_max(0, 0, Min, Max, values, True, [])

print("Optimal value is:", opt)
print("Path to optimal value:", path)
