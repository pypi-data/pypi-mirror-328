from setuptools import setup, find_packages

setup(
    name="fmp-stable-api",
    version="0.0.1",
    description="Python client library for the Financial Modeling Prep API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vimal Seshadri Raguraman",
    url="https://github.com/Vimal-Seshadri-Raguraman/FMP",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "ratelimit",
        "websockets",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial"
    ],
    extras_require={
        "dev": [
            "pytest",
            "twine"
        ]
    },
    python_requires='>=3.6',
    project_urls={
        "GitHub":"https://github.com/Vimal-Seshadri-Raguraman/FMP",
    }
)
