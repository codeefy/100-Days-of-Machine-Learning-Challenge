def poly_term_derivative(c: float, x: float, n: float) -> float:
    # power rule: d/dx[c * x^n] = c * n * x^(n-1)
    return c*n*x**(n-1)

    pass
