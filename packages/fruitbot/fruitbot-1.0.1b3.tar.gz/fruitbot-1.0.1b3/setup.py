from setuptools import setup, find_packages

with open("README.md", encoding="UTF-8") as f:
    readme = f.read()

setup(
    name="fruitbot",
    version="1.0.1b3",
    packages=find_packages(),
    install_requires=["urllib3", "colorama"],
    author="Amir S.Farahani",
    url="https://github.com/AmirSF01/fruitcraft",
    description="A simple, easy-to-use and powerful library for automating gameplay in the Fruit Craft game through APIs.",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Real Time Strategy",
    ],
    keywords=["fruit", "craft", "fruitcraft", "fruitbot", "bot", "api", "client", "automating", "card", "game"],
    python_requires=">=3.7"
)