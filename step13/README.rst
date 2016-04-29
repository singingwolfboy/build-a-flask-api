Step 13: User Cleanup
=====================

We've got the basics done for our user feature in step 12, but we have some
cleaning up to do. So, let's do it!

Make 401 Errors Return JSON
---------------------------

Just like we did in step 11, making 401 errors return JSON instead of HTML is
pretty easy. We just use Flask's error handling system to define the output.

User Schema
-----------

You probably saw how the ``user_profile`` view had to reach into the `User`
model to pull out the attributes, just like the ``get_puppy`` view was doing
before. Let's solve that problem with a `UserSchema`, which lives in the
``schemas.py`` file.

`Step 14: ??? <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step14>`_
=======================

.. _Flask-Login: https://flask-login.readthedocs.io
