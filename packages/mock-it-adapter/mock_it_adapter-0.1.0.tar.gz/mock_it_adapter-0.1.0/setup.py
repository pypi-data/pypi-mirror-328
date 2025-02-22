from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name="mock_it_adapter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.3",
        "pydantic>=2.0.0",
    ],
    author="Vorobev Aleksei",
    author_email="aleksei.suzume@gmail.com",
    description="A Python mock_it_adapter for Mock IT API",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_api_adapter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
