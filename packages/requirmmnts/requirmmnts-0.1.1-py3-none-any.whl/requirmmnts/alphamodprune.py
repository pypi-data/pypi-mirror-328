MAX, MIN = 1000, -1000

pruned_nodes = []  # List to store pruned node indices

def minmax(depth, nodeIndex, maximizing_player, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizing_player:
        best = MIN
        for i in range(0, 2):
            val = minmax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                pruned_nodes.append(nodeIndex * 2 + i + 1)  # Store pruned node index
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = minmax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                pruned_nodes.append(nodeIndex * 2 + i + 1)  # Store pruned node index
                break
        return best

if __name__ == '__main__':
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    optimal_value = minmax(0, 0, True, values, MIN, MAX)
    print("The optimal value is", optimal_value)
    print("Pruned node indices:", pruned_nodes)
