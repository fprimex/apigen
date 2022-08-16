# API bindings generator

This package provides `apigen`, an API bindings generator for REST
API services. The code currently generates

* The `zdesk_api.py` file for the `zdesk` project
* The `doc` directory used by the `zdesk-cli` project
* Most of the `doc` files used by the `tfh` project

# Requirements

The API generator needs Python 3, `requests`, `BeautifulSoup4`, and
`inflection` installed. See the `requirements.txt` file. There also needs to be
a POSIX compliant `patch` executable in your path for applying the patches.
Linux and OSX have this. On Windows the WSL is strongly recommended.

# Setup and execution

```
# configure a virtualenv or conda env, etc

$ python setup.py install

or

$ python setup.py develop

$ cd somewhere/you/want/to/store/docs/and/output

$ apigen [options] FRONTEND BACKEND
```

# Usage

Full options to `zdgen` are shown below in the help output:

```
usage: apigen [-h] [-out OUTFILE] [-docs DOCDIR] FRONTEND BACKEND

description:
  Generate an API language binding directly from the API's documentation

  Available frontend APIs are:
  zendesk - The Zendesk helpdesk REST API
  tfc     - The Terraform Cloud and Enterprise REST API

  Zendesk available Backends are:
  zdesk   - Python for use with zdesk. File: zdesk_api.py
  zdesk.sh- Bourne shell for use with junonia. Output: junonia filetree
  go      - Golang for use with zdesk-go. File: zdesk_api.go

  TFC available Backends are:
  tfc     - Python for use with tfc. File: tfc_api.py
  tfc.sh  - Bourne shell for use with junonia. Output: junonia filetree

  Other backends:
  listing - Text file listing of all endpoints. File: listing.txt

positional arguments:
  FRONTEND      API to implement
  BACKEND       Programming language to generate binding for

optional arguments:
  -h, --help    show this help message and exit
  -out OUTFILE  Output file for the binding (default: from backend)
  -docs DOCDIR  Directory Zendesk docs will be stored in (default: apidocs)
```

# Under the hood

When `apigen` is executed for the first time, the following happens:

All:
* `apidocs` dir is deleted if it is present
* `apidocs_orig` dir is made if it is not present

For Zendesk:
* The introduction pages for each API component is downloaded
* The intro pages are scraped for all other pages which are downloaded

TFC:
* TODO: document when stabilized

All:
* Pages are written into the `apidocs_orig` dir
* `apidocs_orig` is copied to apidocs
* `apidocs` pages are patched with the diffs in `patches` dir
* Patched `apidocs` pages are scraped for REST API info
* Duplicates, redundant, and ambiguous endpoints are resolved
* The code is formatted into to the template(s)
* The backend file or directory is written to the current directory or given path

On subsequent runs, the following happens:

* `apidocs` dir is deleted if present
* The generation target (file or directory) is deleted if present
* `apidocs_orig` is copied to `apidocs` and the rest happens as before

# Developing patches to the documentation

If patches are needed, then to create them I do the following:

* Remove the patched `apidocs` dir
* Copy the `apidocs_orig` dir to `apidocs` dir
* If the file needing an edit has an already existing patch, apply the patch
  first:

```
$ cd apidocs
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

