from setuptools import setup

setup(
    name='KeepBlog',
    version='0.1',
    py_modules=['KeepPages'],
    install_requires=[
        'Click','validators'
    ],
    entry_points='''
        [console_scripts]
        KeepBlog=KeepPages:main
    ''',
)