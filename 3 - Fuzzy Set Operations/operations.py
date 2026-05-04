# Fuzzy Set Operations

# Define fuzzy sets as dictionaries
A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.7}
B = {'x1': 0.6, 'x2': 0.3, 'x3': 0.8}

# UNION (max)
def fuzzy_union(A, B):
    return {x: max(A[x], B[x]) for x in A}

# INTERSECTION (min)
def fuzzy_intersection(A, B):
    return {x: min(A[x], B[x]) for x in A}

# COMPLEMENT (1 - μ)
def fuzzy_complement(A):
    return {x: round(1 - A[x], 2) for x in A}

# DIFFERENCE (A - B = min(A, 1-B))
def fuzzy_difference(A, B):
    return {x: round(min(A[x], 1 - B[x]), 2) for x in A}


# -------- Fuzzy Relations --------

# Cartesian Product (A x B)
def cartesian_product(A, B):
    relation = {}
    for a in A:
        for b in B:
            relation[(a, b)] = min(A[a], B[b])
    return relation


# Max-Min Composition
def max_min_composition(R1, R2, X, Y, Z):
    result = {}
    for x in X:
        for z in Z:
            values = []
            for y in Y:
                values.append(min(R1[(x, y)], R2[(y, z)]))
            result[(x, z)] = max(values)
    return result


# -------- Execution --------

print("Union:", fuzzy_union(A, B))
print("Intersection:", fuzzy_intersection(A, B))
print("Complement of A:", fuzzy_complement(A))
print("Difference (A - B):", fuzzy_difference(A, B))

# Define sets for relations
X = ['x1', 'x2']
Y = ['y1', 'y2']
Z = ['z1', 'z2']

# Fuzzy sets for relations
A_rel = {'x1': 0.5, 'x2': 0.8}
B_rel = {'y1': 0.6, 'y2': 0.9}
C_rel = {'z1': 0.7, 'z2': 0.4}

# Relations
R1 = cartesian_product(A_rel, B_rel)
R2 = cartesian_product(B_rel, C_rel)

print("Relation R1:", R1)
print("Relation R2:", R2)

# Composition
composition = max_min_composition(R1, R2, X, Y, Z)
print("Max-Min Composition:", composition)