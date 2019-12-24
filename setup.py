"""Example Python application, using the paved path."""

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
try:  # for pip >= 10
    from pip._internal.download import PipSession
except ImportError:  # for pip <= 9.0.3
    from pip.download import PipSession

from setuptools import setup


# Gather install requirements from requirements.txt
install_reqs = parse_requirements('requirements.txt', session=PipSession())
install_requires = [str(ir.req) for ir in install_reqs]


setup(
    name='learn_aws_services',
    versioning='build-id',
    author='Om Narayann',
    keywords='aws-sevices',
    url='https://github.com/OMNARAYANYU/Learn-AWS-Services.git',
    setup_requires=['setupmeta'],
    python_requires='>=3.6',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'access_imp_services = aws.cli:cli'
        ]
    }
)
