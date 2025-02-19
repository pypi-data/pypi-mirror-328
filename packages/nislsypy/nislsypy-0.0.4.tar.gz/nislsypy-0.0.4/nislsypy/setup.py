from setuptools import setup, find_packages

setup(
    name='nislsypy',
    version='0.0.4',
    description='For flyexperiment in NISL, HYU, Seoul',
    author='Seongyeon Kim',
    author_email='sykim96500@gmail.com',
    url='https://github.com/SEONGYEONY/nislsypy',
    install_requires=['neo', 'numpy', 'scipy', 'scikit-learn', 'matplotlib'],
    packages=find_packages(exclude=[]),
    keywords=['Seongyeon', 'Anmo', 'drosophila', 'nisl', 'flylab'],
    python_requires='>=3.12',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.12',
    ],
)
