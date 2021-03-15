import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyetfoverlap",
    version="0.1",
    author="sorgmi",
    author_email="author@example.com",
    description="Calculate ETF overlap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sorgmi/pyetfoverlap",
    project_urls={
        "Bug Tracker": "https://github.com/sorgmi/pyetfoverlap/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)