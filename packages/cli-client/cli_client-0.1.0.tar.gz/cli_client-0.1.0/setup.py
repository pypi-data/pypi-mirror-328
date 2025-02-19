# setup.py

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name="sensory-llm-cli",        # При установке через pip библиотеку можно называть, например, cli-client
  version="0.1.0",
  author="SensoryLAB",
  author_email="fox@sensorylab.com",
  description="CLI клиент для взаимодействия с Model Provider API",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/your_username/cli-client",
  packages=setuptools.find_packages(exclude=["tests*"]),
  install_requires=[
    "aiohttp>=3.8.1",
    "pytest>=6.0.0"
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  entry_points={
    "console_scripts": [
      "cli-client=cli_client.__main__:main"
    ]
  },
  python_requires=">=3.8",
)