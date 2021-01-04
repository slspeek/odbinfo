""" Writing out to jekyll site format """
import os
import contextlib
import dataclasses

import yaml
FRONT_MATTER_MARK = "---\n"


@contextlib.contextmanager
def chdir(dirname=None):
    """ Change directory and back """
    curdir = os.getcwd()
    try:
        if dirname is not None:
            os.chdir(dirname)
        yield
    finally:
        os.chdir(curdir)


def write_dict(adict, out):
    """ Writes `adict` to yaml and marks it as frontmatter """
    out.write(FRONT_MATTER_MARK)
    yaml.dump(adict, out)
    out.write(FRONT_MATTER_MARK)


def create_jekyll_site(output_dir, name):
    """ Sets up a empty jekyll site """
    workingdir = output_dir
    os.makedirs(workingdir, exist_ok=True)
    with chdir(workingdir):
        exitcode = os.system(f"jekyll new --blank {name}")
        if exitcode != 0:
            raise RuntimeError("jekyll unable to create blank site")
        exitcode = os.system(f"cp -rv ../data/jekyll-template/* {name}")
        if exitcode != 0:
            raise RuntimeError("unable to copy additional sources")
        os.system(f"rm {name}/index.md {name}/_layouts/default.html")
        sitedir = os.path.join(workingdir, name)
        os.chdir(name)
        exitcode = os.system("bundle install")
        if exitcode != 0:
            raise RuntimeError("bundle install failed")
    return sitedir


def _make_site(output_dir, name, tables):
    path = create_jekyll_site(output_dir, name)
    with chdir(path):
        os.mkdir("_tables")
        for tbl in tables:
            with open(f"_tables/{tbl.name}.md", "w") as out:
                write_dict(dataclasses.asdict(tbl), out)
        exitcode = os.system("jekyll build")
        if exitcode != 0:
            raise RuntimeError("unable to build jekyll site")
