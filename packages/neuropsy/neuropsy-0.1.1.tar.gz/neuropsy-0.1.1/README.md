# Neuropsy 🧠

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PyPI](https://img.shields.io/badge/pypi-v0.1-orange)

**Neuropsy** is a Python package designed for neuropsychological tools and utilities. It provides an easy-to-use graphical interface for administering and recording neuropsychological tests, generating PDF reports, and calculating scores.

---

## Features ✨

- **Graphical User Interface (GUI)**: Built with PySide6 for a seamless user experience.
- **PDF Report Generation**: Automatically generate PDF reports using `reportlab`.
- **Customizable Questions**: Add or modify questions and categories as needed.
- **Score Calculation**: Automatically calculate sensory scores and save results.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## Installation 🛠️

You can install **Neuropsy** using `pip`:

```bash
pip install neuropsy

Alternatively, you can install it from the source:

# Clone the repository
git clone https://github.com/yourusername/neuropsy.git
cd neuropsy

# Install the package
pip install .
```

## How to Use 🚀

### Launching the Application
After installation, you can launch the application by running:

```bash
run-neuropsy
```

## If the Command Doesn’t Work

If the run-neuropsy command is not found, it means the package’s executable is not in your system’s PATH. Follow these steps to fix it:

### On macOS/Linux

1. Open a terminal 
Find the path to the run-neuropsy executable:

```bash
which run-neuropsy
```
This will output something like /Users/yourusername/py3/bin/run-neuropsy.

Open your shell configuration file (e.g., .bashrc, .zshrc):

```bash
nano ~/.bashrc # or nano ~/.zshrc
```

Add the following line to the file:

```bash
export PATH="/Users/yourusername/py3/bin:$PATH"
```
Save and exit (Ctrl + O, then Ctrl + X).

Reload your shell configuration:

```bash
source ~/.bashrc # or source ~/.zshrc
```

Verify the command works:

```bash
run-neuropsy
```

### On Windows

1. Open a Command Prompt or PowerShell.

Find the path to the run-neuropsy executable:

```bash
where run-neuropsy
```     

Add the path to your Python environment to your PATH environment variable:

```bash
set PATH="C:\path\to\your\python\environment\Scripts;%PATH%"
``` 

Verify the command works:

```bash
run-neuropsy
```


## Application Workflow

    Fill Out the Form: Enter the required information in the GUI.

    Submit the Form: Click the "Submit" button to save the results.

    Generate Reports: The application will generate a PDF report and save it to your chosen directory.