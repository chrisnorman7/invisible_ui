from setuptools import setup
import os

n = "invisible_ui"
p = [n]

for f in os.listdir(n):
    if os.path.isdir(os.path.join(n, f)):
        p.append(n + "." + f)
        print("Adding %s to packages." % os.path.join(n, f))

setup(
    name=n,
    version="1.6",
    description="Accessible UI elements for pygame.",
    url="http://github.com/tbreitenfeldt/invisible_ui.git",
    author="TJ Breitenfeldt and Chris Norman",
    author_email="timothyjb310@gmail.com",
    license="GPL",
    packages=p,
    zip_safe=True,
    keywords=[
        "ui",
        "user interface",
        "pygame",
        "accessible",
        "a11y",
        "accessible_output",
        "spoken",
        "menu",
        "element"],
    install_requires=[
        "pygame"
    ],
    dependency_links=[
        "hg+http://hg.q-continuum.net/accessible_output2#egg=accessible_output2"
    ]
)
