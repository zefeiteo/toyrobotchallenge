from setuptools import find_packages, setup

requirements = [
    "setuptools",
    "argparse",
]

setup(
    author="Ze Fei Teo",
    author_email="zefeiteo@gmail.com",
    python_requires=">=3.8.10",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
    description="Toy robot that traverses on a finite surface",
    entry_points={"console_scripts": ["toy_robot=prog:main"]},
    install_requires=requirements,
    license="MIT license",
    keywords="toyrobot",
    name="toyrobot",
    packages=find_packages(include=["toyrobot"]),
    test_suite="tests",
    url="https://github.com/zefeiteo/toyrobotchallenge",
    version="0.1.1",
    zip_safe=False,
)