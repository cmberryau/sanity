from setuptools import setup, find_packages

setup(name='sanity',
      version='2019.1',
      description='Reusable django app to stop you losing your mind',
      packages=find_packages(),
      install_requires=[
        'django',
        'django-celery-beat',
        'django-celery-results',
        'unittest-xml-reporting',
      ],
      include_package_data=True,
      zip_safe=False)
