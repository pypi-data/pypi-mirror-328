from setuptools import setup, find_packages

setup(
    name="safepandas",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your-email@example.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

