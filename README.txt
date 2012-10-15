babel-dustjs
============

  [javascript: **.js]
  extract_messages = _

  [dustjs: **.html]

If you named this config file ``mapping.cfg``, you can run babel with
this config file like this::

  $ bin/pybabel extract -F mapping.cfg <some_directory>

You can also extract from a HTML file. The templates should be
embedded in script tags of type ``text/template`` like this::

  <html>
  <body>
    {@i18n}Hello world!{/i18n}
  </body>
  </html>
