from setuptools import setup, find_packages

setup(
    name='proxy_api_package',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
    ],
    author='Antonio Ciorba',
    author_email='antoniociorba@outlook.com',
    description='A Python client for interacting with a REST API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/proxy_api_package',  # Replace with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
