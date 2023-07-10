from setuptools import setup, find_packages

setup(
    name='streamlit-comments',
    version='0.0.5',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['streamlit'],
    url='https://github.com/pragmatic-streamlit/streamlit-phone-number',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved",
        "Topic :: Scientific/Engineering",
    ]
)