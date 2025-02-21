from setuptools import setup, find_packages

setup(
    name="time-travel-debugger",
    version="0.1.1",
    author="Siddhant Jaiswal",
    author_email="sddhantjaiii@gmail.com",
    description="A time-travel debugger for Python with step-backward execution.",
    long_description=open("README.md", encoding="utf-8").read(),

    long_description_content_type="text/markdown",
    url="https://github.com/sddhantjaiii/Time-Travel-debugger",
    packages=find_packages(),
    install_requires=["rich"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
