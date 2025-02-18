from setuptools import setup, find_packages

setup(name='ida-db',
      version='2025.02.17.1841',
      url='https://github.com/project-ida/ida-db',
      license='MIT',
      author='Florian Metzler',
      author_email='fmetzler@mit.edu',
      description='Interface to Timescale PostgreSQL database',
      packages=find_packages(),
      install_requires=['psycopg2', 'numpy'],
      zip_safe=False)
