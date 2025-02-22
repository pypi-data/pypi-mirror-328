#!/usr/bin/env python3

import argparse
import itertools
from typing import List, Set, Tuple

def parse_arguments():
    parser = argparse.ArgumentParser(description='K-map circuit optimizer')
    parser.add_argument('truthtable', nargs='?', default=None, help='String of 1s, 0s, and Xs representing truth table')
    parser.add_argument('--vars', help='Variables to use (most to least significant)')
    parser.add_argument('--msop', action='store_true', help='Show minimized sum of products')
    parser.add_argument('--mpos', action='store_true', help='Show minimized product of sums')
    parser.add_argument('--sop', action='store_true', help='Show unminimized sum of products')
    parser.add_argument('--pos', action='store_true', help='Show unminimized product of sums')
    parser.add_argument('--all', action='store_true', help='Show all possible minimal solutions')
    return parser.parse_args()

def get_variables(num_vars: int, vars_string: str = None) -> List[str]:
    if vars_string:
        if len(vars_string) != num_vars:
            raise ValueError("Number of variables doesn't match truth table size")
        return list(vars_string)
    return [chr(65 + i) for i in range(num_vars)]

def get_all_groups(ones: Set[int], dcs: Set[int], num_vars: int) -> List[Tuple[Set[int], Tuple[int, ...], Tuple[int, ...]]]:
    groups = []
    for i in range(1, num_vars + 1):
        for combo in itertools.combinations(range(num_vars), i):
            for values in itertools.product([0, 1], repeat=i):
                group = set()
                for term in range(2**num_vars):
                    binary = format(term, f'0{num_vars}b')
                    if all(int(binary[pos]) == val for pos, val in zip(combo, values)):
                        group.add(term)
                if group.issubset(ones | dcs) and group & ones:
                    groups.append((group, combo, values))
    return groups

def get_prime_implicants(groups: List[Tuple[Set[int], Tuple[int, ...], Tuple[int, ...]]]) -> List[Tuple[Set[int], Tuple[int, ...], Tuple[int, ...]]]:
    prime_implicants = []
    for group in groups:
        if not any(group[0].issubset(other[0]) and group[0] != other[0] for other in groups):
            prime_implicants.append(group)
    return prime_implicants

def get_minimal_solution(prime_implicants: List[Tuple[Set[int], Tuple[int, ...], Tuple[int, ...]]], ones: Set[int]) -> List[Tuple[Set[int], Tuple[int, ...], Tuple[int, ...]]]:
    terms_to_cover = ones.copy()
    essential_groups = []
    while terms_to_cover:
        best_coverage = 0
        best_group = None
        best_unique = 0
        for group in prime_implicants:
            coverage = len(group[0] & terms_to_cover)
            if coverage > 0:
                unique_coverage = sum(1 for term in (group[0] & terms_to_cover)
                                      if all(term not in g[0] or g == group for g in prime_implicants))
                if (unique_coverage > best_unique or 
                    (unique_coverage == best_unique and coverage > best_coverage) or
                    (unique_coverage == best_unique and coverage == best_coverage and 
                     len(group[1]) < (len(best_group[1]) if best_group else float('inf')))):
                    best_coverage = coverage
                    best_unique = unique_coverage
                    best_group = group
        if best_group is None:
            break
        essential_groups.append(best_group)
        terms_to_cover -= best_group[0]
    i = 0
    while i < len(essential_groups):
        test_groups = essential_groups[:i] + essential_groups[i+1:]
        covered = set().union(*(g[0] for g in test_groups))
        if ones.issubset(covered):
            essential_groups = test_groups
        else:
            i += 1
    return essential_groups

def get_all_minimal_solutions(prime_implicants: List[Tuple[Set[int], Tuple[int, ...], Tuple[int, ...]]], ones: Set[int]) -> List[List[Tuple[Set[int], Tuple[int, ...], Tuple[int, ...]]]]:
    all_solutions = []
    n = len(prime_implicants)
    for r in range(1, n + 1):
        for combo in itertools.combinations(range(n), r):
            selected = [prime_implicants[i] for i in combo]
            covered = set().union(*(group[0] for group in selected))
            if ones.issubset(covered):
                all_solutions.append(selected)
    if not all_solutions:
        return []
    min_size = min(len(sol) for sol in all_solutions)
    return [sol for sol in all_solutions if len(sol) == min_size]

def solution_to_sop(solution: List[Tuple[Set[int], Tuple[int, ...], Tuple[int, ...]]], variables: List[str]) -> str:
    terms = []
    for _, positions, values in solution:
        term = []
        for pos, val in zip(positions, values):
            term.append(f"/{variables[pos]}" if val == 0 else variables[pos])
        terms.append('*'.join(term))
    return ' + '.join(terms)

def solution_to_pos(solution: List[Tuple[Set[int], Tuple[int, ...], Tuple[int, ...]]], variables: List[str]) -> str:
    terms = []
    for _, positions, values in solution:
        term = []
        for pos, val in zip(positions, values):
            term.append(variables[pos] if val == 0 else f"/{variables[pos]}")
        terms.append('+'.join(term))
    return ' * '.join(f"({t})" for t in terms)


def main():
    args = parse_arguments()
    try:
        if args.truthtable is None:
            import sys
            args.truthtable = sys.stdin.read().strip()

        tt = args.truthtable.strip()
        num_vars = len(tt).bit_length() - 1
        if len(tt) != 2**num_vars or not set(tt).issubset({'0', '1', 'X'}):
            print("Invalid truth table")
            return

        variables = get_variables(num_vars, args.vars)
        minterms = {i for i, v in enumerate(tt) if v == '1'}
        maxterms = {i for i, v in enumerate(tt) if v == '0'}
        dontcares = {i for i, v in enumerate(tt) if v == 'X'}

        if args.sop:
            if not minterms:
                print("0", end="")
            else:
                solution = []
                for minterm in minterms:
                    binary = format(minterm, f'0{num_vars}b')
                    positions = tuple(range(num_vars))
                    values = tuple(int(bit) for bit in binary)
                    solution.append(({minterm}, positions, values))
                print(solution_to_sop(solution, variables), end="")
            return

        if args.pos:
            if not maxterms:
                print("1", end="")
            else:
                solution = []
                for maxterm in maxterms:
                    binary = format(maxterm, f'0{num_vars}b')
                    positions = tuple(range(num_vars))
                    values = tuple(int(bit) for bit in binary)
                    solution.append(({maxterm}, positions, values))
                print(solution_to_pos(solution, variables), end="")
            return

        if args.msop or not args.mpos:
            if not minterms:
                print("0", end="")
            else:
                groups = get_all_groups(minterms, dontcares, num_vars)
                prime_implicants = get_prime_implicants(groups)
                if args.all:
                    solutions = get_all_minimal_solutions(prime_implicants, minterms)
                    for i, sol in enumerate(solutions):
                        if i < len(solutions) - 1:
                            print(solution_to_sop(sol, variables))
                        else:
                            print(solution_to_sop(sol, variables), end="")
                else:
                    solution = get_minimal_solution(prime_implicants, minterms)
                    print(solution_to_sop(solution, variables), end="")

        if args.mpos:
            if not maxterms:
                print("1", end="")
            else:
                groups = get_all_groups(maxterms, dontcares, num_vars)
                prime_implicants = get_prime_implicants(groups)
                if args.all:
                    solutions = get_all_minimal_solutions(prime_implicants, maxterms)
                    for i, sol in enumerate(solutions):
                        if i < len(solutions) - 1:
                            print(solution_to_pos(sol, variables))
                        else:
                            print(solution_to_pos(sol, variables), end="")
                else:
                    solution = get_minimal_solution(prime_implicants, maxterms)
                    print(solution_to_pos(solution, variables), end="")
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    main()