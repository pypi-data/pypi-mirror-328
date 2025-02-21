from setuptools import setup, find_packages

setup(
    name="lqcodeAI",
    version="1.1.9",  # 直接在这里指定版本号
    author="TivonFeng",
    author_email="tivonfeng@163.com",
    description="绿旗编程AI课程SDK",
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