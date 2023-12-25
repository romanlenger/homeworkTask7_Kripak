from setuptools import setup, find_packages

setup(
    name='Clean folder script by Roman Kripak',
    version='0.0.1',
    url='https://github.com/romanlenger/homeworkTask7_Kripak',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean_folder.clean:main',
        ]
    }
)