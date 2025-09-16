import copy
import random

def mutate(seed_function: dict) -> dict:
    """
    Simple mutation of a service configuration.
    seed_function: dict with keys like 'cpu', 'memory', 'timeout'
    Returns a mutated copy.
    """
    new_variant = copy.deepcopy(seed_function)

    # Mutate CPU allocation +/- 10%
    new_variant['cpu'] = max(0.1, new_variant['cpu'] * random.uniform(0.9, 1.1))

    # Mutate Memory allocation +/- 20MB
    new_variant['memory'] = max(32, new_variant['memory'] + random.randint(-20, 20))

    # Mutate timeout +/- 1 sec
    new_variant['timeout'] = max(1, new_variant['timeout'] + random.randint(-1, 1))

    # Mutate other parameters if exist
    if 'retries' in new_variant:
        new_variant['retries'] = max(0, new_variant['retries'] + random.randint(-1, 1))

    return new_variant
