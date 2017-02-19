import codecs
from setuptools import setup
try:
    import pypandoc
    is_travis = False
except ImportError as e:
    import os
    if not 'TRAVIS' in os.environ:
        raise ImportError(e)
    else:
        is_travis = True


def _create_log_desc(travis):
    if is_travis:
        return ''
    _long_desc = ''
    with codecs.open('README.rst', 'w', 'utf-8') as rf:
        _long_desc = pypandoc.convert('README.md', 'rst')
        rf.write(_long_desc)
    return _long_desc
long_desc = _create_log_desc(is_travis)

setup(name='cronquot',
      version='0.0.7',
      description='Cron scheduler.',
      long_description=long_desc,
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries :: Python Modules'
          ],
      keywords='cron crontab schedule',
      author='Shohei Mukai',
      author_email='mukaishohei76@gmail.com',
      url='https://github.com/pyohei/cronquot',
      license='MIT',
      packages=['cronquot'],
      entry_points={
          'console_scripts': [
              'cronquot = cronquot.cronquot:execute_from_console'],
          },
      install_requires=['crontab'],
      test_suite='test' 
      )
