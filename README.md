Flask Application Demo
=======================

Shows a demo application and api example


Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the main branch. ::

    # clone the repository
    $ git clone https://github.com/pallets/flask
    $ cd flask
    # checkout the correct version
    $ git tag  # shows the tagged versions
    $ git checkout latest-tag-found-above
    $ cd examples/tutorial

Create a virtualenv and activate it::

    $ python3 -m venv .venv
    $ . .venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv .venv
    $ .venv\Scripts\activate.bat

Install Flaskr::

    $ pip install -e .

Or if you are using the main branch, install Flask from source before
installing Flaskr::

    $ pip install -e ../..
    $ pip install -e .


Run
---

.. code-block:: text

    $ flask --app flaskapp init-db
    $ flask --app flaskapp run --debug

Open http://127.0.0.1:5000 in a browser.

Bu uygulama app factory ile olsuturuldugu icin gunicorn ile calistririrken asagidaki gibi calistirilir
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser



Code Scan
---------
This project github actions connected to sonarcloud. Sonarcloud is a code scan tool. 
It scans the code and gives a report about the code quality.
Users of an organization needs to subscribe to notifications 
of an project that is attaced to sonarcloud.



Helm
------
This application is deployed to kubernetes cluster with helm. The helm package creation
 is done with github actions. The helm package is stored in github repo and served with github pages.
 This also includes an index.yaml file. This file is for human readable helm repo index.
 Helm package can also be created manually. 
 To create a helm package manually, run the following command in the root directory of the project.
```
helm package helm/flaskapp
````

This will create a package named `flaskapp-0.1.0.tgz` in the root directory of the project.

To create a helm repo index file, run the following command in the root directory of the project.
```
helm repo index --url https://ozgurkara.github.io/flaskapp/ .
````

This will create an `index.yaml` file in the root directory of the project.

To serve the helm repo, run the following command in the root directory of the project.
```
helm serve --repo-path .
```
This will serve the helm repo on http://localhost:8879.

To add the helm repo to helm, run the following command.
```
helm repo add flaskapp http://localhost:8879
```
To install the helm package, run the following command.
```
helm install flaskapp flaskapp/flaskapp
```

To upgrade the helm package, run the following command.
```
helm upgrade flaskapp flaskapp/flaskapp
```
To uninstall the helm package, run the following command.
```
helm uninstall flaskapp
```
To delete the helm repo, run the following command.
```
helm repo remove flaskapp
```
To delete the helm package, run the following command.
```
helm delete flaskapp
```
To delete the helm package and the helm repo, run the following command.
```
helm delete flaskapp --purge
```

    
    