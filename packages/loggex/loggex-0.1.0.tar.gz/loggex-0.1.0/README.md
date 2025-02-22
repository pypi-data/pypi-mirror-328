# Loggex

Loggex helps you track your research experiments across multiple scripts by providing a central log file to record which script produced what results with which configuration.

## Features

- Track experiment runs in CSV, JSON, or Excel format
- Load and add to your experiment log from any script
- Automatic timestamp tracking for each run
- Simple querying and filtering capabilities
- Quick summary reports of your experiments

## Installation

```bash
pip install loggex
```

## Quick Start

### Creating a New Log

```python
from loggex import Project

# Create a new experiment log (defaults to CSV format)
project = Project.new(
    name="sentiment_experiments",
    path="logs",
    columns=["experiment", "script", "model", "lr", "bs", "max_len", "f1_score", "results_file"]
)

# Log an experiment run
project.add(
    experiment="bert_base",
    script="train_bert.py",
    model="bert-base-uncased",
    lr=2e-5,
    bs=16,
    max_len=128,
    f1_score=0.91,
    results_file="results/bert_base_full.csv"
)
```

### Adding Results from Another Script

```python
from loggex import Project

# Load the existing log
project = Project.load("sentiment_experiments", path="logs")

# Add results from this script
project.add(
    experiment="bert_large",
    script="train_bert_improved.py",
    model="bert-large-uncased",
    lr=3e-5,
    bs=8,
    max_len=256,
    f1_score=0.94,
    results_file="results/bert_large_full.csv"
)

# View latest runs
project.tail()
```

### Analyzing Your Experiments

```python
# Generate a summary report
project.report()

# Filter experiments
best_runs = project.filter("f1_score > 0.92")
print(best_runs)

# Remove failed runs
project.remove("f1_score < 0.5")

# Export filtered results
project.export(
    format='excel',  # 'csv', 'json', or 'excel'
    query="model == 'bert-base-uncased'",
    path="analysis/bert_base_results.xlsx"
)
```

### Using Different Formats

By default, Loggex uses CSV files, but you can choose other formats:

```python
# Create a new log in Excel format
project = Project.new(
    name="mnist_experiments",
    path="logs",
    columns=["experiment", "script", "accuracy"],
    format='excel'  # 'csv', 'json', or 'excel'
)
```

## Documentation

The `Project` class supports:
- Creating new logs (`new()`)
- Loading existing logs (`load()`)
- Adding log entries (`add()`) with automatic timestamp tracking
- Printing all logs (`print()`)
- Viewing latest entries (`tail(n=5)`)
- Removing entries (`remove(query)`)
- Generating detailed reports (`report()`)
- Exporting filtered results (`export(format, query, path)`)

See in-line docstrings in the source code for complete usage details.

## License

Licensed under the MIT License.
