def print_models(unprinted_designs, completed_models):
    """Symuluje wydruk projektów."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Wydruk modelu: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Wyświetla wszystkie modele, które zostały wydrukowane."""
    print("\nWydrukowane zostały następujące modele: ")
    for model in completed_models:
        print(model)