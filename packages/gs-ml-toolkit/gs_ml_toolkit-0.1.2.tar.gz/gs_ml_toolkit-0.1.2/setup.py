from setuptools import setup, find_packages

setup(
    name="gs_ml_toolkit",  
    version="0.1.2",
    author="PietroCosseddu",
    author_email="pietro.cosseddu@green-share.it",
    description="Package per trattare dati di trasporto pubblico e semplificare l'utilizzo di questi in progetti AI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://gitlab.greenshare.it/rombo-ai/gs_ml_toolkit.git",
    packages=find_packages(),  
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
