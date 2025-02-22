from setuptools import setup, find_packages

setup(
    name="perchance-dsl",
    version="0.1.1",
    author="Ehre",
    description="A DSL for replacing if-else statements with a more readable syntax",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ehrev/perchance-dsl",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "perchance=perchance.runner:run_perchance_script"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
