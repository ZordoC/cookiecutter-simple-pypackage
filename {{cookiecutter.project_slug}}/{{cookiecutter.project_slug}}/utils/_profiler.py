"""Micro-profiling decorator, used to profile specific functions that can appear to be a bottleneck"""
import cProfile
import tempfile
import pstats


def profile(column="time", list=3):
    """Micro-profiles a specific function using cProfile. This function is to be used
    only as a decorator.

    Args:
        column (str, optional): Sorting criteria for stats. Defaults to "time".
        list (int, optional): Number of rows displayed. Defaults to 3.

    Examle:

        @profile()
        def heavy_function():
            res = random.sample(range(1, 10000), 100000000000)
            return res
    """

    def parametrized_decorator(function):
        def decorated(*args, **kw):
            s = tempfile.mktemp()

            profiler = cProfile.Profile()
            profiler.runcall(function, *args, **kw)
            profiler.dump_stats(s)

            p = pstats.Stats(s)
            print("=" * 5, f"{function.__name__}() profile", "=" * 5)
            p.sort_stats(column).print_stats(list)

        return decorated

    return parametrized_decorator
