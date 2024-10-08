from setuptools import setup, find_packages

with open('README.md', 'r', encoding="utf-8") as file:
    long_description = file.read()

setup(
    name='odins_spear',
    version='1.2.3',
    url='https://github.com/Jordan-Prescott/odins_spear',
    author='Jordan Prescott',
    author_email='jprescott23@gmail.com',
    description='Python library for Odin API to build and manage Broadworks installations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
     classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'certifi==2023.7.22',
        'cffi==1.16.0',
        'charset-normalizer==3.2.0',
        'colorama==0.4.6',
        'cryptography==41.0.7',
        'graphviz==0.20.1',
        'idna==3.4',
        'pycparser==2.21',
        'PyJWT==2.8.0',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.1',
        'ratelimit==2.2.1',
        'requests==2.31.0',
        'six==1.16.0',
        'tqdm==4.66.1',
        'tzdata==2024.1',
        'urllib3==2.0.4',
        'win32-setctime==1.1.0'
    ]
)