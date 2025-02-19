from setuptools import setup, find_packages

setup(
    name="bornvita",
    version="0.1.0",
    author="Raghav Dadhich",
    author_email="dadhichraghav896@gmail.com",
    description="Generate full-screen Bornvita Brainrot messages!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/raghav3615/bornvita",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bornvita=bornvita.brainrot:generate_brainrot"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
