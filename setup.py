from setuptools import setup

setup(name='conll',
      version='0.1',
      description='A collection of scripts for working with conll format files.',
      url='http://github.com/mayhewsw/python-conll',
      author='Stephen Mayhew',
      author_email='swm.mayhew@gmail.com',
      license='MIT',
      packages=['conll'],
      scripts=['bin/applyrules.py',
               'bin/combination.py',
               'bin/compare.py',
               'bin/conll2submission.py',
               'bin/count.py',
               'bin/densify.py',
               'bin/dense2.py',
               'bin/encodestems.py',
               'bin/balance.py',
               'bin/gazmatch.py',
               'bin/getnames.py',
               'bin/getstats.py',
               'bin/perturb.py',
               'bin/iaa.py',
               'bin/datastats.py',
               'bin/mergelabels.py',
               'bin/addweights.py',
               'bin/score.py',
               'bin/sample.py',
               'bin/stemfile.py',
               'bin/stem.py',
               'bin/toconll.py',
               'bin/tolines.py',
               'bin/translate.py',
               'bin/modifylabels.py',
               'bin/twitterner.py'],
      zip_safe=False)
