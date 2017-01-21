import os

import pypandoc

for filename in os.listdir('./docs/pre/'):
    if filename.endswith(".md"):
        output = pypandoc.convert('somefile.md', to='rst', format='markdown' outputfile="./docs/source/" + (os.path.splitext(filename)[0]) + ".rst")
