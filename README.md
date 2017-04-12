# Zendesk API bindings generator

This package provides `zdgen`, an API bindings generator for the Zendesk REST
API. The code currently generates the `zdesk_api.py` file for the `zdesk`
project, but there are more projects planned.

# Requirements

The API generator needs Python 3, `requests`, `BeautifulSoup4`, and
`inflection` installed. See the `requirements.txt` file. There also needs to be
a POSIX compliant `patch` executable in your path for applying the patches.
Linux and OSX have this, but on Windows it will need to be installed manually
with something like Cygwin.

# Contributing

Pull requests and patches to make `zdgen` compatible with Python 2 will not be
accepted. This is a Python 3 codebase. The _output_ of `zdgen` for Python,
however, is aimed to be Python 2 and Python 3 compliant, and patches to fix
Python 2 compatibility in the output are welcome.

# Setup and execution

```
# configure a virtualenv or conda env, etc

$ python setup.py install

or

$ python setup.py develop

$ cd somewhere/you/want/to/store/docs/and/output

$ zdgen
```

# Under the hood

When `zdgen` is executed for the first time, the following happens:

* `apidocs` dir is deleted if it is present
* `apidocs_orig` dir is made if it is not present
* The introduction pages for each API component is downloaded
* The intro pages are scraped for all other pages which are downloaded
* Pages are written into the `apidocs_orig` dir
* `apidocs_orig` is copied to apidocs
* `apidocs` pages are patched with the diffs in `patches` dir
* Patched `apidocs` pages are scraped for REST API info
* Duplicates, redundant, and ambiguous endpoints are resolved
* The actual `zdesk_api.py` code is generated
* The code is formatted into (appended) to the template
* `zdesk_api.py` is written to the current directory

On subsequent runs, the following happens:

* `apidocs` dir is deleted if it is present
* The introduction pages are located in the `apidocs_orig` dir
* The intro pages are scraped for all other pages
* The needed pages are located in the `apidocs_orig` dir
* `apidocs_orig` is copied to `apidocs` and the rest happens as before

# Developing patches to the documentation

If patches are needed, then to create them I do the following:

* Remove the patched `apidocs` dir
* Copy the `apidocs_orig` dir to `apidocs` dir
* If the file needing an edit has an already existing patch, apply the patch
  first:

```
$ cd apidocs_orig
$ patch -p1 < path/to/source/or/package/install/patches/core_stuff
```

* Edit the file as needed
* Generate a new patch, potentially replacing the old patch

```
$ cd ..
$ diff -r -u apidocs_orig apidocs > path/to/source/patches/core_stuff
```

NOTE: Work on patching only one file at a time. If another patch needs to be
made, then the `apidocs` directory needs to be removed again, then recopied
from the `apidocs_orig` directory. This ensures that the patches are for only
one file at a time.

# Documenting what has changed since the last generation

After generation I typically review the `zdesk_api.py` file to see what has
changed and to ensure that there are no new syntax problems and so forth. I
`diff` the old and new file, and also specifically look at the methods.

```
$ diff -u ../zdesk/zdesk_api.py zdesk_api.py

$ grep -E '^ *def' ../zdesk/zdesk_api.py > methods_old
$ grep -E '^ *def' zdesk_api.py > methods_new
$ diff -u methods_old methods_new
```

# Deploying to the zdesk project

Finally, once all is well and I am satisfied with the newly generated
`zdesk_api.py`:

```
cp zdesk_api.py path/to/zdesk/source/zdesk/zdesk_api.py
commit -a

# Document in the commit everything that has changed
```

Hopefully this will help if someone needs to take this over. It would be great
to get patch contributions and feedback on if the generated API needs to be
changed somehow to make it nicer.

