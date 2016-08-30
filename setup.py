#!/usr/bin/env python

import os
from setuptools import setup

PACKAGE_NAME = 'gcpmetrics'
DESCRIPTION = 'Google Cloud Platform Metrics'


def __find_package_data(folder):
    add_extensions = ['.schema', '.html', '.js', '.css', '.xml', '.jinja', '.bat', '.yaml',
                      '.json', '.png', '.jpg', '.po', '.txt', 'cert.pem', 'key.pem', '.zip']

    file_masks = []
    for subdir, dirs, files in os.walk(folder):
        for f in files:
            name = os.path.join(subdir, f)
            f = f.lower()
            if f.endswith(tuple(add_extensions)):
                path = name[len(folder) + 1:]
                file_mask = os.path.join(os.path.split(path)[0], '*' + os.path.splitext(path)[1])
                if file_mask not in file_masks:
                    file_masks.append(file_mask)

    return file_masks


def get_packages():
    bvt_dirs = ['gcpmetrics']
    return bvt_dirs


def get_package_data():
    data = {}
    found = __find_package_data('gcpmetrics')
    data['gcpmetrics'] = found
    return data


def get_install_requires():
    with open('requirements.txt') as f:
        return f.readlines()


def version():
    _path = os.path.split(os.path.abspath(__file__))[0]
    _file = os.path.join(_path, 'version.txt')
    f = open(_file, 'r')
    ver = f.read()
    f.close()
    return ver.strip()


setup(
    name=PACKAGE_NAME,
    version=version(),
    version_getter=version,
    author='Odin - Ingram Micro Company',
    author_email='aps@odin.com',
    description=DESCRIPTION,
    url='https://www.odin.com',
    license='BSD',
    packages=get_packages(),
    package_data=get_package_data(),
    install_requires=get_install_requires(),
    odintools=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['gcpmetrics = gcpmetrics.gcpmetrics:main']
    }
)
