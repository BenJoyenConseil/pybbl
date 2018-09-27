<!-- $theme: default -->

	pip install pybbl

---
# packagin' who ?
		
## Packager c'est encapsuler du code avec

* une version qui correspond à un commit, une date
* le code qui exécuté ou importer par l'utilisateur
* avec des metadata pour le **package manager**
* le tout dans une archive : zip | tar.gz | bzip2

## [PyPA (2014)]() : 

**setuptools** c'est l'outil standard (remplace distutils, distutils2, easy_install, etc..)

---
# OK, let's do this

	touch setup.py
    echo "from setuptools import setup" > setup.py
    echo "setup()" >> setup.py
    python setup.py sdist

### 
	ll -R

---
# python setup.py sdist ?

Demande à python d'éxécuter la function `setup()` de setuptools pour construire un paquet de type **Source Distribution***
#
#
#
#
#
#
*source distribution : une archive du projet avec les *.py et l'arborescence des packages

---
```
pip install dist/UNKNOWN-0.0.0.tar.gz
ll lib/python3.6/site-packages/UNKNOWN-0.0.0-py3.6.egg
```

---
#	 vim setup.py
```
from setuptools import setup

setup(
    py_modules=['iamamodule']
)
```

---
distribution != package != module != extension
===

* **distribution** = une archive d'un projet qui sera accessible sur PyPI, compilé ou non
#
* **package** = un dossier qui possède du code et installé dans site-package/ qui possède un `__init__.py`
#
* **module** = un fichier.py auto-portant et installé à la racine de l'`env/lib/python/`
#
* **extension** = une librairie externe qui n'est pas du Python, à embarquer dans la distribution (lib C, C++)

---
# Using my sdist with pip

	pip install dist/UNKNOWN-0.0.0.tar.gz

---
When sdist? when Wheel ?
===

Packaging Gradient

# ![](https://packaging.python.org/_images/py_pkg_tools_and_libs.png)

---
Who for ? what for ?
===

* **Setuptools** (setup.py + setup.cfg + MANIFEST.in) : pour pip et [PYPI](https://pypi.org/)
#
* **Makefile** + **venv** : install global d'un env Python
#
* **Dockerfile** : isolation total

---
REFs

 * [Python Packaging User Guide¶](https://packaging.python.org/key_projects/#packaging)
 * [Less known packaging features and tricks](https://blog.ionelmc.ro/presentations/packaging/)
 * [Doc setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
 * [Packaging Gradient](https://www.youtube.com/watch?v=iLVNWfPWAC8)
 * [Zest releaser](https://zestreleaser.readthedocs.io/en/latest/index.html?highlight=changelog)
 * [PKG Resource : accessing files](https://setuptools.readthedocs.io/en/latest/pkg_resources.html#basic-resource-access)