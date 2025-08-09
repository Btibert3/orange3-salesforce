from setuptools import setup, find_packages

setup(
    name="orange3-salesforce",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Orange3",
        "simple-salesforce",
        "requests",
    ],
                    entry_points={
                    "orange.widgets": (
                        "Salesforce = orangeaddons.sfdata.widgets",
                    ),
                },
    keywords=[
        "orange3 add-on",
        "salesforce",
        "data mining",
        "machine learning",
        "data integration"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",

        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    include_package_data=True,
    zip_safe=False,
)
