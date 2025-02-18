from setuptools import setup, find_packages

setup(
    name="codejump",
    version="0.1.3",
    packages=find_packages(),
    description="A Python library for controlled code jumps using checkpoints and teleportation.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Ami",
    author_email="amishgupta@outlook.com",
    url="https://github.com/Ami-sh/codejump",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)