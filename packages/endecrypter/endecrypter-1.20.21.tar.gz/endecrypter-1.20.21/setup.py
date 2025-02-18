from setuptools import setup, find_packages

setup(
    name="endecrypter",
    version="1.20.21",
    packages=find_packages(),
    install_requires=[
        "pycryptodome>=3.21.0",
        "numpy>=2.2.3"
    ],
    author="Elabsurdo984",
    author_email="matiassfernandez00@gmail.com",
    description="A comprehensive encryption/decryption library",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Elabsurdo984/EnDecrypter.git",
    python_requires=">=3.12",
    license='GPL',
    project_urls={
        "Source": "https://github.com/Elabsurdo984/EnDecrypter"
    }
)