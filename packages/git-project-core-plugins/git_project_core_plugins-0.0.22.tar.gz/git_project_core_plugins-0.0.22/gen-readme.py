#!/usr/bin/env python3

import ast
import fnmatch
import os
from pathlib import Path
import re
import shutil

class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self._docs = dict()

    def visit_ClassDef(self, node):
        match = re.match(r'^(\w+)Plugin$', node.name)
        if match:
            command = match.group(1).lower()
            self._docs[command] = ast.get_docstring(node)
            self.generic_visit(node)

    @property
    def docs(self):
        return self._docs

def main():
    docs = dict()
    for dirpath, dirnames, filenames in os.walk(Path(__file__).parent):
        pyfilenames = fnmatch.filter(filenames, '*.py')
        for py in pyfilenames:
            with open(Path(dirpath) / py, "r") as source:
                tree = ast.parse(source.read())
            visitor = Analyzer()
            visitor.visit(tree)
            docs.update(visitor.docs)

    template_path = Path(__file__).parent / 'docs' / 'README-template.rst'
    readme_path   = Path(__file__).parent / 'README.rst'

    shutil.copy2(template_path, readme_path)

    with open(readme_path, 'a') as readme:
        readme.write('\nCommand Reference\n')
        readme.write('=================\n')

        for name in sorted(docs):
            doc = docs.get(name, None)
            if doc:
                readme.write(f'\n{name}\n')
                readme.write('-' * len(name))
                readme.write('\n')
                readme.write(doc)
                readme.write('\n')

if __name__ == "__main__":
    main()
