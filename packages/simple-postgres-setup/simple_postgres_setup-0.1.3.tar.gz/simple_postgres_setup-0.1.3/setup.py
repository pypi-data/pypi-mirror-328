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
    'version': '0.1.3',
    'description': 'simple_postgres_setup is a python utility for deploying PostgreSQL databases from a yaml configuration file.',
    'long_description': '# simple_postgres_setup\n\nThis package provides two main functions for **managing a PostgreSQL database**:\n\n1. **`setup_database("path_to_config.yml")`**  \n   Sets up a PostgreSQL database using:\n   - Credentials from your `.env` file  \n   - Additional parameters specified in your `config.yml`  \n\n2. **`drop_database("path_to_config.yml")`**  \n   Drops (tears down) the same PostgreSQL database, reverting changes made during the setup.\n\n---\n\n## scope\n\n1. define the database name\n2. define the database schemas and schema comments\n2.1 per schema there will be three default functional roles: \n    - schema_name_all  = all privileges regarding the schema are granted\n    - schema_name_use  = usage on existing schema assets are granted\n    - schema_name_read = only select on tables is granted\n3. define the login roles (users)\n4. define the access policies for the users by connecting the login roles with the functional roles per schema (see example configuration in the template subfolder)\n\n---\n\n## usage\n\n- install with pip (see installation) or other package manager\n- create directory \n- create config.yml and .env in the directory (use template files provided in the \'template\' subfolder of this pacakge) \n- define output directory in your config.yml as a relative path from the directory you execute the functions from, e.g. THIS directory\n- provide all required input in the .env and config.yml files\n- run setup\n\n---\n\n## Requirements\n\n- Python 3.10+  \n- An existing PostgreSQL server/cluster with Postgreql > 13\n- A `.env` file containing the following DB connection parameters (e.g., hostname, port, user credentials):\n\n```sh\n# database connection variables\n\nHOST=some_host \nPORT=\'some_port_number\'\nDB=postgres # this whole software only works with postgres\nUSER=postgres_or_other_superuser\nPWD=some_password\n```\n\n- A `config.yml` specifying how to configure the database and where to store output artifacts. \n\n**NOTE:** An example configuration file is included in the `templates` subfolder of this package: `templates/config.yml.example`\n```\n\n\n---\n\n## Installation\n\n1. Make sure you have `pip` installed (or use Poetry / another compatible Python package manager).\n2. Install from PyPI (or from source) by running:\n\n   ```bash\n   pip install simple_postgres_setup\n   ```\n',
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
