# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hasura_metadata_manager',
 'hasura_metadata_manager.aggregate_expression',
 'hasura_metadata_manager.auth_config',
 'hasura_metadata_manager.base',
 'hasura_metadata_manager.boolean_expression_type',
 'hasura_metadata_manager.compatibility_config',
 'hasura_metadata_manager.data_connector',
 'hasura_metadata_manager.data_connector.capability',
 'hasura_metadata_manager.data_connector.field_map',
 'hasura_metadata_manager.data_connector.function',
 'hasura_metadata_manager.data_connector.procedure',
 'hasura_metadata_manager.data_connector.representation',
 'hasura_metadata_manager.data_connector.scalar_type',
 'hasura_metadata_manager.data_connector.schema',
 'hasura_metadata_manager.data_connector.schema.collection',
 'hasura_metadata_manager.data_connector.schema.collection.field',
 'hasura_metadata_manager.data_connector.schema.scalar_type',
 'hasura_metadata_manager.data_connector.type_definition',
 'hasura_metadata_manager.data_connector_scalar_representation',
 'hasura_metadata_manager.data_contracts',
 'hasura_metadata_manager.graphql_config',
 'hasura_metadata_manager.lifecycle_plugin_hook',
 'hasura_metadata_manager.mixins',
 'hasura_metadata_manager.mixins.rdf',
 'hasura_metadata_manager.mixins.temporal',
 'hasura_metadata_manager.model',
 'hasura_metadata_manager.model.orderable_field',
 'hasura_metadata_manager.model_permission',
 'hasura_metadata_manager.model_permission.filter',
 'hasura_metadata_manager.object_type',
 'hasura_metadata_manager.object_type.field',
 'hasura_metadata_manager.relationship',
 'hasura_metadata_manager.role',
 'hasura_metadata_manager.subgraph',
 'hasura_metadata_manager.supergraph',
 'hasura_metadata_manager.type_permission',
 'hasura_metadata_manager.utilities']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=2.0.36,<3.0.0',
 'diskcache>=5.6.3,<6.0.0',
 'jsonschema>=4.23.0,<5.0.0',
 'matplotlib>=3.9.3,<4.0.0',
 'networkx>=3.2.1,<4.0.0',
 'numpy>=2.0.2,<3.0.0',
 'opentelemetry-instrumentation-openai>=0.37.1,<0.38.0',
 'pandas>=2.2.3,<3.0.0',
 'psycopg2-binary',
 'pydantic>=2.10.5,<3.0.0',
 'pytest>=8.3.4,<9.0.0',
 'python-json-logger==2.0.7',
 'pytz>=2024.2,<2025.0',
 'rdflib-neo4j>=1.1,<2.0',
 'rdflib>=7.1.2,<8.0.0']

setup_kwargs = {
    'name': 'hasura-metadata-manager',
    'version': '0.1.2',
    'description': 'Tracks a normalized database of a Hasura DDN build across time.',
    'long_description': None,
    'author': 'Kenneth Stott',
    'author_email': 'kenneth.stott@hasura.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
