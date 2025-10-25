"""
Performance Decorator Module
Provides decorators to measure time and space complexity of functions.
"""
import time
import tracemalloc
from functools import wraps


def measure_performance(func):
    """
    Decorator that measures both time and space complexity of a function.

    Returns:
        A wrapper function that prints execution time and memory usage.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Start memory tracking
        tracemalloc.start()

        # Start time tracking
        start_time = time.perf_counter()

        # Execute the function
        result = func(*args, **kwargs)

        # End time tracking
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # Get memory usage
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Print results
        print(f"\n{'='*60}")
        print(f"Function: {func.__name__}")
        print(f"{'='*60}")
        print(f"Execution Time: {execution_time:.6f} seconds ({execution_time * 1000:.3f} ms)")
        print(f"Current Memory: {current / 1024:.2f} KB ({current} bytes)")
        print(f"Peak Memory:    {peak / 1024:.2f} KB ({peak} bytes)")
        print(f"{'='*60}\n")

        return result

    return wrapper


def measure_time(func):
    """
    Decorator that measures only execution time of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print(f"{func.__name__}: {execution_time:.6f}s ({execution_time * 1000:.3f} ms)")

        return result

    return wrapper


def measure_memory(func):
    """
    Decorator that measures only memory usage of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"{func.__name__}: Peak Memory = {peak / 1024:.2f} KB ({peak} bytes)")

        return result

    return wrapper


def compare_performance(funcs, test_cases):
    """
    Compare performance of multiple functions with given test cases.

    Args:
        funcs: List of functions to compare
        test_cases: List of tuples containing (args, kwargs) for each test

    Example:
        compare_performance(
            [two_sum, two_sum_v2, two_sum_v3],
            [
                (([2, 7, 11, 15], 9), {}),
                (([3, 2, 4], 6), {}),
            ]
        )
    """
    results = {func.__name__: {'times': [], 'memories': [], 'results': []} for func in funcs}

    for test_idx, (args, kwargs) in enumerate(test_cases):
        print(f"\n{'#'*60}")
        print(f"Test Case {test_idx + 1}: args={args}")
        print(f"{'#'*60}")

        for func in funcs:
            # Measure time
            start_time = time.perf_counter()

            # Measure memory
            tracemalloc.start()
            result = func(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            end_time = time.perf_counter()
            execution_time = end_time - start_time

            # Store results
            results[func.__name__]['times'].append(execution_time)
            results[func.__name__]['memories'].append(peak)
            results[func.__name__]['results'].append(result)

            print(f"\n{func.__name__}:")
            print(f"  Result: {result}")
            print(f"  Time:   {execution_time:.6f}s ({execution_time * 1000:.3f} ms)")
            print(f"  Memory: {peak / 1024:.2f} KB ({peak} bytes)")

    # Print summary
    print(f"\n{'*'*60}")
    print("PERFORMANCE SUMMARY")
    print(f"{'*'*60}")

    for func_name, data in results.items():
        avg_time = sum(data['times']) / len(data['times'])
        avg_memory = sum(data['memories']) / len(data['memories'])

        print(f"\n{func_name}:")
        print(f"  Average Time:   {avg_time:.6f}s ({avg_time * 1000:.3f} ms)")
        print(f"  Average Memory: {avg_memory / 1024:.2f} KB ({avg_memory} bytes)")

    # Determine winners
    print(f"\n{'*'*60}")
    fastest = min(results.items(), key=lambda x: sum(x[1]['times']))
    most_memory_efficient = min(results.items(), key=lambda x: sum(x[1]['memories']))

    print(f"⚡ Fastest: {fastest[0]}")
    print(f"💾 Most Memory Efficient: {most_memory_efficient[0]}")
    print(f"{'*'*60}\n")

    return results

