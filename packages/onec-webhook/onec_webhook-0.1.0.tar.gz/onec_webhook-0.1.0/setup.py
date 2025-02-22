from setuptools import setup, find_packages

setup(
    name="onec_webhook",  # Уникальное имя на PyPI
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",  # Зависимости
    ],
    author="Muresda",
    author_email="ads.bagan@yandex.ru",
    description="Python-библиотека для интеграции с системой взаимодействия 1С",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Muredsa/onec_webhook",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
