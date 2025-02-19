from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='neuropsy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PySide6',
        'reportlab',
    ],
    entry_points={
        'console_scripts': [
            'run-neuropsy=neuropsy.questions:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for neuropsychological tools and utilities.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/neuropsy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)