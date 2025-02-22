from setuptools import setup, find_packages

setup(
    name="p4print",  # Updated package name
    version="0.1",
    packages=find_packages(),
    description="A simple package to use 'p()' instead of 'print()' for faster coding.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ashish Kumar",
    author_email="ashish.jnu@outlook.com",
    url="https://github.com/AshishKumarCS/p4print",  # Update GitHub repo (if needed)
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)