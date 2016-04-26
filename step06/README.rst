Step 6: Slugs
=============

Numbers are nice, but sometimes we want to have more readable URLs. Rather
than a numerical identifier, some websites and APIs use slugs in their URLs.
A slug_ is an identifier that is usually generated from a name or title, so
that a URL can identify a resource and still be readable. Slugs are typically
entirely lowercase, with punctuation removed and spaces replaced by dashes.

We've changed ``puppy.py`` so that each puppy has a slug that is based on his
name. ``PUPPIES`` is no longer a list, but is now a dictionary. Each key in
the dictionary is a slug, and the key's value is the puppy that the slug
refers to. Rover's slug is "rover", and Spot's slug is "spot", so it's pretty
straightforward to see who is who.

In the ``get_puppy()`` view, we're now doing a dictionary lookup using the
slug passed in the URL. The exception type has changed, since a failed
dictionary lookup raises a ``KeyError`` while a failed list lookup raises
an ``IndexError``, but aside from that, the function is identical.

Run the application again and try a few URLs. Do ``/0`` and ``/1`` still work?
Do ``/rover`` and ``/spot`` work? How about ``/purple``? Try adding more
puppies to the ``PUPPIES`` dictionary, and see if they show up in the API.

`Step 7: SQLAlchemy <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step07>`_
====================

.. _slug: https://en.wikipedia.org/wiki/Slug_(web_publishing)
