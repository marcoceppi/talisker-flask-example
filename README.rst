talisker-flask-example
=======================

.. image:: https://travis-ci.org/canonical-ols/talisker-flask-example.svg?branch=master
    :target: https://travis-ci.org/canonical-ols/talisker-flask-example

.. image:: https://coveralls.io/repos/github/canonical-ols/talisker-flask-example/badge.svg?branch=master&cacheBuster=1
    :target: https://coveralls.io/github/canonical-ols/talisker-flask-example?branch=master

An example Flask app using Tallisker, deployable with Kubernetes.

Deployment
----------

Create the pods and health checks with ``kubectl create -f helloworld.k8s.yaml``

Monitor their status with ``watch 'kubectl get svc; kubectl get po'``
