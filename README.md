<!-- $theme: default -->

	pip install pybbl


[@Github du BBL](https://github.com/BenJoyenConseil/pybbl.git)

---
# packagin' who ?
		
## Packager c'est encapsuler du code avec

* une version qui correspond à un commit, une date
* le code qui exécuté ou importer par l'utilisateur
* avec des metadata pour le package manager (ex: pip, apt, yum)
* le tout dans une archive : zip | tar.gz | bzip2

On appelle ça communément un artéfact, un paquet, sauf en python où c'est une **distribution**

---
# [PyPA (2014)]() 
#

* **setuptools** c'est l'outil standard, qui remplace distutils, distutils2, easy_install, etc..
* **pip** c'est le package manager principal
* **pypi.org** c'est le repo central
#
#
#
#
*PyPA : Python Packaging Authority

---
# OK, let's do this

	touch setup.py
    echo "from setuptools import setup" > setup.py
    echo "setup()" >> setup.py
    python setup.py sdist

#
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

# and check the result
ll lib/python3.6/site-packages/UNKNOWN-0.0.0-py3.6.egg
```



---
# vim setup.py

```
from setuptools import setup

setup(
	...
)
```

[bbl repo interactif : https://github.com/BenJoyenConseil/pybbl](https://github.com/BenJoyenConseil/pybbl)




---
# distribution != package != module != extension

* **distribution** = une archive d'un projet qui sera accessible sur PyPI, compilé ou non
#
* **package** = un dossier qui possède du code et installé dans site-package/ qui possède un `__init__.py`
#
* **module** = un fichier.py auto-portant et installé à la racine de l'`env/lib/python/`
#
* **extension** = une librairie externe qui n'est pas du Python, à embarquer dans la distribution (lib C, C++)




---
# When sdist? when Wheel ?

Packaging Gradient

# ![](https://packaging.python.org/_images/py_pkg_tools_and_libs.png)




---
# PyPi.org

* Upload avec twine
* De préférence les deux types de distribution : wheel et source
* Le nom de la distribution (dans setup.py) = `pip install nom_distribution`
* Le nom du package = lib/python/site-package/nom_package
* Une distribution peut donc contenir plusieurs packages




---
# No more sys.append

```md
pip install -e .

# équivalent de 
python setup.py develop

```
#
Pour accéder à votre package en cours de développement depuis un autre projet




---
# Who for ? what for ?

* **Setuptools** (setup.py + setup.cfg + MANIFEST.in) : pour pip et [PyPI](https://pypi.org/) (si d'autres personnes veulent utiliser votre package, c'est le mieux)
#
* **conda** (env.yaml) ou **venv** (requirements.txt) : installation global d'un env Python (cool pour le dev)
#
* **Makefile** : point d'entrée pour installer, tester, packager, distribuer (le pont entre le process d'install sur la prod et sur la dev)
#
* **Dockerfile** : isolation totale avec les libs du système




---
# Des dépendances à différents endroits

		Dev / Build dist / Test / Deploy / Run


---
REFs

 * [Python Packaging User Guide](https://packaging.python.org/key_projects/#packaging)
 * [Less known packaging features and tricks](https://blog.ionelmc.ro/presentations/packaging/)
 * [Doc setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
 * [Packaging Gradient](https://www.youtube.com/watch?v=iLVNWfPWAC8)
 * [Zest releaser](https://zestreleaser.readthedocs.io/en/latest/index.html?highlight=changelog)
 * [PKG Resource : accessing files](https://setuptools.readthedocs.io/en/latest/pkg_resources.html#basic-resource-access)
 * [pip install via Github](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support)