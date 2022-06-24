from setuptools import setup

setup(
    name="VidUp",
    version="1.0",
    description="VidUp",
    author="Team Chat Team",
    install_requires=[
        "asyncio",
        "sanic",
        "sanic_cors",
        "motor",
    ],
)
