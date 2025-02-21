import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hhhhhhhhhhhhhhhhhhhhh",
    version="12.0.9",
    author="ZZL",
    url='http://www.baidu.com',
    author_email="sdfds@qq.com",
    description="xxx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
