Step 9: Transforming Data with Marshmallow
==========================================

Once again, we've reached a point where it's useful to separate the different
parts of our code into different places. Pulling the data out of Python and
into a database was a great help, but the entire Python codebase still needs
to know the shape and structure of that data. For example, in the
``get_puppy()`` view in step 8, we had to transform the puppy object into
a Python dictionary, like this:

.. code-block:: python

    output = {
        "name": puppy.name,
        "image_url": puppy.image_url,
    }

That means that any time we want to modify our data models, we also have to
go through all of our code and modify the parts that touch the models like
this. If we want to add a new field on our Puppy model, we have to modify
*many* different files to make it all work properly. We can do better.

Schemas
-------

Marshmallow_ is a library that solves this exact problem. It does data
serialization and deserialization, and also does data validation in the
process. Marshmallow has a rich ecosystem of integration systems, including
`a Flask extension`_ and `a SQLAlchemy extension`_, so it's perfect for our
needs. Those dependencies have been added to the ``requirements.txt`` file in
this directory.

The ``schemas.py`` file defines a Marshmallow schema for a puppy. A schema
defines how to transform an instance of a class into a dictionary, or vice
versa. Since we're using the integration systems that I mentioned earlier,
we can subclass from ModelSchema_, and it knows how to introspect a
SQLAlchemy model.

In the ``puppy.py`` file, we've modified the ``get_puppy()`` and
``create_puppy()`` views to use our Marshmallow schema. The ``get_puppy()``
method is now *super* tiny: we just run a SQLAlchemy query to get a puppy
object, and pass that object to the Marshmallow schema. The schema knows
how to transform that object into a dictionary, and from there, into JSON.

Validation
----------

The ``create_puppy()`` view is a bit shorter as well, but even more importantly,
it actually works *better* now than it did before. In Step 8, if you made
multiple errors in trying to create a puppy (like leaving off both ``name``
and ``image_url``), the HTTP response would only tell you about the first
error ("name required"). Once you fixed that first error, *then* it will tell
you the next error ("image_url required"), and so on. There was no way to know
how many problems you actually had! By contrast, the ``puppy_schema.load()``
function automatically does data validation, and if the validation fails,
it will return *all* the errors at once in that ``errors`` dictionary, rather
than just returning the first one. This means that you'll get much more
informative and useful error messages. Give it a try!

.. code-block:: bash

    $ curl 127.0.0.1:5000/ -X POST
    {
      "image_url": [
        "Missing data for required field."
      ],
      "name": [
        "Missing data for required field."
      ]
    }

Increased Flexibility
---------------------

Now our code is much more flexible. If we decide that we need more information
in our Puppy model, we can add it in one place (``models.py``), and not touch
*any* other code! Everything will just work. (The only exception is if you're
adding required columns, where ``nullable=False``, you'll of course need to
update the ``seeddb`` task so that it inserts seed data that has all the
required data.)

Try adding a new column to the Puppy model, and running the code again to see
how the views adapt. You may have to delete the ``puppy.db`` file, re-create,
and re-seed the database to make it run properly.

In addition, if you want to define exactly what information gets put into the
API, you can do that in one place. By default, Marshmallow will output all
four attributes of the puppy object: ``id``, ``slug``, ``name``,
and ``image_url``. If you want to switch back to just displaying ``name``
and ``image_url``, you can set a list of ``fields`` on the
``PuppySchema.Meta`` class, like this:

.. code-block:: python

    class PuppySchema(ma.ModelSchema):
        class Meta:
            model = Puppy
            fields = ["name", "image_url"]

`Check out the Marshmallow documentation for more information.
<https://marshmallow.readthedocs.org/en/latest/quickstart.html#refactoring-implicit-field-creation>`_

`Step 10: REST Semantics <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step10>`_
=========================

.. _Marshmallow: https://marshmallow.readthedocs.org/
.. _a Flask extension: https://flask-marshmallow.readthedocs.org
.. _a SQLAlchemy extension: https://marshmallow-sqlalchemy.readthedocs.org
.. _ModelSchema: https://marshmallow-sqlalchemy.readthedocs.org/en/latest/api_reference.html#marshmallow_sqlalchemy.ModelSchema
