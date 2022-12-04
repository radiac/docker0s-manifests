=============================
docker0s manifest: smtp-relay
=============================

This is an open mail relay for use by your docker host and other docker0s applications.

Take care to not open it to the world.


This manifest:

* creates an internal ``smtp-relay`` network
* listens for outgoing mail on port 25 on the ``smtp-relay`` network
* optionally listens on localhost port 25 on your docker host
* relays outgoing mail through your ISP's relay to ensure deliverability


Known limitations:

* your relay host must allow outgoing email using the address your docker0s applications
  send from
* no authentication - this is by design, it is intended for internal trusted services


Environment variables
=====================

``MAIL_HOST``
  The docker0s host to say where the emails are originating from

  Default: ``my.example.com``

``RELAY_HOST``
  The ISP relay host which will be relaying your emails

  Default: ``mail.example.org``

``RELAY_PORT``
  The port the ISP relay host is listening on

  Default: ``25``

``RELAY_USERNAME``
  The username for connecting to the ISP relay host

  Default: ``me@example.com``

``RELAY_PASSWORD``
  The password for connecting to the ISP relay host

  Default: ``secret``


Template variables
==================

``bind_host``
  If set, bind to 127.0.0.1:25

  Default: ``False``


Example usage
=============

Prepare a host ready to relay mail from the host and other containers::

    host:
      name: myserver.example.com
      user: myuser

    apps:
      smtp-relay:
        path: git+https://github.com/radiac/docker0s-manifests#smtp-relay
        env:
          MAIL_HOST: "my.example.com"
          RELAY_HOST: "mail.example.org"
          RELAY_PORT: 25
          RELAY_USERNAME: "me@example.com"
          RELAY_PASSWORD: "secret"
        compose_context:
          bind_host: true
