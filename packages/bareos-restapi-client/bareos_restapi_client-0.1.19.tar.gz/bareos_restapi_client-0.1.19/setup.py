from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bareos-restapi-client",
    version="0.1.19",
    author="Your Name",
    author_email="your.email@example.com",
    description="A client for Bareos REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-repo",
    packages=['bareos_restapi_client'],  # 패키지 이름을 명시적으로 설정합니다.
    package_dir={'bareos_restapi_client': '.'},  # 현재 디렉토리를 패키지의 루트로 설정합니다.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "pydantic",
        "fastapi",
    ],
)