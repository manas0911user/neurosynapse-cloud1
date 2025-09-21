import time
import json

def run_function_safely(variant: dict) -> dict: 
    """
    Simulates safe execution of a mutated service inside a sandbox.
    Later this can be replaced with Docker/WASM container execution.
    """

    start_time = time.time()

    # 🔹 Simulated latency (depends on timeout config)
    simulated_latency = max(0.1, variant['timeout'] * 0.8)

    # 🔹 Decide success/failure
    success = simulated_latency <= variant['timeout']

    # Simulate execution delay (not real execution, just demo)
    time.sleep(0.05)

    end_time = time.time()
    execution_time = round(end_time - start_time, 3)

    # 🔹 Collect metrics
    metrics = {
        "latency": round(simulated_latency, 3),
        "success": success,
        "cpu": variant.get("cpu", 1.0),
        "memory": variant.get("memory", 128),
        "retries": variant.get("retries", 0),
        "execution_time": execution_time
    }

    return metrics


# 🔹 Testing the sandbox independently
if __name__ == "__main__":
    test_variant = {
        "cpu": 1.0,
        "memory": 128,
        "timeout": 5,
        "retries": 2
    }

    result = run_function_safely(test_variant)
    print("Sandbox Execution Metrics:")
    print(json.dumps(result, indent=4))
