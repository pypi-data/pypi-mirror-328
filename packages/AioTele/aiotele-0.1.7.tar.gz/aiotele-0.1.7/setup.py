from io import open
from setuptools import setup, find_packages

version = "0.1.7"

with open("./README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="AioTele",
    version=version,
    
    author="Bogdan Boris",
    author_email="gdrghdhgddy@gmail.com",
    
    description=(
        "AioTele is a Python module for building Telegram bots using asyncio. "
        "It offers an intuitive API for handling updates, commands, and messaging, "
        "supporting both long polling and webhooks for scalable, high-performance bots."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    url="https://github.com/Bogdan-godot/AioTele",
    download_url="https://github.com/Bogdan-godot/AioTele/archive/v{}.zip".format(version),
    
    license="Apache License, Version 2.0, see LICENSE file",
    
    packages=find_packages(),  # Автоматический поиск пакетов
    include_package_data=True,
    install_requires=[
        "aiohttp>=3.8.1",
        "certifi>=2025.1.31"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="telegram bot asyncio async telegram",
    python_requires=">=3.7",
)
