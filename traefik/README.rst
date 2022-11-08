==========================
docker0s manifest: traefik
==========================

Traefik is an edge router - it routes inbound traffic to the correct container.

Most official docker0s app manifests expect this to be part of your host manifest, and
will register themselves with Traefik using Docker labels.


This manifest:

* listens on ports 80 and 443
* detects other apps you use
* redirects HTTP to HTTPS and sorts out certificates automatically
* adds a dashboard for you to see what's going on
* creates an internal ``traefik`` network for your other apps to join their public
  services to


Current known limitations:

* no support for ports other than 80 and 443
* no support for SSO


Environment variables
=====================

``DASHBOARD_URL``:
  The URL to serve the dashboard on

  Default: ``traefik.example.com``

``DASHBOARD_USER``:
  The username for HTTP authentication to access the dashboard

  Default: ``admin``

``DASHBOARD_PASSWORD``:
  Password. Must be encrypted - use the ``mkpass`` command to generate the string::

      docker0s cmd traefik mkpass

  Default: ``password`` (encrypted using ``mkpass``)

``LETSENCRYPT_EMAIL``:
  The email address to use when registering HTTPS certificates

  Default: ``user@example.com``


Example usage
=============

Prepare a host ready to serve apps over HTTPSs::

    host:
      name: myserver.example.com
      user: myuser

    apps:
      traefik:
        path: git+https://github.com/radiac/docker0s-manifests#traefik
        env:
          DASHBOARD_URL: "traefik.myserver.example.com"
          DASHBOARD_USER: "myuser"
          DASHBOARD_PASSWORD: "$1$zMqRlaFZ$gfG1yqfaZnmHtVsPCgQl//"
          LETSENCRYPT_EMAIL: "myuser@example.com"
