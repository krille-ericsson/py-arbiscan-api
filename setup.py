import setuptools

setuptools.setup(
    name='py_arbiscan_api',
    version='0.9.0',
    packages=['examples', 'examples.stats', 'examples.tokens',
              'examples.accounts', 'examples.blocks', 'examples.transactions',  'arbiscan'],
    url='https://github.com/krille-ericsson/py-arbiscan-api.git',
    license='MIT',
    author='Christian Ericsson',
    author_email='',
    description='Python Bindings to Arbitrum Block Explorer API',
    install_requires=[
        'requests>=2.20.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
