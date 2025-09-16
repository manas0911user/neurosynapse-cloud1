import random
from backend.agents.mutator import mutate
from sandbox.runner import run_function_safely

# Example seed function (simple microservice config)
seed_function = {
    'cpu': 1.0,         # vCPU
    'memory': 128,      # MB
    'timeout': 5,       # seconds
    'retries': 2
}

def fitness(function_variant: dict) -> float:
    """
    Fitness function now uses sandbox execution metrics.
    Lower latency + successful execution = better score.
    """
    metrics = run_function_safely(function_variant)

    if not metrics['success']:
        # Penalize failed executions
        return float('inf')

    # Weighted scoring: latency (50%), memory (30%), cpu (20%)
    score = (
        metrics['latency'] * 0.5 +
        metrics['memory'] * 0.3 +
        metrics['cpu'] * 0.2
    )

    # Small random factor to avoid premature convergence
    score += random.uniform(-0.05, 0.05)

    return score


def evolutionary_loop(seed, generations=5, population_size=5):
    population = [seed]

    for gen in range(generations):
        print(f"\n--- Generation {gen+1} ---")
        # Create mutated variants
        new_population = []
        for variant in population:
            for _ in range(population_size):
                new_variant = mutate(variant)
                new_population.append(new_variant)

        # Evaluate fitness using sandbox metrics
        scored_population = [(fitness(v), v) for v in new_population]

        # Select top 2 variants for next generation
        scored_population.sort(key=lambda x: x[0])
        population = [v for (_, v) in scored_population[:2]]

        # Print best variant of this generation
        best_score, best_variant = scored_population[0]
        print(f"Best Variant: {best_variant} | Fitness: {best_score:.3f}")

    return population[0]  # Return best variant after all generations


if __name__ == "__main__":
    best = evolutionary_loop(seed_function, generations=5, population_size=3)
    print("\n=== Final Best Variant ===")
    print(best)
