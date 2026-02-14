# Coding Interview Practice 🚀

[![Languages](https://img.shields.io/badge/Languages-Python%20%7C%20Go%20%7C%20Java%20%7C%20Rust-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A multi-language repository for solving coding problems from various platforms. This project serves two main purposes:

1. **Learning Algorithms & Interview Preparation** - Practice algorithmic thinking and problem-solving patterns
2. **Learning Programming Language Fundamentals** - Master syntax, idioms, and best practices across different languages

## 📚 Problem Sources

- **[ByteByteGo Coding Patterns](https://bytebytego.com/courses/coding-patterns)** - Primary resource for learning algorithmic patterns
- **[LeetCode](https://leetcode.com/)** - Top Interview 150 and practice problems

## 🗂️ Project Structure

```
├── python/          # Python (main language)
│   ├── leetcode/
│   └── bytebytego/
├── golang/          # Go (learning & review)
│   └── leetcode/
├── java/            # Java (planned)
└── rust/            # Rust (planned)
```

Problems are organized by category: `array-string`, `hashmap`, `two-pointer`, `stack`, `linked-list`, `intervals`, `math`, etc.

## 🛠️ Languages

- **Python** 🐍 - Primary language
- **Go** 🔵 - Learning & reviewing fundamentals
- **Java** ☕ - Planned
- **Rust** 🦀 - Planned

## 💻 Installation

```sh
git clone https://github.com/rezamobaraki/leetcode-top-interview-150.git
cd leetcode-top-interview-150
```

### Python

This project uses [uv](https://github.com/astral-sh/uv) for dependency management:

```sh
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup and activate
uv sync
source .venv/bin/activate
```

### Go

```sh
go version  # Ensure Go is installed
cd golang
```

### Java & Rust

Coming soon!

## 📖 Usage

### Running Solutions

**Python:**
```sh
python python/leetcode/hashmap/two-sum.py
```

**Go:**
```sh
go run golang/leetcode/two-pointer/valid-palindrome.go
```

### Code Quality (Python)

```sh
uv run ruff check .          # Lint
uv run ruff check --fix .    # Auto-fix
uv run ruff format .         # Format
```

## 📚 Problem Categories

Solutions are organized by common algorithmic patterns:

- **Array & String** - Manipulation, searching, and pattern matching
- **HashMap / HashSet** - Efficient lookups and frequency counting
- **Two Pointer** - Optimization techniques for arrays and strings
- **Linked List** - Pointer manipulation and traversal
- **Stack** - LIFO operations and expression parsing
- **Intervals** - Range handling and merging
- **Math** - Number theory and mathematical patterns

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add solutions in any language
- Improve existing solutions
- Add tests or documentation
- Fix bugs

**Coding Standards:**
- Python: PEP 8 (enforced by Ruff)
- Go: Standard Go formatting (`gofmt`)
- Java: Google Java Style Guide
- Rust: Rustfmt

## 📝 License

MIT License - see the LICENSE file for details.

## 📚 Resources

### Learning Platforms
- [ByteByteGo Coding Patterns](https://bytebytego.com/courses/coding-patterns) - Structured algorithmic patterns course
- [LeetCode](https://leetcode.com/) - Practice coding problems
- [NeetCode](https://neetcode.io/) - Problem roadmap and explanations

### Language Documentation
- [Python Documentation](https://docs.python.org/3/)
- [Go Documentation](https://go.dev/doc/)
- [Java Documentation](https://docs.oracle.com/en/java/)
- [Rust Documentation](https://doc.rust-lang.org/)

### Algorithm Resources
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Visualgo](https://visualgo.net/) - Algorithm visualizations

## 👥 Authors

**Reza Mobaraki** - [@rezamobaraki](https://github.com/rezamobaraki)

**Contributors:** [Mary Ostovar](https://github.com/maryOstovar)

---

**Happy Coding!** 💻✨
