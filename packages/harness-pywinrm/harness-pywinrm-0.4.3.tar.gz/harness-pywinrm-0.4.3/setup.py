from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="harness-pywinrm",
    version="0.4.3", 
    packages=find_packages(),
    install_requires=[
        'pykerberos',
        'pywinrm',
    ],
    extras_require={
        'test': ['unittest'],
    },
    entry_points={
        'console_scripts': [
            'harness-pywinrm = harness_pywinrm.pywinrm:main',
        ],
    },
    author="Ivan Mijailovic",
    author_email="ivansrbija@yahoo.com",
    description="CLI for Windows Remote Management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wings-software/winrm-kerberos-pywinrm", 
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
