# Datasans Pandamatic

A Llama-powered code generator for pandas dataframe processing.

## Installation

```bash
pip install datasans-pandamatic
```

## Usage

```python
import pandas as pd
from datasans_pandamatic import gen

# Load your dataframe
df = pd.read_csv("your_data.csv")

# Generate code with a simple prompt
code = gen(df, "Calculate mean sales by category")
```

## Features

- Llama-powered code generation
- Smart data type handling
- Simple, intuitive API
- Comprehensive error handling

## Changelog

### 0.2.2
- Fixed Together API client initialization

### 0.2.1
- Switched to Llama model for code generation
- Simplified API with single function interface
- Removed key code requirement
- Improved error handling and performance

### 0.1.4
- Previous version changelog...
