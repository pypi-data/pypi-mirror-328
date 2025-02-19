from setuptools import setup, find_packages

setup(
    name="replicats-tvdatafeed",
    version="0.1.0",
    author="Lucas Fonseca",
    author_email="lucasfonmiranda@gmail.com",
    description="Test.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/replicatsai/replicats-tvdatafeed",
    packages=find_packages(),
    install_requires=[
        "requests",  # Adicione outras dependências aqui
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
