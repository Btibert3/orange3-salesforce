# Installation Guide

## Prerequisites

- Python 3.11 or higher
- Orange3 installed and working
- Git (for source installation)

## Installation Methods

### Method 1: Install from PyPI (Recommended)

```bash
pip install orange3-salesforce
```

### Method 2: Install from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/btibert3/orange3-salesforce.git
   cd orange3-salesforce
   ```

2. Install in development mode:
   ```bash
   pip install -e .
   ```

## Verification

After installation, you should see "Salesforce" in your Orange3 widget palette under the "Salesforce" category.

## Troubleshooting

### Widgets not appearing
- Make sure Orange3 is restarted after installation
- Check that the package was installed correctly: `pip list | grep orange3-salesforce`
- Verify the entry points in `pyproject.toml`

### Import errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version compatibility (3.11+)

### Connection issues
- Verify your Salesforce credentials
- Check if your IP is whitelisted in Salesforce
- Ensure you have the correct security token if using username/password auth

## Testing

Run the basic test to verify installation:
```bash
python test_basic.py
```

## Next Steps

1. Open Orange3
2. Look for "Salesforce" widgets in the widget palette
3. Try the example workflow: `example_workflow.ows`
4. Connect to your Salesforce org and fetch some data!
