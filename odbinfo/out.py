""" Writing out to jekyll site format """


import yaml
FRONT_MATTER_MARK = "---\n"


def write_dict(adict, out):
    """ Writes `adict` to yaml and marks it as frontmatter """
    out.write(FRONT_MATTER_MARK)
    yaml.dump(adict, out)
    out.write(FRONT_MATTER_MARK)
