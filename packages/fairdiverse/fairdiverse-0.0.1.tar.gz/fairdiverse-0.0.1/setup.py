from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import os

from setuptools import setup, find_packages

install_requires = [
    "numpy>=1.20.3",
    "torch>=1.11.0",
    "PyYAML>=6.0",
    "pandas>=1.2.0",
    "scipy",
    "cvxpy",
    "tqdm>=4.65.0",
    "scikit_learn",
]

setup_requires = []


classifiers = ["License :: OSI Approved :: MIT License"]

long_description = (
    "FairDiverse is developed based on Python for "
    "reproducing and developing fairness- and diversity-aware "
    "IR algorithms in a unified, comprehensive framework for "
    "research purpose. In the first version, our library "
    "includes 28 fairness- and diversity algorithms and 16 base models, covering "
    "pre-processing, in-processing and post-processing"
    "for more information: https://github.com/XuChen0427/FairDiverse"
)

# Readthedocs requires Sphinx extensions to be specified as part of
# install_requires in order to build properly.
on_rtd = os.environ.get("READTHEDOCS", None) == "True"
if on_rtd:
    install_requires.extend(setup_requires)

setup(
    name="fairdiverse",
    version="0.0.1",  # please remember to edit recbole/__init__.py in response, once updating the version
    description="A unified, comprehensive fairness- and diversity-aware IR library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XuChen0427/FairDiverse",
    author="Chen Xu",
    author_email="chenxu0427ruc@gmail.com",
    #packages=find_packages(),
    packages=[package for package in find_packages() if package.startswith("fairdiverse")],
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
    extras_require=None,
    zip_safe=False,
    classifiers=classifiers,
    python_requires=">=3.6",
)