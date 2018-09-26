import setuptools

setuptools.setup(
    name="pylint-aiida",
    license="MIT",
    version="0.1.0",
    description="Linter to flag issues in AiiDA plugins",
    author="The AiiDA team",
    author_email="leopold.talirz@gmail.com",
    url="https://github.com/aiidateam/pylint-aiida",
    packages=[
        "pylint_aiida",
    ],
    install_requires= [
        'pylint',
        'aiida-core',
    ],
    classifiers=[
        "Framework :: Pylint",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
