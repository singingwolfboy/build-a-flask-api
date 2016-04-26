Step 4: Hello Rover
===================

Now, we need to start thinking about what this API actually *does*. For
this tutorial, we'll make an API that can display information about puppies.
(There are too many kittens on the internet, and not enough puppies --
let's try to even the score a bit.)

We're renamed ``hello.py`` to ``puppy.py`` to reflect the meaning of the code.
We're also outputting JSON that describes a puppy, rather than outputting
"Hello World". Try running the application again:

.. code-block:: bash

    $ python puppy.py

Visit ``http://127.0.0.1:5000/`` in your web browser, and you'll see the JSON
that describes our puppy, Rover.

Rover has two attributes, "name" and "image_url". In the code, we define
"name" first, and "image_url" second. However, when you view the JSON API,
they might come out in the reverse order. Python dictionaries are unordered,
and so are JSON objects, so there's no way to know which order you'll
see the attributes in the JSON. However, that doesn't matter -- either order
is correct.

`Step 5: Multiple Puppies <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step05>`_
==========================
