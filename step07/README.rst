Step 7: SQLAlchemy
==================

In order to proceed, we need to start separating the different parts of our
API into different places. This makes it easier to think about each different
part, and see how they all fit together. The first separation we're going
to make is separating data and views.

"Data" is the information that your API provides: in this case, Rover and Spot.
"Views" are how the information is displayed in your API. So far, data and
views have been stored in the place: the ``puppy.py`` file. However, data
doesn't belong in Python files, it belongs in a database.

Object Relational Mappers
-------------------------

We need to make our data separate, so it isn't clogging up our Python files.
However, it also needs to be accessible, so that we can get that data when
we need it. `Object relational mappers`_, or ORMs, can help us achieve this
balance. By using an ORM, we can define Python classes that represent the
data in the database, and then use standard Python methods on those classes
to access the database and pull out data when we need it. Python has a few
ORMs, but the best one is SQLAlchemy_. Fortunately, there's a handy Flask
extension called `Flask-SQLAlchemy`_ that makes using SQLAlchemy with Flask
fairly straightforward.

Defining a Model
----------------

When using a database, you have to consider how your data is structured.
With an ORM, you can define that structure using a Python class. Open the
``models.py`` file, and you'll see that we have a ``Puppy`` data model all
ready to go. This data model has four attributes: ``id``, ``slug``,
``name``, and ``image_url``.

``id`` is an integer that the database uses to keep track of every puppy
it knows about. In Step 5, when the ``PUPPIES`` variable was a list, each
puppy could be identified by a number; the ``id`` attribute is very much
like that. ``slug`` is the slug that we discussed in Step 6, a name that
can be used to look up a specific puppy. Since each puppy has both an ``id``
and a ``slug``, you can use either one to find a puppy! We'll set
``index=True`` on the ``slug`` property, so that the database can look up
a puppy by its slug much faster.

We're already familiar with the ``name`` and ``image_url`` attributes.
They just hold information about each puppy, like the dictionaries that we
used before. We'll also set ``nullable=False`` on these two properties, to
indicate that each puppy *must* have a name, and *must* have an image_url.

Integrating Flask-SQLAlchemy
----------------------------

In order to integrate our data model with our Flask application, we need to
integrate Flask-SQLAlchemy by calling ``db.init_app(app)``. SQLAlchemy also
needs to know where to find a database, which is why we need to define
``app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///puppy.db"``. We are using
sqlite_, which makes it very easy to get started: there's nothing to install!

Querying on a Model
-------------------

Our ``Puppy`` model has a ``query`` attribute as well, which is used for
making database queries. In the ``get_puppy()`` view, we need to use this
to find the right puppy.

When you access ``Puppy.query``, it's all set to return *all* the puppies
defined in the database. But we don't want all of them in this view, we just
want one. To find the one we want, we need to filter down the results using
the slug from the URL. We can do that like this:

.. code-block:: python

    Puppy.query.filter(Puppy.slug==slug)

That will select *only* the puppies that have a matching slug. Once we've
filtered down the results of the query, we need to actually *get* a result
from the database. To do that, we can use the ``.first()`` method, but
Flask-SQLAlchemy provides something even nicer: ``.first_or_404()``. Just like
the ``.first()`` method, this tries to return the first result from the
filtered query. However, if there are no results in the database that match
the query, ``.first_or_404()`` will call ``abort(404)``, so that the page
will return a 404 Not Found response. It's doing the error-checking for you!

Once we have the puppy object, we need to transform it back into a Python
dictionary so that the ``jsonify()`` function can handle it. This is sort of
annoying, but in a few steps, we'll learn how to make this transformation
happen automatically.

Creating and Seeding Database Tables
------------------------------------

Now that we're adding a database to our application, we need to tell the
database how our data is structured. We've already done this in Python,
in our ``models.py`` file, but the database doesn't know about it yet.
In order to pass along that information, we need to run a task that will
communicate with the database and tell it how the data will be structured.

To do this, we've added some new lines at the end of the file, after the
``if __name__ == "__main__":`` section. These lines will only run once when
you execute the Python file, rather than once for every HTTP request, like
the ``get_puppy()`` function does.

The first task we've added is the "createdb" task. The Python code checks to
see if you ran the ``puppy.py`` file with a command that includes the word
"createdb". If so, it will run ``db.create_all()``, which contacts the
database and creates the database tables, which is how the database knows
how the data will be structured. If you run this command, the code will *not*
execute ``app.run()``, and so the web server won't run. The code will create
the database tables and immediately quit.

The second task we've added is the "seeddb" task. Once the database tables
have been created, they start out empty, which is not very useful for our
API. In order to put Rover and Spot back in our API, they first need to go
into the database. The "seeddb" command will make the code create two
``Puppy`` objects, one for Rover and one for Spot, and insert them into the
database via the SQLAlchemy session. Just like the previous command, the code
will *not* execute ``app.run()``, so the web server won't run. The code will
seed this information into the database tables and immediately quit.

Give It a Try
-------------

Well, that was a lot of information! Now it's time to try actually running
this database-enabled application! First, we need to install the
Flask-SQLAlchemy Python module. Make sure that you have your virtual
environment activated, and then run:

.. code-block::

    $ pip install -r requirements.txt

That command will read the ``requirements.txt`` file in this directory, which
lists all of the Python modules that should be installed. In this case, there's
two: Flask, and Flask-SQLAlchemy. Once they're both properly installed,
create and seed the database:

.. code-block::

    $ python puppy.py createdb
    Database created!
    $ python puppy.py seeddb
    Database seeded!

When you run this code, you may see warnings about something called
``SQLALCHEMY_TRACK_MODIFICATIONS``. This is unrelated to this tutorial, and
any warnings that mention it can be ignored.

And then run the application, just as before:

.. code-block::

    $ python puppy.py
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat

Try visiting a few URLs. The application should work exactly as it did in
Step 6. In Step 8, we'll use the database to start doing some things that we
couldn't do before.

`Step 8: Creating Data from the API <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step08>`_
====================================

.. _Object relational mappers: https://en.wikipedia.org/wiki/Object-relational_mapping
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _Flask-SQLAlchemy: http://flask-sqlalchemy.pocoo.org/
.. _sqlite: https://www.sqlite.org/
