from setuptools import setup

setup(name="pin-tag",
      version="0.1",
      description="pinboard tag cleanup",
      url="",
      author="Smell Gibbons",
      license="MIT",
      packages=["pin-tag"],
      install_requires=["pinboard", "ruamel.yaml"]
      zip_safe=False
      )
