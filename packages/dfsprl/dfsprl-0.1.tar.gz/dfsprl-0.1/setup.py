from setuptools import setup, find_packages

setup(
    name='dfsprl',
    version='0.1',
    description='Real-time anomaly detection for streaming data',
    author='Your Name',
    author_email='familybrokenist@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
