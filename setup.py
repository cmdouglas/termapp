from setuptools import setup

setup(
    name='termapp',
    version='0.1',
    description='Mini-framework for developing terminal applications',
    url='https://github.com/cdouglas/termapp',
    author='Charlie Douglas',
    author_email='cmdouglas@gmail.com',
    license='MIT',
    packages=['termapp'],
    install_requires=[
        'blessed>=1.9.5',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ]
)
