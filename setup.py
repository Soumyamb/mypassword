from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
	long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['random']

# some more details
CLASSIFIERS = [
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'Topic :: Internet',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python',
	'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 2.6',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	]

# calling the setup function
setup(name='mypassword',
	version='1.0.0',
	description='A simple password generator',
	long_description=long_description,
	url='https://github.com/Soumyamb/mypassword',
	author='Soumyamb',
	author_email='soumyamb123@gmail.com',
	license='MIT',
	packages=['password1122'],
	classifiers=CLASSIFIERS,
	install_requires=REQUIREMENTS,
	keywords='{password generator}'
	)
