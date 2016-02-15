import os
from setuptools import setup, find_packages
# import sys
# reload(sys).setdefaultencoding("UTF-8")

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-webodt',
    version='0.3.2',
    author='NetAngels',
    author_email='info@netangels.ru',
    packages=find_packages(),
    url='http://github.com/netangels/django-webodt',
    license='BSD License',
    description=u'ODF template handler and odt to html, pdf, doc, etc converter',
    long_description=README,
    install_requires=[
        'Django==1.9.2',
        'lxml==3.5.0',
    ],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
