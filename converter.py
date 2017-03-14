import codecs
import pypandoc

long_desc = ''
with codecs.open('README.md', 'r', 'utf-8') as f:
    logn_desc_md = f.read()
    with codecs.open('README.rst', 'w', 'utf-8') as rf:
        rf.write(pypandoc.convert('README.md', 'rst'))
