
# PyForShort

**PyForShort** is a Python package designed for creating shortcuts on Windows using PowerShell.

## Installation

You can install the package using `pip`:

```bash
pip install PyForShort
```

## Usage

The package provides the function `CreateShortcut` to create a shortcut at the specified location.

### Function: `CreateShortcut`

```python
from pyforshort import CreateShortcut

# Parameters:
# name: The name of the shortcut.
# path: The directory where the shortcut will be created.
# target: The target file or folder that the shortcut will point to.

CreateShortcut(name="MyShortcut", path="C:/path/to/shortcut/directory", target="C:/path/to/target/file")
```

### Example

```python
from pyforshort import CreateShortcut

# Creating a shortcut named "MyApp" in the "C:/Shortcuts" folder pointing to "C:/Program Files/MyApp/myapp.exe"
CreateShortcut(name="MyApp", path="C:/Shortcuts", target="C:/Program Files/MyApp/myapp.exe")
```

This will create a shortcut named `MyApp.lnk` in the `C:/Shortcuts` folder, which points to `C:/Program Files/MyApp/myapp.exe`.

## Requirements

- Python 3.6 or higher
- Windows OS

## Error Handling

If the provided `path` does not exist, a `FileNotFoundError` will be raised:

```python
FileNotFoundError: Error: The location 'C:/path/to/shortcut/directory' is not valid.
```

## Contributing

Feel free to fork the repository and submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
