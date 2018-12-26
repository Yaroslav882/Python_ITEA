from time import perf_counter


class callstat:
    def call_counter(func):
        def helper(x):
            helper.calls += 1
            return func(x)

        helper.calls = 0
        return helper

    @property
    def succ(x):
        return x + 1

foo = callstat()