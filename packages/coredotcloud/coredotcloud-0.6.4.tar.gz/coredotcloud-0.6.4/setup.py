from setuptools import setup, find_packages

setup(
    name="coredotcloud",
    version="0.6.4",
    packages=find_packages(),
    install_requires=["psutil", "requests", "gputil"],
    entry_points={
        "console_scripts": [
            "coredotcloud=coredotcloud.main:main"
        ]
    },
    author="CoreDotToday",
    author_email="dev@core.today",
    description="A simple system monitoring tool for CoreDotCloud",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/coredottoday/coredotcloud",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
