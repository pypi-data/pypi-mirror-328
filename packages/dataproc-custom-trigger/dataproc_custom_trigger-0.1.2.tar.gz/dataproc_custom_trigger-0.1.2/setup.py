from setuptools import setup, find_packages

setup(
    name="dataproc_custom_trigger",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "apache-airflow>=2.2",  # ajusta según tus necesidades
        "apache-airflow-providers-google>=6.0.0",  # ajusta la versión necesaria
    ],
)
