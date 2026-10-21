import itertools

def strong_off_checker(types):
    max_coverage = 0
    results = []
    for combo in itertools.combinations(types, 4):
        coverage = []
        for t in combo:
            for c in t.strong_off:
                if not c in coverage:
                    coverage.append(c)
        if len(coverage) > max_coverage:
            max_coverage = len(coverage)
            results = []
        if len(coverage) == max_coverage:
            combo_list = []
            for t in combo:
                combo_list.append(t.name)
            results.append(combo_list)
    
    return results

def weak_off_checker(types):
    min_weakness = 18
    results = []
    for combo in itertools.combinations(types, 4):
        weakness = []
        for t in combo:
            for c in t.weak_off:
                if not c in weakness:
                    weakness.append(c)
        if weakness.length() < min_weakness:
            min_weakness = weakness.length()
            results = []
        if weakness.length() == min_weakness:
            results.append(combo)
    
    return results