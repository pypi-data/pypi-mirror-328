from setuptools import setup, find_packages

# requirements = [line.strip() for line in open('requirements.txt', 'r').readlines()]


setup(
    name = 'my_lib_api',
    version='0.1',
    packages=find_packages(),
    install_requires = [
        'Flask>=3.1.0',
        'Flask-SQLAlchemy>=3.1.1'
    ],
    include_package_data=True,
    package_data={
        'my_lib_api' : ['templates/*']
    }
)

# print(requirements)