from setuptools import setup, find_packages
setup(
  name = 'billplz-python',
  packages = find_packages(),
  version = '1.0.2',
  license='MIT',
  description = 'Billplz Client Interface',
  author = 'Matthew Cross',
  author_email = 'mattyc246@gmail.com',
  url = 'https://github.com/mattyc246/billplz-python',
  download_url='https://github.com/mattyc246/billplz-python/archive/1.0.2.tar.gz',
  keywords = ['billplz', 'payment', 'payment gateway'],
  include_package_data = False,
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
)
