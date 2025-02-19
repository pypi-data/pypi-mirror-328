from setuptools import find_packages, setup
from setuptools_scm import get_version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    name="sais-prism",
    author="Shepard",
    author_email="zhaoxun@sais.com.cn",
    description="SAIS Prism: A unified interface for ML data access and lifecycle management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab-paas.internal.sais.com.cn/data_intelligence_platform/sais-prism",
    packages=find_packages(),
    install_requires=[
        "mlflow>=2.0.0",
        "PyYAML>=6.0",
        "transformers>=4.30.0",
        "torch>=2.0.0",
        "peft>=0.4.0",
    ],
    extras_require={
        "test": ["pytest>=7.0.0", "pytest-cov>=4.0.0", "pytest-mock>=3.10.0"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
