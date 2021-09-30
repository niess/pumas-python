# Python bindings for the [PUMAS library](https://niess.github.io/pumas-pages/)

__Warning__: _This is an experimental project. It is work in progress._

# Building

From source, on Linux:

1. Clone this project
   ```
   git clone https://github.com/niess/pumas-python
   ```

2. Copy, or link, the _pumas.c_ and _pumas.h_ source files.
   ```
   ln -s $PUMAS_DIR/src/pumas.c pumas/c/src
   ln -s $PUMAS_DIR/include/pumas.h pumas/c/include
   ```
   where `PUMAS_DIR` is the location of the PUMAS source.

3. Run the [Makefile](Makefile)
   ```
   cd pumas-python
   make
   ```
   This generates _in-source_ bindings under the [pumas/](pumas) folder.

4. (Optionnaly) export the [pumas/](pumas) folder to PYTHONPATH
   ```
   export PYTHONPATH=$(pwd):$PYTHONPATH
   ```

# Usage

A few examples of usage are located under the [examples/](examples) folder. The
Python API is similar to the C one, with some _quality of life_ tweaks.
