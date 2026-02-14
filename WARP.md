# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This repository contains solutions to LeetCode's Top 150 Interview Questions, implemented in multiple languages (Python, Go, JavaScript, TypeScript). Each solution is a standalone file with a `main` function/block that includes example test cases.

## Project Structure

Solutions are organized by **problem category** (not by problem type):
- `python/array-string/` - Array and string manipulation problems
- `python/two-pointer/` - Two-pointer technique problems
- `python/hashmap/` - Hash map/dictionary problems
- `python/stack/` - Stack-based problems
- `python/intervals/` - Interval-related problems
- `python/linked-list/` - Linked list problems

The same structure mirrors across `golang/`, `javascript/`, and `typescript/` directories.

## Running Solutions

### Python
```bash
# Run a single solution from the root
python python/array-string/merge-sorted-array.py

# Or navigate to the category directory
cd python/array-string
python merge-sorted-array.py
```

### Go
```bash
# Run a single solution from the root
go run golang/array-string/merge-sorted-array.go

# Or navigate to the category directory
cd golang/array-string
go run merge-sorted-array.go
```

### JavaScript
```bash
# Run a single solution
node javascript/1-two-pointer/is-subsequence.js
```

### TypeScript
```bash
# Compile and run
tsc typescript/1-two-pointer/is-subsequence.ts
node typescript/1-two-pointer/is-subsequence.js
```

## File Naming Convention

All solution files use kebab-case naming that matches the LeetCode problem slug:
- `merge-sorted-array.py` → LeetCode problem "Merge Sorted Array"
- `is-subsequence.go` → LeetCode problem "Is Subsequence"
- `ransom-note.py` → LeetCode problem "Ransom Note"

## Code Structure Patterns

### Python Solutions
- Functions use snake_case naming
- Type hints from `typing` module (e.g., `List[int]`)
- Test cases in `if __name__ == '__main__':` block
- Often include alternative implementations (e.g., `merge_v2()`)

### Go Solutions
- Functions use PascalCase for exported functions, camelCase for internal
- Package is always `main` with a `main()` function
- Test cases directly in `main()` function
- Use Go's built-in types (slices, maps)

## Adding New Solutions

When adding a new solution:
1. Identify the correct category directory
2. Use kebab-case filename matching the LeetCode problem URL slug
3. Include a `main` function/block with at least 2 test cases
4. Add inline comments explaining the algorithm approach
5. For complex solutions, include alternative implementations

## Testing

This repository does not use formal testing frameworks. Each solution file is self-contained with test cases in the main execution block. To verify a solution:

1. Run the file directly with the language's runtime
2. Check the output matches expected results in comments
3. Modify test inputs in the main block to try additional cases

## Language-Specific Notes

### Python
- Standard library imports are used (e.g., `Counter` from `collections`)
- Solutions prioritize readability and Pythonic idioms

### Go
- Solutions use idiomatic Go patterns
- No external dependencies beyond the standard library
- Pointer usage for in-place modifications where applicable
