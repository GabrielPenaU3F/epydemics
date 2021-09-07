def second_derivative(t, rho, gamma):
    return ((gamma/rho) - 1) * (rho**2) * (1 + rho * t)**(gamma/rho - 2)

