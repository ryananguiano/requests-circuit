from setuptools import find_packages, setup

version = __import__('requests_circuit').__version__

setup(
    name='requests-circuit',
    version=version,
    url='https://www.github.com/ryananguiano/requests-circuit',
    author='Ryan Anguiano',
    description=('A circuit breaker for Python requests'),
    license='MIT',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    install_requires=[
      'requests',
      'six',
    ],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
