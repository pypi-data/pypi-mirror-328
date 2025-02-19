from setuptools import setup, find_packages

setup(
    name='lial_sms',  # Replace with your package’s name
    version='1.0.0',
    packages=find_packages(include=['lial_sms']),
    install_requires=[
        'requests'
    ],
    author='SIGIER Luc',  
    author_email='l.sigier@lialrioz.fr',
    description=rf'Une librairie qui permet d\'intéragir avec le service de SMS de LIAL',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',

)