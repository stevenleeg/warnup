from distutils.core import setup

setup(
    name="warnup",
    version="1.0",
    url="http://github.com/stevenleeg/warnup",
    license="MIT",
    author="Steve Gattuso",
    author_email="steve@stevegattuso.me",
    description="An easier way to deploy code when you can't do it the easy way.",
    install_requires=[
        "xtermcolor >= 1.2.1"
    ],
    packages=["warnup"],
    scripts=["bin/warnup"]
)
