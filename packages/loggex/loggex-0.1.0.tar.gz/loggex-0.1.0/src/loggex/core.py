from datetime import datetime
import pandas as pd
from pathlib import Path
from typing import List, Optional, Any, Literal

FormatType = Literal['csv', 'json', 'excel']

class Project:
    def __init__(self, name: str, path: Path, columns: List[str], df: pd.DataFrame, format: FormatType) -> None:
        self.name = name
        self.path = path
        self.columns = columns
        self.df = df
        self.format = format

    @classmethod
    def new(cls, name: str, path: Optional[str] = ".", columns: List[str] = None, format: FormatType = 'csv') -> "Project":
        """
        Creates a new project.
        Args:
            name: Name of the project (required)
            path: Directory for the project CSV (defaults to current folder)
            columns: List of column names (required, must contain at least one element)
            format: Format of the project file (default: 'csv')
        """
        if not name:
            raise ValueError("Project name is required")
        if not columns or len(columns) == 0:
            raise ValueError("At least one column must be provided for a new project")
        
        # Automatically add "timestamp" column if not provided
        columns = list(columns)
        if "timestamp" not in columns:
            columns.append("timestamp")
            
        p = Path(path) if path else Path(".")
        file_extension = 'xlsx' if format == 'excel' else format
        project_file = p / f"{name}.{file_extension}"
        if project_file.exists():
            raise FileExistsError(f"Project '{name}' already exists at {p}")
        
        df = pd.DataFrame(columns=columns)
        p.mkdir(parents=True, exist_ok=True)
        if format == 'csv':
            df.to_csv(project_file, index=False)
        elif format == 'json':
            df.to_json(project_file, date_format='iso')
        elif format == 'excel':
            df.to_excel(project_file, index=False)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        return cls(name, p, columns, df, format)

    @classmethod
    def load(cls, name: str, path: Optional[str] = ".", format: FormatType = 'csv') -> "Project":
        """
        Loads an existing project.
        Args:
            name: Name of the project (required)
            path: Directory containing the project file (defaults to current folder)
            format: Format of the project file (default: 'csv')
        """
        if not name:
            raise ValueError("Project name is required")
            
        p = Path(path) if path else Path(".")
        file_extension = 'xlsx' if format == 'excel' else format
        project_file = p / f"{name}.{file_extension}"
        if not project_file.exists():
            raise FileNotFoundError(f"Project '{name}' does not exist at {p}")
        
        if format == 'csv':
            df = pd.read_csv(project_file)
        elif format == 'json':
            df = pd.read_json(project_file)
        elif format == 'excel':
            df = pd.read_excel(project_file)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        # Convert timestamp column to datetime if it exists
        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
        columns = list(df.columns)
        # If "timestamp" is missing in the stored file, add it to the project schema
        if "timestamp" not in columns:
            columns.append("timestamp")
            df["timestamp"] = None
        
        return cls(name, p, columns, df, format)

    def add(self, **values: Any) -> None:
        """
        Adds a new experiment run.
        The timestamp is automatically added.
        Args:
            **values: Values for each column as named parameters (do not provide 'timestamp')
        """
        required = set(self.columns) - {"timestamp"}
        missing = required - set(values.keys())
        if missing:
            raise ValueError(f"Missing values for columns: {missing}")
        
        # Automatically add current timestamp if not provided
        values["timestamp"] = datetime.now().isoformat()
        self.df = pd.concat([self.df, pd.DataFrame([values])], ignore_index=True)
        file_extension = 'xlsx' if self.format == 'excel' else self.format
        if self.format == 'csv':
            self.df.to_csv(self.path / f"{self.name}.{file_extension}", index=False)
        elif self.format == 'json':
            self.df.to_json(self.path / f"{self.name}.{file_extension}", date_format='iso')
        elif self.format == 'excel':
            self.df.to_excel(self.path / f"{self.name}.{file_extension}", index=False)
        else:
            raise ValueError(f"Unsupported format: {self.format}")
    
    def remove(self, query: str) -> None:
        """
        Removes entries from the log that match the given query.
        Args:
            query: Query string in pandas query format (e.g., "lr > 0.01 and bs == 32")
        """
        before_len = len(self.df)
        self.df = self.df.query("not ({})".format(query))
        removed = before_len - len(self.df)
        print(f"Removed {removed} entries")
        file_extension = 'xlsx' if self.format == 'excel' else self.format
        if self.format == 'csv':
            self.df.to_csv(self.path / f"{self.name}.{file_extension}", index=False)
        elif self.format == 'json':
            self.df.to_json(self.path / f"{self.name}.{file_extension}", date_format='iso')
        elif self.format == 'excel':
            self.df.to_excel(self.path / f"{self.name}.{file_extension}", index=False)
        else:
            raise ValueError(f"Unsupported format: {self.format}")

    def tail(self, n: int = 5) -> None:
        """
        Prints the last N experiment runs.
        Args:
            n: Number of entries to show (default: 5)
        """
        print(self.df.tail(n).to_string(index=False))

    def print(self) -> None:
        """
        Prints all experiments in a formatted table.
        """
        print(self.df.to_string(index=False))
    
    def report(self) -> None:
        """
        Prints a detailed report with meta information for each column.
        For each column, it shows:
         - Data type
         - Total number of unique values
         - For numeric columns: mean, min, and max values.
        """
        print("Detailed Log Report Summary:")
        total_entries = len(self.df)
        print(f"Total entries: {total_entries}")
        for col in self.columns:
            series = self.df[col]
            print(f"\nColumn: {col}")
            print(f" - Data Type: {series.dtype}")
            print(f" - Unique Values: {series.nunique(dropna=True)}")
            if pd.api.types.is_numeric_dtype(series):
                print(" - Numeric Summary:")
                print(f"   Mean: {series.mean():.3f}")
                print(f"   Min: {series.min()}")
                print(f"   Max: {series.max()}")

    def filter(self, query: str) -> pd.DataFrame:
        """
        Returns a filtered view of the data matching the query.
        Args:
            query: Query string in pandas query format
        Returns:
            DataFrame with matching entries
        """
        return self.df.query(query)

    def search(self, column: str, value: Any) -> pd.DataFrame:
        """
        Simple search in a specific column.
        Args:
            column: Column name to search in
            value: Value to search for
        Returns:
            DataFrame with matching entries
        """
        if column not in self.columns:
            raise ValueError(f"Column '{column}' not found")
        return self.df[self.df[column] == value]

    def export(self, format: FormatType = 'excel', path: Optional[str] = None, query: Optional[str] = None) -> None:
        """
        Exports the log to different formats.
        Args:
            format: 'csv', 'json' or 'excel'
            path: Output path (optional)
            query: Filter query before export (optional)
        """
        data = self.filter(query) if query else self.df
        
        if not path:
            file_extension = 'xlsx' if format == 'excel' else format
            path = self.path / f"{self.name}_export.{file_extension}"
        
        if format == 'csv':
            data.to_csv(path, index=False)
        elif format == 'json':
            data.to_json(path, date_format='iso')
        elif format == 'excel':
            data.to_excel(path, index=False)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        print(f"Exported to {path}")