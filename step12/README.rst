Step 12: Users
==============

Our API is looking great! Let's add a new feature: users. So far, each API
request has been made by an anonymous user, so there's no way to grant
different permissions to different users. Once we can differentiate users,
then we can start making API endpoints that return information specific to
the user requesting it.

Flask-Login
-----------

We're going to use the excellent `Flask-Login`_ extension to handle user
authentication. We've added that dependency to the ``requirements.txt`` file,
and used it in ``models.py`` to create a new `User` class. This user has a
``name`` and an ``api_key``, which is kind of like a password for an API.
A user will need to provide his or her API key on every API request, in order
to be identified.

In ``puppy.py``, we've configured a `LoginManager`, which knows how to
identify users. In our project, we've taught the `LoginManager` object how
to look up a user by ID, and how to identify a user based on the `Authorization`
header in an incoming HTTP request.

Who Am I?
---------

We've also added a ``/whoami`` view to our Flask API. By sending a HTTP request
to that view, we can find out who the `LoginManager` believes we are. If
it can't figure it out, the view will say that we're anonymous.

We've added an example user to the ``seeddb`` task, with an API key
of ``abc123``. Create and seed the database, and test out this ``/whoami`` view!

.. code-block:: bash

    $ curl 127.0.0.1:5000/whoami
    {
      "name": "anonymous"
    }

.. code-block:: bash

    $ curl 127.0.0.1:5000/whoami -H "Authorization: abc123"
    {
      "name": "Jack London"
    }

Login-Protected Views
---------------------

Now that we can differentiate between users, we can also make views that are
*only* accessible to users that are logged in. Flask-Login makes this easy,
by providing a `login_required` decorator. We've created a ``/profile``
view that uses this decorator, which you should test out, as well.

.. code-block:: bash

    $ curl 127.0.0.1:5000/profile
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>401 Unauthorized</title>
    <h1>Unauthorized</h1>
    <p>The server could not verify that you are authorized to access the URL
    requested.  You either supplied the wrong credentials (e.g. a bad password),
    or your browser doesn't understand how to supply the credentials required.</p>

.. code-block:: bash

    $ curl 127.0.0.1:5000/profile -H "Authorization: abc123"
    {
      "api_key": "abc123",
      "name": "Jack London"
    }

That HTML in the 401 Unauthorized response is a bit ugly. We'll clean that up
in the next step.

`Step 13: User Cleanup <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step13>`_
=======================

.. _Flask-Login: https://flask-login.readthedocs.io
