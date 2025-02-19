from setuptools import setup, find_packages

VERSION = "0.0.4"
DESCRIPTION = "AI 4 Clinic"
LONG_DESCRIPTION = "AI 4 Clinic"

setup(
    name="ai4clinic",
    version=VERSION,
    author="Katyna Sada del Real, Josefina Arcagni",
    author_email="ksada@unav.es",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=1.5.0",
        "torch>=2.0.0",
        "torchmetrics>=0.11.0"
    ],
    keywords=["python", "first package"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

