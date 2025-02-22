from setuptools import setup, find_packages

setup(
    name="pygameshort",
    version="1.0.2",
    author="Neo Zetterberg",
    author_email="20091103neo@gmail.com",
    description="A UI extention onto pygame. Quite simple actually.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    include_package_data=True,  # Include all files inside the package folder
    install_requires=[
        "secure_network",
        "pygame",
        "pyperclip"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)