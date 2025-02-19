from setuptools import setup, find_packages


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="docker-chatgpt-files-generator",
    version="0.0.2",
    author="tsyhanok-ivan",
    author_email="tsyhanok.ivan.dmytrovych@gmail.com",
    description="ChatGPT docker files generator.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Tsyhanok-Ivan",
    packages=find_packages(),
    install_requires=["requests==2.32.3", "openai==1.63.2"],
    classifiers=[
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
    ],
    keywords="docker chatgpt python generator",
    python_requires=">=3.0"
)
