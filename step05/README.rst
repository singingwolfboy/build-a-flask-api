Step 5: Multiple Puppies
========================

Rover is adorable, but our API isn't going to have just one puppy! We need
to handle multiple puppies, so we've changed the code to account for that.

We now have a ``PUPPIES`` variable, which is a list of all the puppies that
are in the API. At the moment, we have two puppies: Rover, and Spot. However,
we can always add more puppies to the list.

Now that we have more than one puppy, you have to indicate *which* puppy you
want the API to return. We've changed the URL of the ``get_puppy()`` view
so that you have to pass an index number in the URL. That number will be used
to determine which puppy you want the API to return.

Notice that we now need some error handling in the API. If you put a number
in the URL that is higher than the length of the ``PUPPIES`` list,
there isn't a puppy that corresponds to that number. If that happens,
we'll use Flask's `abort()`_ function to return an
HTTP 404 NOT FOUND response.

Try running the application again:

.. code-block::

    $ python puppy.py

This time, you'll get a 404 response if you try to visit
``http://127.0.0.1:5000/``, since we no longer have a view for that URL.
However, you can visit ``http://127.0.0.1:5000/0`` or
``http://127.0.0.1:5000/1``. For conciseness, we'll call those URLs ``/0``
and ``/1``.

What happens if you visit ``/2``? What about ``/-1``? What about some silly
URLs, like ``/one`` or ``/purple``? Give it a try!

Try editing the ``puppy.py`` file to add a few more puppies to the ``PUPPIES``
list. Can you display those puppies in the API?

`Step 6: Slugs <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step06>`_
===============

.. _abort(): http://flask.pocoo.org/docs/0.10/api/#flask.abort
