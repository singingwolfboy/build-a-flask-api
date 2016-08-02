Step 8: Creating Data from the API
==================================

Now that our data and views are separated, it's possible to modify one without
modifying the other. In practical terms, this means you can create, edit, and
delete data without needing to re-write your Python code! Not only is that
super nifty, but it's also an important part of creating a dynamic API.

In the ``puppy.py`` file, we've now added a new view called ``create_puppy()``.
This view is only accessible via the HTTP POST method, which is the proper
method to use for HTTP requests that create data on the server. This view
can be broadly divided into three parts: validating incoming data, inserting
the data into the database, and returning an informative HTTP response.

Validate Incoming Data
----------------------

In order to create a new puppy on the server, the incoming HTTP request has
to specify some information for that puppy. In this case, the request has to
specify the puppy's ``name`` and ``image_url`` properties. In Flask, you
can access information about the incoming HTTP request from the request_ object
imported from Flask. HTTP POST data is available from the ``form`` property
on this ``request`` object.

We've specified in the data model that every puppy *must* have a ``name``
and an ``image_url`` -- note the ``nullable=False`` option on those two
columns when you look at ``models.py``. As a result, if you try to create
a puppy without both of those values, the request should fail. That's why
the ``create_puppy()`` view first checks that both values are present, and
if either one is missing, the view returns a 400 Bad Request HTTP response,
along with a message indicating what the problem was. The way this code is
implemented, the responses will be returned as plain text rather than JSON,
which is unfortunate, but we'll fix that later.

Once we have both a ``name`` and an ``image_url``, we can generate a ``slug``
from the ``name`` property. Flask doesn't have a ``slugify()`` function by
default, but fortunately, there's a handy `slugify module`_ that we can install
with Pip. We've added this dependency to the ``requirements.txt`` file, so it's
easier to keep track of. Once it's installed, we can use the ``slugify()``
function provided by that module to generate a slug from the puppy's name.
Now, our new puppy will have a slug, without the person using the API needing
to send us one. Making things easier for our users is a good thing to do!

Insert Data Into Database
-------------------------

Now that we have the data that we need for our puppy, we can construct a
``Puppy`` object with that data, and pass it to the SQLAlchemy_ session.
Note that we don't need to specify an ``id`` for this puppy -- the database
will assign one automatically. Remember that the data doesn't actually
get inserted into the database until you call ``db.session.commit()``!

Return a HTTP Response
----------------------

Great, we've successfully created a new puppy! Now, we need to inform the user
that we've done so. There are also a few standard REST practices that we
should follow here:

1. Provide a human-readable message confirming that the puppy was created.
2. Set the HTTP response code to 201 Created instead of the default 200 OK.
   This is more correct, since we did, in fact, create some new data.
3. Set the Location header to a URL where the user can find more information
   about the newly-created puppy. By asking us to create this new puppy,
   the user is basically asking this API to store some data for them -- it's
   nice to tell the user where they can go to get this data *back*.

In order to do these things, we create a response object with the
``jsonify()`` function, but we don't return it immediately. For the first
item, we'll make sure to put a friendly message in the dictionary that we
pass to ``jsonify()``. For the second item, we can directly set the
``status_code`` attribute on the response to 201.
Finally, for the third item, we use the `url_for()`_ function to determine
what the proper URL should be for the new puppy, and set the Location header
to that URL. Once we've done all those things, we can return the response
object, and Flask will send it along to the user. Done!

Testing It Out
--------------

You don't think we're going to ship this API without testing it first, do you?
Start out by installing the new dependencies, so that we can run the code:

.. code-block:: bash

    $ pip install -r requirements.txt

Then run the application the same way you've done in the past:

.. code-block::

    $ python puppy.py
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat

We can use a web browser to make sure that ``get_puppy()`` view still works,
but testing views that require POST methods is difficult with a browser. It's
easier to use a different tool, and the best tool for the job is curl_, a
command-line swiss army knife for making HTTP requests. To test out ``curl``,
try running a basic GET request, like this:

.. code-block:: bash

    $ curl 127.0.0.1:5000/rover
    {
      "image_url": "http://example.com/rover.jpg",
      "name": "Rover"
    }

There's our good friend, just like he was in the web browser! The ``curl``
command takes a *lot* of different options, but the most relevant ones are:

``-X [method]``
    Set the HTTP method. To make a POST request, use ``-X POST``
``-d [key]=[value]``
    Set a key-value pair in the POST data. You can use this option multiple
    times, and ``curl`` will combine them all together. To set a ``name``
    value to ``Lassie`` and a ``image_url`` value to
    ``http://example.com/lassie.jpg``, use
    ``-d name=Lassie -d image_url=http://example.com/lassie.jpg``
``-i``
    Make ``curl`` display the HTTP response headers, in addition to the
    response body.

To make a new puppy named Lassie, you can run the following command:

.. code-block:: bash

    $ curl 127.0.0.1:5000/ -X POST -d name=Lassie -d image_url=http://example.com/lassie.jpg -i

Give it a try, and see what happens! Try making other puppies, as well. You can
never have too many puppies!

`Step 9: Transforming Data with Marshmallow <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step09>`_
============================================


.. _request: http://flask.pocoo.org/docs/0.10/api/#flask.request
.. _slugify module: https://github.com/un33k/python-slugify
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _url_for(): http://flask.pocoo.org/docs/0.10/api/#flask.url_for
.. _curl: https://curl.haxx.se/
