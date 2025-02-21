from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="recursion2loop",
    version="0.2.0",
    packages=find_packages(include=["recursion2loop", "recursion2loop.*"]),
    description="conversion of recursive functions to iterative implementations. Optimize your Python code by transforming stack-heavy recursion into efficient loops.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Adil Köken',
    author_email='mail@adilkoken.com',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    url='https://github.com/AdilKoken/recursion2loop',
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

