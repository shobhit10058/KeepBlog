from setuptools import setup

setup(
    name='KeepBlog',
    version='0.1',
    py_modules=['KeepBlog'],
    install_requires=[
        'Click','validators'
    ],
    entry_points='''
        [console_scripts]
        KeepPages=KeepPages:main
    ''',
)