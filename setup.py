from setuptools import setup

setup(
  name='Flask CMS',
  version='0.0.1',
  packages=['flask_cms'],
  include_package_data=True,
    install_requires=[
      'flask',
      'flask-sqlalchemy',
      'flask-migrate',
    ]

)