"""
fleval
------

Simple light-weight flask app for grading homeworks, scoring
applications, reviewing papers, etc. A web-server runs locally and
starts a browser to allow you to step through documents, showing you a
two-pane view with the document on the left and a comment+score box on
the right, with easy insertion of lines from comments in other
documents (useful for commenting on common mistakes when grading
homeworks).

* `Website <http://github.com/ayanc/fleval>`_

"""

import setuptools

setuptools.setup(
    name="fleval",
    version="0.1.1",
    author="Ayan Chakrabarti",
    author_email="ayan.chakrabarti@gmail.com",
    description="Flask app for grading or rating submissions, applications, etc.",
    long_description=__doc__,
    long_description_content_type="text/markdown",
    url="https://github.com/ayanc/fleval",
    license='MIT',
    packages= [],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0, <4',
    scripts = ['fleval','flerge'],
    install_requires = ['markdown','flask'],
)
