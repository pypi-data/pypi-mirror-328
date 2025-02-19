# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_postgres_setup',
 'simple_postgres_setup.code',
 'simple_postgres_setup.code.core',
 'simple_postgres_setup.code.utils']

package_data = \
{'': ['*'], 'simple_postgres_setup': ['templates/*']}

install_requires = \
['aiosql==10.2',
 'psycopg2-binary==2.9.6',
 'pyyaml==6.0.1',
 'sqlalchemy-utils==0.41.1',
 'sqlalchemy>=2.0.15,<3.0.0']

setup_kwargs = {
    'name': 'simple-postgres-setup',
    'version': '0.1.2',
    'description': 'simple_postgres_setup is a python utility for deploying PostgreSQL databases from a yaml configuration file.',
    'long_description': '# PyPG\nA python utility to deploy PostgreSQL databases from a configuration file\n\n### minimal dependencies:\n\nThe core library os is needed. Additionally you need \n\n- sqlalchemy (> 2.0.0)\n- sqlalchemy_utils (> 0.41.0)\n- pyyaml (>= 6.0)\n\nas specified in requirements.txt. Install these if they don\'t already exist in your environment with ```"pip install -r requirements.txt"```\n',
    'author': 'Matthias Daues',
    'author_email': 'matthias.daues@datenschoenheit.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
