"""
Input
Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett

Output
Peter Smith Lily Everett
"""
import re

names = input()

matches = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", names)

print(" ".join(matches))
