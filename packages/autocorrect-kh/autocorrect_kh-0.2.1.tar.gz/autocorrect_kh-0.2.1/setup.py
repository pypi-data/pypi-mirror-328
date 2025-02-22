from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="autocorrect_kh",
    version="0.2.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'autocorrect_kh': [
            'data/phum/*.txt',
            'data/khum/*.txt',
            'data/*.txt'
        ],
    },
    install_requires=[
        "jellyfish",
        "regex",
    ],
    author="Kim Ouddommony",
    author_email="kimmony039@gmail.com",
    description="An autocorrect address library specifically for Khmer National ID Card",
    url="https://github.com/monykappa/autocorrect-kh.git",
)
