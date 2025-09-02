# c4-components-analyzer

## Overview
This project is designed to analyze components and relationships in a C4 model diagram specifically for an Java Monolite project. It provides a structured approach to identify and represent various elements of the system architecture.

## Project Structure
```
c4-components-analyzer
├── src
│   ├── main.py                # Entry point of the application
│   ├── components             # Contains definitions for component types
│   │   └── __init__.py
│   ├── relationships          # Defines relationships between components
│   │   └── __init__.py
│   ├── utils                  # Utility functions for analysis
│   │   └── __init__.py
│   └── types                  # Type definitions and interfaces
│       └── index.py
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to ignore in version control
└── paths.properties           # paths info

```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd <directory>
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create paths into paths.properties: CONTROLLERS_PATH - SERVICES_PATH - REPOSITORIES_PATH

## Usage
To run the application, execute the following command:
```
python src/main.py
```

This will initialize the application and start the analysis of the C4 model components and relationships.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.