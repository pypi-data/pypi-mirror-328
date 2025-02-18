import setuptools
from setuptools import find_packages


with open("requirements.txt") as f:
    requirements = [req for req in f.read().splitlines() if req]

setuptools.setup(
    name="eosapi-async",
    version="1.2.6",
    author="encoderlee",
    author_email="encoderlee@gmail.com",
    description="a simple, high-level and lightweight eosio sdk write by python with async support",
    long_description="""
        Introduced asynchronous versions of `abi_json_to_bin`, `make_transaction`, `get_info` and 
        `push_transaction` methods using aiohttp. This update enhances performance by allowing 
        non-blocking HTTP requests, especially useful for high-latency operations.
        
        Additional Asynchronous part developed by [alsekaram](https://github.com/alsekaram), you can find him on  
        GitHub or email [git@awl.su](mailto:git@awl.su).
        """,
    long_description_content_type="text/markdown",
    url="https://github.com/alsekaram/eosapi_async",
    packages=find_packages(),
    install_requires=requirements,
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
