from setuptools import setup, find_packages

setup(
    name='Turtle_Glide',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'services': [
            'utils/js/*.js',
            'utils/css/*.css',
            'utils/views/*.html',
            'utils/views/layouts/*.html',
        ],
    },
    install_requires=[
        'Django>=3.2',
        'requests',
        'setuptools',
    ],
)
