from setuptools import setup, find_packages


setup(
    name="CPLS",
    version="0.0.1",
    author="Максуров Денис",
    author_email="denismaksyrov@bk.ru",
    description="Centralized Project Launch System",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Manul147/General-Arcgitecture",
    packages=find_packages(),  # Автоматический поиск пакетов
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[
        "annotated-types==0.7.0",
        "fix-busted-json==0.0.18",
        "pydantic==2.10.3",
        "pydantic_core==2.27.1",
        "typing_extensions==4.12.2",
        "watchdog==6.0.0",
    ],
    include_package_data=True,
    package_data={
        "CPLS": ["base_configs/*.json"],
    },
)