#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from collections import defaultdict
import codecs,string
from subprocess import check_output

punc = list(string.punctuation)
punc.append(u"।")
punc.append(u"።")
punc.append(u"‹")
punc.append(u"›")
punc.append(u"”")
punc.append(u"“")
punc.append(u"፡")
punc.append(u"፣")
punc.append(u"፤")
punc.append(u"«")
punc.append(u"،")
punc.append(u"»")
punc.append(u".")
punc.remove(u"@")
punc.remove(u"#")


translator = str.maketrans('', '', "".join(punc))

def ispuncnum(x):
    # TODO: this could be updated to include lists of punctuation...
    return x in punc or isnum(x)

def isnum(x):
    x = x.translate(translator)
    try:
        float(x)
        return True
    except:
        return False



def sortmap(m, k=20):
    """ Sort a dictionary by value, return the top k """
    return sorted(m.items(), key=lambda p: p[1], reverse=True)[:k]


def call_lm(ngramlist, port=8181, host="localhost"):
    """ This makes a call to an SRILM language model
    server. Equivalent to:
    $ ngram -use-server port@host -cache-served-ngrams -nbest ngramlist

    Start the server with:
    $ ngram -lm uglm.txt -server-port 8181
    
    ngramlist -- list of phrases, each having the same ngram length
    
    """

    FNULL = open(os.devnull, 'w')
    tmpname = "/tmp/tmp.txt"
    
    with codecs.open(tmpname, "w", "utf-8") as out:
        for ngl in enumerate(ngramlist):
            out.write("(1) " + ngl + "\n")
            
    result = check_output(["ngram", "-use-server", str(port) + "@" + host, "-cache-served-ngrams", "-nbest", tmpname], stderr=FNULL)
    return result

def getfnames(fof):
    """
    This takes a name which is either a file or a folder. If the name is
    a file, it returns a list containing only that file. If it is a folder,
    it returns a list containing the files in the folder.
    """
    if os.path.isdir(fof):
        fnames = list(map(lambda f: fof + "/" + f, os.listdir(fof)))
    else:
        fnames = [fof]
    return fnames
