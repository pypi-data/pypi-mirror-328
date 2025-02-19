from setuptools import setup, find_packages

# Ensure README.md is read with UTF-8 encoding
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pptx-editor",
    version="0.1.2",
    packages=find_packages(),
    install_requires=["python-pptx"],
    description="A Python library for navigating PowerPoint slides and adding a red dot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/pptx_editor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
