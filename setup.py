from setuptools import setup,find_packages

setup(
  name = 'git-search',
  packages = find_packages(),
  version = '1.1.8',
  description = 'Search text in commits',
  author = 'Siddharh Jain,Arun Kumar',
  author_email = 'sidj242@gmail.com,arun6582@gmail.com',
  url = 'https://github.com/sidj242/git-search/', # use the URL to the github repo
  keywords = ['git search','commit search'], # arbitrary keywords
  classifiers = [],
  install_requires = [],
  scripts=["bin/git-search"],
)
