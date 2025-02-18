from setuptools import setup, find_packages

setup(
    name="bathini",
    version="0.1.4",
    packages=find_packages(),
    description="A package that introduces Bathini.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Bathini",
    author_email="shivduttchoubey@gmail.com",  # Replace with your email
    url="https://github.com/bathini/bathini",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)