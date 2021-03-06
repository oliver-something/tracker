from setuptools import setup

setup(
    name='tracker',
    version='0.1',
    py_modules=['tracker','tables', 'req'],
    install_requires=[
       'certifi==2020.12.5',
        'chardet==4.0.0',
        'click==7.1.2',
        'colored==1.4.2',
        'idna==2.10',
        'prettytable==2.0.0',
        'pyfiglet==0.8.post1',
        'requests==2.25.1',
        'urllib3==1.26.3',
        'wcwidth==0.2.5',
    ],
    entry_points='''
        [console_scripts]
        tracker=tracker:cli
    ''',
)