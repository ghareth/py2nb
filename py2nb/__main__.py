from py2nb.py2nb import py2nb
from py2nb.nb2py import nb2py

from  pathlib import Path
import argparse

def determine_out_file(in_file, suffix, args):
    if args.output_file is None:
        out_file = in_file.with_suffix(suffix)
        if out_file.exists():
            max_number = 0
            for each_file in in_file.parent.iterdir():
                if out_file.stem != each_file.stem and (out_file.stem+"_") in each_file.stem:

                    number_str = each_file.stem.rsplit("_", 1)[1]
                    print(number_str)
                    try:
                        number = int(number_str)
                    except ValueError:
                        continue
                    print(max_number, number)
                    if max_number <= number:
                        max_number = number
                    print(max_number, number)
            out_file = in_file.parent / (in_file.stem + "_" + str(max_number + 1) + suffix)
    else:
        out_file = Path(args.output_file).resolve()

    return out_file

def call():
    parser = argparse.ArgumentParser(
        description='python to Jupyter Notebook converter')
    parser.add_argument('input_file',
                        help='name of the input file, either py or ipynb')
    parser.add_argument('output_file', nargs='?',
                        help='name of output file, without suffix, (optional)')
    args = parser.parse_args()

    # ------------
    # File names
    # ------------

    in_file = Path(args.input_file).resolve()

    if in_file.suffix == ".py":
        out_file = determine_out_file(in_file, ".ipynb", args)
        func = py2nb
    elif in_file.suffix == ".ipynb":
        out_file = determine_out_file(in_file, ".py", args)
        func = nb2py
    else:
        print("Unexpected file extension")
        return None

    print(str(in_file))
    print(str(out_file))

    func(str(in_file), str(out_file))

if __name__ == "__main__":
    call()