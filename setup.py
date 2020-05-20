from setuptools import setup

setup(
  name='flask_cms',
  packages=['flask_cms'],
  include_package_data=True,
    install_requires=[
      'flask',
      'python-dotenv'
    ]

)