Step 10: REST Semantics
=======================

You may have heard of "RESTful APIs", and wondered what that meant. REST
(or ReST) is an acronym for `Representational State Transfer`_, which is a
certain architectual style. Basically, if an API conforms to the REST style,
then it behaves in a predictable manner and is easier to learn and use.

In order to make our API more RESTful, we need to implement a few more features.
Users of this API can view and create puppies, but they can't yet edit puppies
or delete them. Let's add edit and delete functionality!

Edit
----

We now have a ``edit_puppy()`` function that will update the attributes of a
puppy. Thanks to our Marshmallow schema, it looks almost identical to the
``create_puppy()`` method! We simply find the puppy that we want to edit,
and pass it to the ``puppy_schema`` object as the ``instance`` that it should
update. Easy-peasy.

Delete
------

The ``delete_puppy()`` function is even easier! There's no input from the user,
so we don't need to use our Marshmallow schema at all. Instead, we just look
up the puppy that should be deleted, and call ``db.session.delete()``.
Done! Notice that this view uses the ``DELETE`` HTTP method, which makes a
lot of sense.

Give It a Try
-------------

Try playing around with these new views using ``curl``. Make a new puppy, view
it, edit it, view it again, delete it, and then try to view it after it's
been deleted. You're using a real RESTful API!

`Step 11: Minor Cleanups <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step11>`_
=========================

.. _Representational State Transfer: https://en.wikipedia.org/wiki/Representational_state_transfer
