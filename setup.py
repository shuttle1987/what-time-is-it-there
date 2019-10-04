from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='wtii',
    version='0.0.1',
    description="A utility to make it easy to find information about times where your friend/family/coworkers/etc are.",
    long_description=readme,
    author="Janis Lesinskis",
    author_email='janis@lesinskis.com',
    packages=[
        'wtii',
    ],
    package_dir={'wtii': 'wtii'},
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    keywords='timezones',
    entry_points = {
        'console_scripts': ['wtii=wtii.command_line:main'],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
