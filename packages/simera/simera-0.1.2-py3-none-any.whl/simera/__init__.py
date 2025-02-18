import toml


# Read the version from pyproject.toml
def get_version():
    # Read pyproject.toml
    with open("pyproject.toml", "r") as f:
        pyproject_data = toml.load(f)

    # Get version from pyproject.toml
    return pyproject_data["project"]["version"]

# Set the __version__ attribute
__version__ = get_version()
