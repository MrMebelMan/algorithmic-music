from FoxDot.lib.TimeVar import expvar, linvar, sinvar, TimeVar
from FoxDot.lib.Patterns.Main import Pattern

def nvar(values: (Pattern, list), durations: (Pattern, list)):
    if not isinstance(values, (Pattern, list)):
        raise Exception('values should be a Pattern, or a list!')
    if not isinstance(durations, (Pattern, list)) and not isinstance(durations, int):
        raise Exception('durations should be a Pattern, a list or a number!')
    elif isinstance(durations, int):
        durations = [durations for x in range(len(values))]
    if len(values) < 2 or len(durations) < 2:
        raise Exception('Both values and durations must be at least 2 elements long!')
    if len(values) != len(durations):
        raise Exception('Values should have the same length as durations!')
    result_var_values = []
    timevars = []
    for i, val in enumerate(values):
        if isinstance(val, (float, int, long)):
            result_var_values.append(val)
        elif isinstance(val, (TimeVar, linvar, expvar, sinvar)):
            result_var_values.append(0)
            timevar_values = [1 if j == i else 0 for j, x in enumerate(range(len(durations)))]
            timevars.append(var(timevar_values, durations) * val)
    result_var = var(result_var_values, durations)
    for timevar in timevars:
        result_var += timevar
    return result_var
