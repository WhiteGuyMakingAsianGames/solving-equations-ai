def parse_equation(equation):
    """
    Parses an equation of the form ax + b = cx + d and converts it to standard form Ax + B = 0.
    """
    equation = equation.replace(' ', '')
    lhs, rhs = equation.split('=')
    lhs = lhs.replace('-', '+-')
    rhs = rhs.replace('-', '+-')
    
    # Parse left-hand side
    lhs_terms = lhs.split('+')
    a, b = 0, 0
    for term in lhs_terms:
        if 'x' in term:
            a += float(term.replace('x', ''))
        else:
            b += float(term)
    
    # Parse right-hand side
    rhs_terms = rhs.split('+')
    c, d = 0, 0
    for term in rhs_terms:
        if 'x' in term:
            c += float(term.replace('x', ''))
        else:
            d += float(term)
    
    # Convert to standard form Ax + B = 0
    A = a - c
    B = b - d
    return A, B

def solve_for_x(A, B):
    """
    Solves the equation Ax + B = 0 for x.
    """
    if A == 0:
        raise ValueError("No solution or infinite solutions exist.")
    x = -B / A
    return x

def solve_equation(equation):
    """
    Solves the equation and provides the steps involved.
    """
    steps = []
    steps.append(f"Step 1: Write down the equation: {equation}")
    
    A, B = parse_equation(equation)
    steps.append(f"Step 2: Convert to standard form Ax + B = 0: {A}x + {B} = 0")
    
    x_solution = solve_for_x(A, B)
    steps.append(f"Step 3: Solve for x: x = {x_solution}")
    
    return x_solution, steps

def main():
    """
    Main function to solve an equation and provide the steps.
    """
    equation = input("Enter the equation (e.g., 2x+1=3x+6): ").strip()
    
    try:
        solution, steps = solve_equation(equation)
        for step in steps:
            print(step)
        print(f"Solution: x = {solution}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
