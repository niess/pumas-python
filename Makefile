LIB= libpumas.abi3.so

PUMAS_C=   pumas/c
PUMAS_SRC= $(PUMAS_C)/src
PUMAS_H=   $(PUMAS_C)/include

SOURCES= $(PUMAS_SRC)/pumas.c \
         $(PUMAS_SRC)/pumas/extensions.c \
         $(PUMAS_SRC)/pumas/vectorization.c

INCLUDES= $(PUMAS_H)/pumas.h \
          $(PUMAS_H)/pumas/extensions.h \
          $(PUMAS_H)/pumas/vectorization.h


pumas/$(LIB): $(SOURCES) $(INCLUDES) pumas/pumas_build.py setup.py
	python3 setup.py build --build-lib .

.PHONY: clean
clean:
	rm -rf pumas/$(LIB) pumas/__pycache__

