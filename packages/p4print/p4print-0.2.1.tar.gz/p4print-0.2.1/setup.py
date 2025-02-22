from setuptools import setup, find_packages

setup(
    name="p4print",
    version="0.2.1",
    packages=find_packages(),
    description="Use 'p()' instead of 'print()' in Python",
    long_description=open("README.md", encoding="utf-8").read(),  # Ensure README.md exists
    long_description_content_type="text/markdown",
    author="Ashish Kumar",
    author_email="ashish.jnu@outlook.com",
    url="https://github.com/AshishKumarCS/p4print",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)
