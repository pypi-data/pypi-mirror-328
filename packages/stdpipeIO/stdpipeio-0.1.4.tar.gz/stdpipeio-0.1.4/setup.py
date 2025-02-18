from setuptools import setup, find_packages

setup(
    name='stdpipeIO',
    version='0.1.4',
    author='Greendog',
    author_email='x6reend0g@foxmail.com',
    description='A simple decorator for receiving and sending data via the standard pipe',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    test_suite="tests",
)
