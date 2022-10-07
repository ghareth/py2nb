# py2nb – Conversion between jupyter notebooks and python scripts

This python package provides two modules:

* `py2nb` – Convert a python script to a jupyter notebook
* `nb2py` – Convert a jupyter notebook to a python script

To install this package type:
```
cd \path\to\py2nb\setup.py
pip install .
```

To convert a python script to a jupyter notebook
```
python -m py2nb python_script.py
python -m py2nb python_script.py python_script.ipynb
```

To convert a jupyter notebook to a python script 
```
python -m py2nb python_script.ipynb
python -m py2nb python_script.ipynb python_script.py
```

Note that the both command lines use the `py2nb` module


The script will determine the conversion from the extension of the first file.
If a second file is not provided, the script will determine the output file from first file.

### `py2nb`

Cells in the python script are separated by '#%%' as in the
jupyter extension for visual studio code. (Also spyder?)

Markdown cells are marked by following the separator with a triple quoted
string, starting and ending with `"""` (but not `'''`)  at the start of their lines. Any code in
the cell after the triple quoted string is ignored.

All other cells are converted to jupyter code cells.

### Other work

Conversion from notebook to python is part of the official `jupyter nbconvert` package.

Conversion from python to notebook is discussed at stackoverflow,
https://stackoverflow.com/questions/23292242.

This repo is a fork of 

There is also a github repository, https://github.com/sklam/py2nb, with the
same name. It is presently not maintained. A newer repository is
https://github.com/chicham/py2nb.

There is a vs code extension, Jupyter Notebook Converter, by Yigit Ozgumus.
This is supposed to do a py2nb-like conversion within the vs code editor.
Unfortunately, it is not working for me. Presently, the `py2nb` script does not
accept the Jupyter Notebook Converter markup format for the markdown info. This
may be implemented later.
