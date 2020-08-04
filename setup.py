import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='hivenpy',
    version='1.22',
    scripts=['hivenpy'] ,
    author="Julian Jones",
    author_email="julianjones663@gmail.com",
    description="An unofficial wrapper for hiven",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NexInfinite/hivenpy/",
    packages=["Hiven", "Hiven.Events", "Hiven.Methods", "Hiven.Objects", "Hiven.Websocket"],
    install_requires=[
        'websocket_client',
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )