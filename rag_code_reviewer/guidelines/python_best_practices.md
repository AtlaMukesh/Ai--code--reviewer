# Python Best Practices

## Error Handling
Never use a bare `except:`. Catch specific exceptions such as ValueError or KeyError, and log them with context. Silent failures hide bugs. Use `with` statements for files and connections so they always close.

## Mutable Default Arguments
Never use mutable default arguments such as `def add(item, items=[])`. The list is created once and shared between calls. Use `None` as the default and create the list inside the function.

## Functions
Keep each function short and focused on one job. If a function needs a comment to separate sections, split it into smaller functions. Add type hints and a docstring to every public function.

## Naming
Use snake_case for functions and variables, PascalCase for classes, and UPPER_CASE for constants. Names should explain intent, so use `user_count` instead of `x`.

## Performance
Prefer list comprehensions over manual loops that build lists. Do not concatenate strings inside a loop; use `"".join(...)`. Avoid database or network calls inside tight loops.

## Readability
Replace magic numbers with named constants. Use early returns instead of deeply nested if statements. Remove unused imports and dead code.