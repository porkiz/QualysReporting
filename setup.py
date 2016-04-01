from setuptools import setup, find_packages

setup(
    name='QualysReporting',
    version='0.2.6dev',
    install_requires=['requests', 'sqlalchemy', 'psycopg2', 'certifi',
                      'selenium'],
    packages=find_packages(),
    package_data={'qgreports': ['config/*']},
    url='https://github.com/dmwoods38/QualysReporting',
    license='MIT',
    author='dmwoods38',
    author_email='',
    description='Tool to help with automation of Qualys Scan Report delivery'
)
