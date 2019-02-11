import os

from setuptools import find_packages, setup

HERE = os.path.dirname(os.path.abspath(__file__))


def _get_version():
    """ Get version by parsing _version programmatically """
    version_ns = {}
    with open(os.path.join(HERE, "dash_google_charts", "_version.py")) as f:
        exec(f.read(), {}, version_ns)
    version = version_ns["__version__"]
    return version


def _get_long_description():
    with open(os.path.join(HERE, "README.md")) as f:
        return f.read()


setup(
    name="dash-google-charts",
    version=_get_version(),
    description="Google Charts for Plotly Dash",
    long_description=_get_long_description(),
    long_description_content_type="text/markdown",
    license="Apache Software License",
    author="Tom Begley",
    author_email="tomcbegley@gmail.com",
    url="https://github.com/tcbegley/dash-google-charts",
    packages=find_packages(),
    install_requires=["dash>=0.32.1", "dash-html-components"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    project_urls={
        "Bug Reports": "https://github.com/tcbegley/dash-google-charts/issues"
    },
)
