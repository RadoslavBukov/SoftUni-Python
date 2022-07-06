"""
Input	            Output	                Input	                        Output
SoftUni rocks	     : 1 time/s             Why do you like Python?	        : 4 time/s
                    S: 1 time/s                                             ?: 1 time/s
                    U: 1 time/s                                             P: 1 time/s
                    c: 1 time/s                                             W: 1 time/s
                    f: 1 time/s                                             d: 1 time/s
                    i: 1 time/s                                             e: 1 time/s
                    k: 1 time/s                                             h: 2 time/s
                    n: 1 time/s                                             i: 1 time/s
                    o: 2 time/s                                             k: 1 time/s
                    r: 1 time/s                                             l: 1 time/s
                    s: 1 time/s                                             n: 1 time/s
                    t: 1 time/s                                             o: 3 time/s
                                                                            t: 1 time/s
                                                                            u: 1 time/s
                                                                            y: 3 time/s
"""
string_input = input()
symbol_dict = {}

for symbol in string_input:
    if symbol not in symbol_dict.keys():
        symbol_dict[symbol] = 1
    else:
        symbol_dict[symbol] += 1

for key, value in sorted(symbol_dict.items()):
    print(f"{key}: {value} time/s")