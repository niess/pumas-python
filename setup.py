from setuptools import setup

setup(name='pumas',
      version='0.1',
      description='Python wrapper for PUMAS',
      author='Valentin Niess',
      packages=['pumas'],
      setup_requires=['cffi>=1.0.0'],
      cffi_modules=['pumas/pumas_build.py:ffi'],
      install_requires=['cffi>=1.0.0']
)
