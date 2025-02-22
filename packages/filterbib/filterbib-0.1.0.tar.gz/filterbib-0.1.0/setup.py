from setuptools import setup, find_packages

setup(
    name="filterbib",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    scripts=[
        "filterbib/filter_bib",
        "filterbib/read_bib"
    ]
)
