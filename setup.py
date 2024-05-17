from setuptools import setup, find_packages

setup(
    name='odin_api',
    version='0.0.1',
    description='Encapsulates the Odin API easing the use as well as additional features such as find alias',
    author='Jordan Prescott',
    author_email='jprescott23@gmail.com',
    url='https://github.com/Jordan-Prescott/odins_spear',
    packages=find_packages(),
    install_requires=[
        "certifi==2023.7.22",
        "charset-normalizer==3.2.0",
        "colorama==0.4.6",
        "idna==3.4",
        "requests==2.31.0",
        "tqdm==4.66.1",
        "urllib3==2.0.4"
    ]
)