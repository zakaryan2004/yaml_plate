#  MIT License
#
#  Copyright (c) 2020 Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="YAML_Plate",
    version="1.0.3",
    description="A fork of Plate (Internationalization library for Python), for YAML",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/zakaryan2004/yaml_plate",
    author="zakaryan2004",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
    ],
    keywords="i18n internationalization l10n localization library python yaml interpolation pluralization emoji",
    project_urls={
        "Tracker": "https://github.com/zakaryan2004/yaml_plate/issues",
        "Source": "https://github.com/zakaryan2004/yaml_plate",
    },
    python_requires="~=3.5",
    packages=["yaml_plate"],
    install_requires=["PyYAML"],
    zip_safe=False,
)
