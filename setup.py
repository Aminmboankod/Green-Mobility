import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Green-Mobility",
    version="0.0.1",
    author="Amin Mustafa & Antonio Maroto",
    author_email="amustafaboankod@cifpfbmoll.eu & amarotoblasco@cifpfbmoll.eu",
    description="Rental website for bikes",
    long_description="Project to create a bicycle rental website with Python",
    long_description_content_type="text/markdown",
    url="https://github.com/Aminmboankod/Green-Mobility",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.10",
    install_requires=[
        "attrs==22.1.0",
        "certifi==2022.9.24",
        "charset-normalizer==2.1.1",
        "coverage==6.5.02",
        "exceptiongroup==1.0.4",
        "gitdb==4.0.10",
        "GitPython==3.1.29",
        "idna==3.4",
        "iniconfig==1.1.1",
        "packaging==21.3",
        "pluggy==1.0.0",
        "pyparsing==3.0.9",
        "pytest==7.2.0",
        "requests==2.28.1",
        "smmap==5.0.0",
        "tomli==2.0.1",
        "urllib3==1.26.13",
    ],
)


