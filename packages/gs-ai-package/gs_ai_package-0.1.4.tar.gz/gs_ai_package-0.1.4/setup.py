from setuptools import setup, find_packages

setup(
    name="gs_ai_package",  # Nome del tuo pacchetto su PyPI (univoco se lo pubblichi)
    version="0.1.4",
    author="PietroCosseddu",
    author_email="pietro.cosseddu@green-share.it",
    description="Package per associare a dati trasporto pubblico la direzione della tratta",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://gitlab.greenshare.it/pietro.cosseddu/gs-ai-package.git",
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
