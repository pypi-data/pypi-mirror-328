from setuptools import setup

with open("requirements.txt") as f:
    req = f.read().splitlines()

with open("README.md") as f:
    long_desc = f.read()

setup(
    name="transactional_remove",
    version="1.0.5",
    packages=["trm"],
    install_requires=req,
    entry_points={
        "console_scripts": [
            "trm=trm:main",
        ],
    },
    long_description=long_desc,
    long_description_content_type="text/markdown"
)