def cubic_series(n):
    if n == 0:
        return 0
    else:
        current_cube = n ** 3
        print(f" {n} cubed is = to {current_cube}")
        return current_cube + cubic_series(n-1)
    
