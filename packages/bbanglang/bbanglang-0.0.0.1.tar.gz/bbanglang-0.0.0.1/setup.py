import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bbanglang",
    version="0.0.0.1",
    author="ILIKEERPIN",
    author_email="ILIKEERPIN@ERPIN.com",
    description="erpin-bbang-lang",
    long_description=open('README.md',encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ilikeerpin/erpin-bbang-lang",
    install_requires=[
                      
    ],
    include_package_data=True,
    python_requires=">=3.9.13", # 파이썬 최소 요구 버전
)