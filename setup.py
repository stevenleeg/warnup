from distutils.core import setup

setup(
    name="Warnup",
    version="0.0.1",
    license="MIT License",
    description="An easy/simple way to push/diff production",
    install_requires=[
        "xtermcolor >= 1.2.1"
    ],
    scripts=["bin/warnup"]
)
