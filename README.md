# Security Evidence Collector

A Python-based command-line utility that scans a directory for predefined evidence file types and generates a structured report containing file metadata. This project was developed as a learning exercise in Python automation while applying concepts commonly used in digital forensics and incident response (DFIR).

---

## Overview

During security investigations, analysts often need to quickly identify files that may contain useful evidence. Manually searching through directories is repetitive and time-consuming.

Security Evidence Collector automates this process by scanning a selected directory, identifying evidence-related file types, collecting basic metadata, and optionally generating a report.

This project focuses on building practical Python skills while following a real-world cybersecurity use case.

---

## Features

- Scan the current working directory
- Scan a custom directory
- Detect common evidence file types
  - `.txt`
  - `.log`
  - `.pdf`
  - `.docx`
  - `.exe`
  - `.bat`
  - `.ps1`
- Display:
  - File Name
  - File Extension
  - File Size
  - Absolute File Path
- Generate investigation reports
- Save reports with a custom filename
- Interactive command-line interface
- Basic exception handling for invalid user input

---

## Technologies Used

- Python 3
- os Module
- File Handling
- Exception Handling

---

## Sample Workflow

1. Launch the application.
2. Choose whether to scan the current directory or a custom directory.
3. The application scans for supported evidence files.
4. Review the collected metadata.
5. Choose whether to save the generated report.

---

## Learning Objectives

This project was created to strengthen understanding of:

- Python fundamentals
- Directory traversal
- File handling
- User input validation
- Exception handling
- Basic cybersecurity automation

---

## Current Limitations

This project intentionally keeps the implementation simple for learning purposes.

Current limitations include:

- Scans only the selected directory (no recursive scanning)
- Supports a limited number of file extensions
- Generates plain text reports only
- Does not calculate file hashes
- No logging functionality

---

## Future Improvements

- Recursive directory scanning
- SHA-256 and MD5 hash generation
- CSV and JSON report export
- Timestamp collection
- Logging support
- Refactor using functions and modular design
- Graphical user interface (GUI)

---

## Disclaimer

This project is intended for educational purposes only and demonstrates basic Python automation techniques in the context of digital forensics and incident response.

---

## Author

**Yuvraj Singh**

Cybersecurity Student | Python Automation | Ethical Hacking
