from setuptools import setup, find_packages

setup(
    name="lqcode",
    version="0.1.0",
    author="TivonFeng",
    author_email="tivonfeng@163.com",
    description="个人信息管理模块",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TivonFeng/lqcode",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)