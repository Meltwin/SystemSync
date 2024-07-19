from setuptools import setup

setup(
    name='systemsync',
    version='0.0.1',
    author="Meltwin",
    author_email="meltwin158@gmail.com",
    url="https://github.io/Meltwin/SystemSync",
    license="MIT",
    description="SystemSync let you keep several installations synced together through a single distant manifest file.",
    long_description=open("README.md").read(),
    install_requires=[
        "PyYaml"
    ],
    entry_points={
        'console_scripts': [
            'sysync = systemsync.cli:main'
        ]
    },
)
