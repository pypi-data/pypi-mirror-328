from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="candleweb-ai",
    version="0.1.2",
    description="A custom tool for Candleweb AI Agents developers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Candleweb Power Developers",
    author_email="ai@candleweb.com",
    url="https://github.com/edfolmi/candleweb-ai",
    packages=find_packages(),
    install_requires=[
        "crewai>=0.95.0",
        "pydantic>=1.10",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
