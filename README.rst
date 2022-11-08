==================
docker0s manifests
==================

A collection of ready-to-use app manifests for `docker0s`_, with examples for how to
deploy them to your host.

.. _docker0s: https://github.com/radiac/docker0s

These are provided as is - you are responsible for what you deploy. Read through the
definitions to see if you are happy with them or want to customise them further.

Until docker0s supports base manifest hashes, for security purposes we recommend pinning
to a specific commit.

Contributions of improvements and generic definitions for popular services are welcome.


Available apps
==============

* Traefik - edge router for inbound traffic. We recommend this as part of every
  deployment.
