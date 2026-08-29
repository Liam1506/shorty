# Shorty

Shorty is a URL shortener that runs entirely on GitHub Issues, GitHub Actions, and GitHub Pages — no server or database required.

Open an issue with a short code and a target URL, and a workflow automatically generates a redirect page for it. Close the issue, and the redirect page is removed again.

## How It Works

1. You open a GitHub Issue specifying a short code and a target URL.
2. A GitHub Action triggers a Python script (`add_page.py`), which creates a new folder named after your short code containing an `index.html` that redirects to your target URL. The change is committed directly to the repo.
3. GitHub Pages serves that folder, so `https://<your-username>.github.io/shorty/<short-code>/` redirects visitors to your target URL.
4. When you close the issue, another script (`remove_page.py`) deletes the folder, taking the short link down.

## How to Set It Up

### 1. Repository Permissions (Required)

For GitHub Actions to create and commit new files to your repository, you must enable **Write** permissions:

1. Go to **Settings** -> **Actions** -> **General**.
2. Scroll down to **Workflow permissions**.
3. Select **Read and write permissions**.
4. Click **Save**.

### 2. Enable GitHub Pages

1. Go to **Settings** -> **Pages**.
2. Under **Source**, select the branch (e.g. `main`) that the Action commits to.
3. Save. Your shortener will be live at `https://<your-username>.github.io/shorty/`.

### 3. File Structure

```text
├── .github/
│   └── workflows/          # Workflow config files
├── example/                 # Example short link page
├── index.html                # Base template / landing page
├── template.html              # Template used to generate redirect pages
├── add_page.py                 # Creates a redirect page on issue creation
├── remove_page.py               # Deletes the redirect page on issue close
├── LICENSE
└── README.md
```

### 4. Add a Short Link

To create a new short link / redirect page:

1. Click the **Issues** tab at the top of the repository.
2. Click **New Issue** (or select the **Create New Short Link** template).
3. Fill out the form:
   - **Title (Short Code):** Enter your desired short link name (e.g., `example`).
   - **Target URL:** Enter the full destination link (e.g., `https://example.com/`).
4. Click **Submit new issue**.

The GitHub Action will automatically run, create the new folder with an `index.html` file, and commit the changes directly to your repository!

### 5. Remove a Short Link

Close the issue that created it, and the corresponding folder and redirect page are automatically removed.

## Demo

Try it out: <https://liam1506.github.io/shorty/>

## License

Released under the [MIT License](LICENSE).
