# PL Wff Checker

Script to check if a formula in propositional logic (PL) is a well-formed formula (wff). Program checks:

- if user inputs PL symbols. Acceptable symbols include: upper case letters, parentheses, and truth-functional operators (~, ^, v, ->, <->)
- if user puts propositional letters next to each other
- for an equal number of left and right parentheses
- that parentheses are used correctly
- if negation $\neg$ is used correctly
- if the truth-functional operators $\wedge, \vee, \rightarrow, \leftrightarrow$ are used correctly.

Program returns an error message if input violates one of the above checks.

## Known Error

Program will say that PQ is not a wff but PP is a wff.
