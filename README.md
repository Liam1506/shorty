# Shorty - Automated Page Generator

This repository automatically generates and commits HTML target pages whenever a new GitHub Issue is created.

## How to Set It Up

### 1. Repository Permissions (Required)

For GitHub Actions to create and commit new files to your repository, you must enable **Write** permissions:

1. Go to **Settings** -> **Actions** -> **General**.
2. Scroll down to **Workflow permissions**.
3. Select **Read and write permissions**.
4. Click **Save**.

### 2. File Structure

Ensure your repository matches the following structure (pay close attention to the plural `.github/workflows` folder):

```text
├── .github/
│   └── workflows/
│       └── new_issue.yml    # Workflow config file
├── index.html                # Base template file
├── addUrl.py                 # Python script to handle generation
└── README.md
```
