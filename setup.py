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
        "certifi==2023.7.22"
        "cffi==1.16.0"
        "charset-normalizer==3.2.0"
        "colorama==0.4.6"
        "cryptography==41.0.7"
        "graphviz==0.20.1"
        "idna==3.4"
        "loguru==0.7.2"
        "numpy==1.26.4"
        "pandas==2.2.2"
        "pycparser==2.21"
        "PyJWT==2.8.0"
        "python-dateutil==2.9.0.post0"
        "pytz==2024.1"
        "ratelimit==2.2.1"
        "requests==2.31.0"
        "six==1.16.0"
        "tqdm==4.66.1"
        "tzdata==2024.1"
        "urllib3==2.0.4"
        "win32-setctime==1.1.0"
    ]
)