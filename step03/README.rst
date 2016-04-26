Step 3: Hello JSON
==================

We've modified the ``hello.py`` to output JSON_ rather than plain text.
We're using Flask's `jsonify()`_ function, which makes it easy to convert
Python data types into JSON output.

Run this application:

.. code-block:: bash

    $ python hello.py

Visit ``http://127.0.0.1:5000/`` in your web browser. You should see
``{"message": "Hello World!"}`` in your browser.

`Step 4: Hello Rover <https://github.com/singingwolfboy/build-a-flask-api/tree/master/step04>`_
=====================

.. _JSON: http://json.org/
.. _jsonify(): http://flask.pocoo.org/docs/0.10/api/#flask.json.jsonify
