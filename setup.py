from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

setup(
    name='common',
    version='0.1.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
    description='Utilities for webinar.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Gerardo Roa Dabike',
    author_email='g.roadabike@salford.ac.uk',
    license='MIT',
    packages=find_packages(),
    keywords=['audio', 'hearing', 'loss', 'music', 'sound', 'cadenza', 'clarity'],
    install_requires=[
        REQUIREMENTS
    ],
)
