import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secuuthJwtPythonSdk",
    version="0.3",
    author="secuuth",
    author_email="amitoshkumar10@gmail.com",
    description="secuuth  SDK for python scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akum304/secuuthJwtPythonSdk.git",
    packages=["secuuthJwtPythonSdk"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "python-jose", "cryptography"]
)
