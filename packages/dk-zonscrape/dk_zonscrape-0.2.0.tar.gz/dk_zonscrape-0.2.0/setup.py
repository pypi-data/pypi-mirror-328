from setuptools import setup, find_packages

setup(
    name="dk_zonscrape",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "httpx",
        "beautifulsoup4",
        "pydantic"
    ],
    author="DK",
    author_email="dibas9110@gmail.com",
    description="A package for scraping Amazon product details using ASIN",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dibas9110/amazon_scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
) 