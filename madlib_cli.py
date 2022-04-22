import re


def read_template(file):
    with open(file) as f:
        return f.read()


def parse_template(template):
    pattern = r"{(.*?)}"
    parts = tuple(re.findall(pattern, template))
    stripped = re.sub(pattern, "{}", template)
    return stripped, parts


def merge(expected_stripped, parts):
    return expected_stripped.format(*parts)
