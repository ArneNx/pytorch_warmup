import setuptools

with open("README.md", "r") as fh:
    long_description = ''
    for _ in range(3):
        long_description += fh.readline()

setuptools.setup(
    name="pytorch-warmup",
    version="0.0.3",
    author="Takenori Yamamoto",
    author_email="yamamoto.takenory@gmail.com",
    description="A PyTorch Extension for Learning Rate Warmup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tony-Y/pytorch_warmup",
    packages=['pytorch_warmup'],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    test_suite='test',
    install_requires=['torch>=1.1']
)