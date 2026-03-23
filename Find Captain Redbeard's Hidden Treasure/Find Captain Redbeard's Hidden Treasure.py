def find_treasure(start_x: float) -> float:
    
    learning_rate = 0.01   # separate line ✅
    tolerance = 1e-6       # separate line ✅
    max_iters = 10000      # separate line ✅
    
    def f(x):
        # original function to compare results
        return x**4 - 3*x**3 + 2
    
    def gradient(x):
        # derivative of x^4 - 3x^3 + 2
        return 4 * x**3 - 9 * x**2
    
    def descend(start):
        # run gradient descent from a given start point
        x = start
        for _ in range(max_iters):
            grad = gradient(x)
            new_x = x - learning_rate * grad
            if abs(new_x - x) < tolerance:
                break
            x = new_x
        return x
    
    # try multiple starts to avoid local minimum trap at x=0
    starts = [start_x, 1.0, 2.0, 3.0, -1.0]
    
    best_x = start_x
    best_val = float('inf')
    
    for s in starts:
        x = descend(s)          # find minimum from each start
        if f(x) < best_val:     # keep x with lowest f(x)
            best_val = f(x)
            best_x = x
    
    return round(best_x, 4)

