"""
Input	                Output
4                       Ce
Ce O                    Ee
Mo O Ce                 Mo
Ee                      3
Mo

3                       Ch
Ge Ch O Ne              Ge
Nb Mo Tc                Mo
O Ne                    Nb
                        Ne
                        O
                        Tc
"""
n = int(input())
chemical_compounds_set = set()

for _ in range(n):
    chemical_compounds = input().split()
    for chemical in chemical_compounds:
        chemical_compounds_set.add(chemical)

print('\n'.join(chemical_compounds_set))

"""
# Variant 2
for _ in range(n):
    chemical_compounds = set(input().split())
    # Add every new set (chemical_compounds) to the set result with (.union) = (a|b)
    result = result.union(chemical_compounds)
    
[print(el) for el in result]

# Variant 3: for printing
print(*result, sep='\n')
"""