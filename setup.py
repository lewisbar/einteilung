import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="einteilung",
    version="0.0.1",
    author="Lennart Wisbar",
    author_email="lewisbar.git@gmail.com",
    description="Makes a plan which volunteer musicians/sound guys are in charge at which date in our church service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lewisbar/einteilung",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'attrs==19.3.0',
        'cachetools==3.1.1',
        'certifi==2019.9.11',
        'chardet==3.0.4',
        'google-api-python-client==1.7.11',
        'google-auth==1.6.3',
        'google-auth-httplib2==0.0.3',
        'gspread==3.1.0',
        'httplib2>=0.18.0',
        'idna==2.8',
        'importlib-metadata==1.3.0',
        'more-itertools==8.0.2',
        'oauth2client==4.1.3',
        'packaging==19.2',
        'pluggy==0.13.1',
        'py==1.8.0',
        'pyasn1==0.4.7',
        'pyasn1-modules==0.2.7',
        'pyparsing==2.4.5',
        'pyperclip==1.7.0',
        'pytest==5.3.1',
        'requests==2.22.0',
        'rsa==4.0',
        'six==1.12.0',
        'tqdm==4.36.1',
        'uritemplate==3.0.0',
        'urllib3==1.25.6',
        'wcwidth==0.1.7',
        'zipp==0.6.0',
    ]
)
