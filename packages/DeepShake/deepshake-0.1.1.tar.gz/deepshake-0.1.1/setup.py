from setuptools import setup

setup(
    name="DeepShake",
    version="0.1.1",
    long_description="DeepShake",
    long_description_content_type="text/markdown",
    packages=["deepshake"],
    install_requires=["numpy",  "h5py", "matplotlib", "pandas"],
)
