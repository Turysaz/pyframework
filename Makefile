
# source directories
SRC_DIR		= thirdparty
PYTHON_SRC_DIR	= $(SRC_DIR)/cpython
PYGAME_SRC_DIR	= $(SRC_DIR)/pygame

# target directories
PROJ_DIR		= xylophone
PYTHON_TRG_DIR	= $(PROJ_DIR)/python
PYGAME_TRG_DIR	= $(PROJ_DIR)/pygame

# 3rd party binaries
PYTHON_BIN	= python pybuilddir.txt libpython3.6m.a Modules Lib build
PYBIN_TRG	= $(PYTHON_BIN:%=$(PYTHON_TRG_DIR)/%)
PYBIN_SRC	= $(PYTHON_BIN:%=$(PYTHON_SRC_DIR)/%)

PYGAME_BIN	= a file
PGBIN_TRG	= $(PYGAME_BIN:%=$(PYTHON_TRG_DIR)/%)
PGBIN_SRC	= $(PYGAME_BIN:%=$(PYGAME_SRC_DIR)/%)


all: thirdparty
	# build xylophone

thirdparty: python-executable pygame-module

python-executable: $(PYTHON_TRG_DIR) $(PYBIN_TRG)

$(PYTHON_TRG_DIR):
	mkdir $(PYTHON_TRG_DIR)

$(PYTHON_TRG_DIR)/%: $(PYTHON_SRC_DIR)/%
	cp -r $< $@

$(PYBIN_SRC):
	cd $(PYTHON_SRC_DIR); bash configure --enable-optimization; make

pygame-module: $(PYGAME_TRG_DIR) #$(PGBIN_TRG)

$(PYGAME_TRG_DIR):
	mkdir $(PYGAME_TRG_DIR)

$(PYGAME_TRG_DIR)/%: $(PYGAME_SRC_DIR)/%
	cp -r $< $@

$(PGBIN_SRC):
	cd $(PYGAME_SRC_DIR)
	python setup.py build

test:
	python -m unittest -v

clean-pycache:
	find . | grep "__pycache__" | xargs rm -rfv
