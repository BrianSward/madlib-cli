import re

greeting = """
Hello there MadLib Enthusiast! At the prompts below enter words as instructed.
"""


def read_template(name):
    """
    this function takes in a template and reads it for us
    :param name: a_filename.txt
    :return: the contents of the file
    """
    try:
        with open(f"{name}", mode='r') as f:
            contents = f.read()
        return contents
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(name):
    """
    this takes in a string to be broken down into its word types and remaining text
    :param name: "a string so sweet"
    :return: a tuple with info seperated per regex term
    """
    put_here = []
    new_string = ""
    contents = name
    term = r"\{(.*?)\}"
    new_string = re.sub(term, "{}", contents)
    extracted = re.finditer(term, contents)
    for i, b in enumerate(extracted):
        put_here.append(b.group(1))
    chunk = (new_string, tuple(put_here))
    return chunk


def merge(a, b):
    """
    merges a string and a tuple back into a madlib
    :param a: string to be joined
    :param b: list to be joined
    :return: string {list_items} inserted into brackets
    """
    return a.format(*b)


if __name__ == "__main__":
    print(greeting)
    solutions = []
    for item in parse_template(read_template("assets/dark_and_stormy_night_template.txt"))[1]:
        solutions.append(input(f"Give me an {item}: "))
    final = merge(parse_template(read_template("assets/dark_and_stormy_night_template.txt"))[0], solutions)
    with open("assets/madlib.txt", mode='w') as f:
        f.write(final)
