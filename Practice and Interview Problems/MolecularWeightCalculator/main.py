# Define the atomic weights of elements
atomic_weights = {'H': 1.00784, 'C': 12.011, 'O': 15.999}

def calculate_molecular_weight(formula):
    total_weight = 0.0
    current_element = ''
    current_count = ''

    for char in formula:
        if char.isalpha():
            if current_count == '':
                current_count = '1'
            total_weight += atomic_weights.get(current_element, 0.0) * int(current_count)
            current_element = char
            current_count = ''
        elif char.isdigit():
            current_count += char
        else:
            current_element += char

    if current_count == '':
        current_count = '1'
    total_weight += atomic_weights.get(current_element, 0.0) * int(current_count)

    return total_weight

while True:
    molecular_formula = input("Enter a molecular formula (e.g., C6H12O6): ").strip()
    
    if not molecular_formula:
        break

    molecular_weight = calculate_molecular_weight(molecular_formula)
    print(f"The molecular weight of {molecular_formula} is approximately {molecular_weight:.2f} g/mol\n")
