from setuptools import setup
from setuptools.command.install import install


class PostInstallCommand(install):
    def run(self):
        import os
        os.system("echo 'Just a demo POC for the Seasides 2025 SAST SCA Village.' > /tmp/seasides2025_pypi_poc.txt")
        install.run(self)


setup(
    cmdclass={
        "install": PostInstallCommand,
    },
    name="package-name-here",
    version="0.0.1",
    author="",
    author_email="",
    description="A demo POC for the Seasides 2025 SAST SCA Village.",
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ]
)

