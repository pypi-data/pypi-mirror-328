# Python Template

Template for general `Python` development.

## Development Workflow

First, a local project environment needs to be created, then the project's modules will be installed into locally into a virtual environment.

1. Clone the repository.

   ```sh
   git clone https://github.com/bellanov/python-template.git
   cd python-template
   ```

2. Create a virtual environment.

   ```sh
   # Create Virtual Environment
   python3 -m venv .venv

   # Activate Virtual Environment
   source .venv/bin/activate

   # Install Dependencies
   pip install -r requirements.txt 

   # Deactivate Virtual Environment
   deactivate
   ```

3. Make your changes, increment the version in `pyproject.toml`, and **build** the application.

   ```sh
   # Build a Python package distribution
   scripts/build.sh

   # Publish a distribution to PyPi (testpypi)
   scripts/release.sh

   # Install the Python package locally, from testpypi.
   scripts/install.sh "<VERSION>"

   # Execute Unit Tests
   scripts/test.sh

   # Execute Code Samples
   scripts/examples.sh

   # Lint Code Base
   scripts/lint.sh
   ```