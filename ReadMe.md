# OPSWAT Assessment

Python program that scans file for malware/vulnerabilities. Uses the OPSWAT MetaDefender Cloud api for scanning.

## Installation

Make sure Python3 and the neccessary libraries (requests, hashlib, time, os) are installed on your machine. Replace API_KEY with your key in the FileScanner.py file. Run program with

```bash
python3 main.py
```

## Contents

- FileScanner.py: Contains class definition for the FileScanner obj
- main.py: Entry point for the application

## Allowed Commands

- exit: Exit the application
- upload_file {filepath} : Upload the specified file for scanning
