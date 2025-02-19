from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="surfercid-client",
    version="0.1.48",
    author="SurferCID",
    author_email="HeySurfers@protonmail.com",  # Replace with your email
    description="A Python client for the SurferCID API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://documenter.getpostman.com/view/15842770/2s9YJW55kQt",
    packages=find_packages(exclude=["examples*", "tests*", "docs*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.31.0",
    ],
    keywords="surfercid, api, client, token",
    include_package_data=True,
    exclude_package_data={
        '': ['.gitignore', '.pypirc', 'build.py', '*.log'],
        'examples': ['*'],
        'tests': ['*'],
        'docs': ['*'],
    },
) 