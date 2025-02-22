from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name="simple_system_ot_bank",
    version='0.0.1',
    author='KuroKagami',
    author_email="jeangabriel0990@gmail.com",
    description='Simple Banking System',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url="https://github.com/kurokagami/python-optimize-fundamentals",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.12',
)