# Lab 5: Static Code Analysis

Repo: https://github.com/varunrao024/L5_30_electricity_bill
Script: electricity_bill.py

## Results

| Tool | Before | After |
|---|---|---|
| Bandit | 4 issues (1 High, 1 Medium, 2 Low) | No issues |
| Pylint | 5.44/10 | 10.00/10 |
| Flake8 | 4 issues | No issues |

## Issue Table

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| os.system with string concatenation (B605) | Security, High | 63 | meterIp was joined into a shell command, which allows command injection | Replaced with requests.get using a timeout |
| xml.etree.ElementTree.fromstring (B314) | Security, Medium | 18 | Standard XML parser is open to XML attacks such as entity expansion | Switched to defusedxml |
| xml.etree.ElementTree import (B405) | Security, Low | 3 | Same risk, flagged at import | Imported ElementTree from defusedxml |
| Hardcoded password (B105) | Security, Low | 13 | CLERK_PASSWORD stored as a plain string in source | Read from the CLERK_PASSWORD environment variable |
| Mutable default argument (W0102) | Bug | 42 | extras={} is created once and shared across calls | Default changed to None, dict created inside the function |
| Unused argument (W0613) | Code quality | 50 | averageBill(currency) never used currency | Removed the parameter and updated the call in main |
| open without encoding (W1514) | Code quality | 57 | File opened without an explicit encoding | Added encoding="utf-8" |
| Naming style (C0103) | Style | 17-67 | camelCase function, argument and variable names | Renamed to snake_case |
| Missing docstrings (C0114, C0116) | Documentation | 1, 17-66 | Module and all functions had no docstrings | Added short docstrings |
| E302 blank lines | Style | 22 | Only one blank line before calculateUnits | Added a second blank line |
| E203 whitespace before ':' | Style | 44 | "meter" : meterId in the dict | Removed the space |
| E501 line too long | Style | 72 | Print line was 86 characters | Split across two lines |
| E225 missing whitespace | Style | 76 | total=sum(...) | Added spaces around = |
| Missing final newline (C0304) | Style | 93 | File did not end with a newline | Added a newline at end of file |

## Commits

1. fix bandit issues
2. fix pylint issues
3. fix flake8 issues

Before and after reports are in the repo (before/ folder and the root).
