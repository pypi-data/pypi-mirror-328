# setup.py
from setuptools import setup, find_packages

setup(
    name="llm_factory_tag",
    version="0.2.0",
    author="Hasan",
    description="Een package om LLM modellen te initialiseren op basis van provider.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "anthropic",
        "openai",
        "pydantic_ai",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
