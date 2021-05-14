import nbformat
import argparse


def nb2py(nbfile, pyfile):

    nb = nbformat.read(nbfile, as_version=4)

    with open(pyfile, mode='wt', encoding='utf-8') as pyf:
        for cell in nb.cells:
            type = cell.cell_type

            if type == 'code':
                pyf.write('#%%\n')
                pyf.write(cell.source)
                pyf.write('\n\n')

            elif type == 'markdown':
                pyf.write('#%%\n')
                pyf.write('"""\n')
                pyf.write(cell.source)
                pyf.write('\n"""\n\n')

def call():
    parser = argparse.ArgumentParser(
    description='Convert from Jupyter Notebook to python')
    parser.add_argument('notebook_file',
                        help='name of the jupyter notebook input file')
    parser.add_argument('python_file', nargs='?',
                        help='name of python output file')
    args = parser.parse_args()

    # ------------
    # File names
    # ------------

    nbfile = args.notebook_file
    pyfile = args.python_file
    if pyfile is None:
        pyfile = nbfile.replace('.ipynb', '.py')

    nb2py(nbfile, pyfile)

if __name__ == "__main__":
    call()