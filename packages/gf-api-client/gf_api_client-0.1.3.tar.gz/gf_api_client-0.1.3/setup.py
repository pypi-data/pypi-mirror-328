from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gf-api-client",
    version="0.1.3",
    author="GF",
    author_email="tanzhixiong@gf.com.cn",
    description="广发证券开放平台 API 客户端",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.31.0",
        "pandas>=2.0.0",
    ],
)
