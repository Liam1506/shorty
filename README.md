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

```text
├── .github/
│   └── workflows/
│       └── new_issue.yml    # Workflow config file
├── index.html                # Base template file
├── addUrl.py                  # Python script to handle generation
└── README.md
```

### 3. Add a Website

To create a new short link / redirect page:

1. Click the **Issues** tab at the top of the repository.
2. Click **New Issue** (or select the **Create New Short Link** template).
3. Fill out the form:
   - **Title (Short Code):** Enter your desired folder name (e.g., `test2`).
   - **Target URL:** Enter the full destination link (e.g., `https://example.com/destination`).
4. Click **Submit new issue**.

The GitHub Action will automatically run, create the new folder with an `index.html` file, and commit the changes directly to your repository!
