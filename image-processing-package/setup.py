from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='image-processing-henrique0909',
    version='0.0.1',
    author='Henrique C. de Andrade',
    author_email='rique9906@gmail.com',
    description='A package to process images',
    long_description = page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/riqie/dio-suzano-python-developer/tree/main/image-processing-package',
    packages = find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)

