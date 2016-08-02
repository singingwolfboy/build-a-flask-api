Step 11: Minor Cleanups
=======================

In this step, we'll do a few minor cleanups to make the code and the API
a bit cleaner.

Switch Back to IDs in URLs
--------------------------

Slugs are very useful in web applications, where we need readable URLs for
SEO purposes and a better user experience. However, APIs have different needs.
For APIs, stable URLs are more important than human-readable URLs. Now that
we've added the ability for users to edit an existing puppy, it's possible
for the puppy's URL to change, which is a bad thing. Integer IDs, while not
as readable, will *never* change for a given item in the database. As a result,
it's a better candidate to use in the URL of an API. However, we'll leave
the ``slug`` column in the database, so that a web application can use it
if necessary.

Once we've made this change, we can also remove the "Location" header from
the HTTP response to the ``edit_puppy()`` view. Since a puppy's URL can't
change anymore, there's no need to remind the user what the URL is.

Add a ``/puppies`` Prefix to URLs
---------------------------------

Prefixing the ID with the data type gives us more flexibility to add new data
types to our API. Maybe we'll want to create a "Person" class, and associate
puppies with people. Using data types in URLs means we won't have to worry
about if ID #5 means puppy #5 or person #5 -- the URL will say so explicitly!

Add a ``url`` Property to the Puppy Model
-----------------------------------------

Python properties aren't stored in the database, but are calculated
automatically when referenced. Since puppies now have stable URLs, it makes
sense to define a ``url`` property, so that it's easy to look up a puppy's
URL from Python. We use this in the ``create_puppy()`` view, to set the
"Location" header.

Add a Basic ``list_puppies()`` View
-----------------------------------

Creating a new view to see all puppies in the database allows a user to browse
through the existing data, rather than always creating new data. In this step,
we've added a trivial implementation that is nearly an exact copy of the
``get_puppy()`` view. We simply had to create another schema that knows how
to handle multiple puppies, and pass that schema a list of all the puppies
in the database.

However, this basic view will cause problems if there are many, many puppies
in the database. Can you imagine trying to output a million puppies in one
HTTP request, or even more? In the future, we'll improve on this view to make
it more performant. But for now, this is a reasonable prototype.

Make 404 Errors Return JSON
---------------------------

It's kind of annoying to have the entire API return JSON, except for when you
encounter a 404 Not Found exception, which returns HTML. We can use Flask's
error handling system to modify the 404 response, so that it returns JSON
instead.

`Step 12: Users <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step12>`_
================

.. _Representational State Transfer: https://en.wikipedia.org/wiki/Representational_state_transfer
