import argparse
import os
import re

import mindblow


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="name of the file being compiled, has to end with `.` followed by one or more `🤯`",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="the name of the output file, defaults to the name of the program with .o at the end",
        type=str,
    )
    args = parser.parse_args()
    out_file_path: str = args.output
    in_file_path: str = args.file
    if out_file_path is None:
        out_file_path = in_file_path + ".o"
    validate_input(in_file_path, out_file_path)

    with open(in_file_path, encoding="utf_8") as in_file_d:
        in_file_content = in_file_d.read()
    number_of_leading_zeros = in_file_path.rsplit(".", 1)[1].count("🤯") - 1
    output = mindblow.compile(in_file_content, number_of_leading_zeros)

    with open(out_file_path, "wb") as out_fd:
        out_fd.write(output)
    print("done")


def validate_input(in_file: str, out_file: str) -> None:
    assert isinstance(out_file, str), "there has to be an output path"
    assert isinstance(in_file, str), "there has to be an input path"
    assert re.match(
        r".*\.🤯+$", in_file
    ), "the input path has to and with one or more `🤯` after a `.`"
    assert os.path.isfile(in_file), f"the file {in_file} doesn't exist🤯🤯🤯🤯🤯🤯"


if __name__ == "__main__":
    main()
