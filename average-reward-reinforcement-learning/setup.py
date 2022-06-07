from setuptools import find_packages
import os

from distutils.core import setup



packages = find_packages()

setup(name='average-reward-reinforcement-learning',
      version='v1',
      packages=packages,
      install_requires=['gym', 'numpy','scipy', 'joblib', 'matplotlib', 'networkx']  # And any other dependencies foo needs
)

