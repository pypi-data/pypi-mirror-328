import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datahyde", 
    version="0.0.2",
    author="Ani Kulkarni",
    author_email="aniruddha.k1911@gmail.com",
    description="A package to encrypt/decrypt the images/data using ""SMART"" Image Processing Algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akulka404/datahyde",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers" 
    ],
    python_requires='>=3.6',
    keywords=["cryptography","Encryption","Decryption","Image Processing"],
    license="MIT",include_package_data=True,zip_safe=True,
)