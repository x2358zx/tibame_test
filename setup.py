import os
from io import open

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="py_test",  # Required
    version="0.0.1",  # Required
    description="test",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    author="rita",  # Optional
    author_email="x2358zx73@gmail.com",  # Optional
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
    ],
    #packages=find_packages(where="src"),
    #package_dir={"": "src"},
)
