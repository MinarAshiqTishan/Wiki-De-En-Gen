from setuptools import setup, find_packages

setup(
      name="Wiki-De-En-Gen",
      description="Generate German word list from Wiki with meaning as a CSV",
      version="1.0.0",
      url="https://github.com/MinarAshiqTishan/Wiki-De-En-Gen",
      install_requires=["dictcc", "pandas", "wikipedia-api"],
      author='Minar Ashiq Tishan',
      packages=find_packages(),
     )