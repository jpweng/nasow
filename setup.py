from setuptools import setup


setup(
    name="nasow",
    version="1.0.0",
    packages=[
      "nasow"
    ],
    include_package_data=True,
    description="Nasow is a simple small python script which synchronizes DNS servers for WSL from Windows.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jean-Paul Wenger",
    author_email="jpaul.wenger@gmail.com",
    url="https://github.com/jpweng/nasow",
    install_requires=[
        "pathlib2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ]
)
