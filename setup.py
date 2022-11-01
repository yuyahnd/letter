from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='letter',
    version='0.0.1',
    license='MIT',
    description='Letter of the simple document creation tool',
    author='Yuya Honda',
    url='https://github.com/yuyahnd/letter',
    packages=find_packages(),
    py_modules=[splitext(basename(path))[0] for path in glob('./*.py')],
    include_package_data=True,
    zip_safe=False,
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
