# Orange3-Salesforce

This allows users to interact and manage data in Salesforce directly within Orange3. This is only possible because of the fantastic library [simple-salesforce](https://github.com/simple-salesforce/simple-salesforce).

## Installation

### Option 1: Install via Orange3 Add-ons Manager (Recommended)
1. Open Orange3
2. Go to Options → Add-ons
3. Click "Add more..." 
4. Search for "orange3-salesforce"
5. Click Install

### Option 2: Install from Source
```bash
git clone https://github.com/yourusername/orange3-salesforce.git
cd orange3-salesforce
pip install -e .
```

**Note**: This extension uses the `orangeaddons` namespace to avoid conflicts with existing Orange3 packages.

## Features

### Current (MVP)
- **Salesforce Authentication Widget**: Connect to Salesforce orgs using username/password + security token
- **Salesforce Query Widget**: Execute SOQL queries and retrieve data as Orange3 tables
- Support for Contacts and Opportunities objects
- Simple dropdown selection for common objects

### Planned
- Bulk create, update, and delete operations
- Data validation and error handling
- Support for custom objects
- Advanced SOQL query builder

## Usage

### Basic Workflow
1. **Connect**: Use the Salesforce Authentication widget to connect to your org
2. **Query**: Use the Salesforce Query widget to retrieve data
3. **Analyze**: Use Orange3's built-in data analysis tools on your Salesforce data

### Example Workflow
1. Drag "Salesforce Authentication" widget to canvas
2. Enter your Salesforce credentials and click "Connect"
3. Drag "Salesforce Query" widget to canvas
4. Connect the authentication output to the query input
5. Select an object (Contact/Opportunity) and execute query
6. View results in Orange3's data table

## Requirements

- Orange3
- Python 3.7+
- simple-salesforce
- requests
- pandas

## Development

### Project Structure
```
orange3-salesforce/
├── setup.py                 # Package installation
├── requirements.txt         # Dependencies
├── orangecontrib/          # Orange3 convention
│   └── salesforce/         # Our extension
│       ├── widgets/        # Widget definitions
│       │   ├── auth.py     # Authentication widget
│       │   └── query.py    # Query widget
│       └── icons/          # Widget icons
└── README.md
```

### Adding New Widgets
1. Create new widget class in `orangecontrib/salesforce/widgets/`
2. Inherit from appropriate Orange3 widget base class
3. Register in `orangecontrib/salesforce/widgets/__init__.py`
4. Add icon to `icons/` directory

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
1. Check the Orange3 documentation
2. Review simple-salesforce documentation
3. Open an issue on GitHub


## TO BE DELETED

Local testing

```
/Applications/Orange.app/Contents/MacOS/PythonApp -m pip install docopt
```




