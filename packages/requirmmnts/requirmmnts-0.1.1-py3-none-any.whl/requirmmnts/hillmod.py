def hill(func, start_x, start_y, step):
    cx, cy = start_x, start_y
    cv = func(cx, cy)

    for _ in range(1000):
         
        np1 = (cx + step, cy)
        npv1 = func(*np1)

        np2 = (cx - step, cy)
        npv2 = func(*np2)

        np3 = (cx, cy + step)
        npv3 = func(*np3)

        np4 = (cx, cy - step)
        npv4 = func(*np4)

        # Find the best move
        neighbors = [(np1, npv1), (np2, npv2), (np3, npv3), (np4, npv4)]
        best_point, best_value = max(neighbors, key=lambda x: x[1])

        if best_value > cv:
            cx, cy = best_point
            cv = best_value
        else:
            break   
    
    return cx, cy, cv


 
expr = input("Enter function in terms of x and y: ")  
func = lambda x, y: eval(expr)

x_start = float(input("Enter starting x: "))
y_start = float(input("Enter starting y: "))

max_x, max_y, max_val = hill(func, x_start, y_start, 0.01)

print("Max position at (", max_x, ",", max_y, ")")
print("Max value at", max_val)
