{{ group_name|capfirst }} forms
===============================

{% block content %}{% endblock %}

{% for form in form_list %}

------------

{{ form.type_and_num|safe }}
~~~~~~~~~~~~~

{{ form.title|safe }}

{{ form.description|safe }}
{% if form.sections|length > 0 %}
Sections
^^^^^^^^
{% for section in form.sections %}
* {{ section.title|safe }} {% if section.documentcloud.start_page %}(`p. {{ section.documentcloud.start_page }}{% if section.documentcloud.end_page %}-{{ section.documentcloud.end_page }}{% endif%} <{{ section.documentcloud.canonical_url }}>`_){% endif %}

{% endfor %}
{% endif %}

{% if not form.documentcloud_id %}
*No PDF available.*
{% else %}
Example Form
^^^^^^^^^^^^


.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-{{ form.documentcloud.id }}" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/{{ form.documentcloud.id }}.js", {
      container: "#DV-viewer-{{ form.documentcloud.id }}",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href={{ form.documentcloud.pdf_url }}>{{ form.documentcloud.title }} (PDF)</a>
      <br />
      <a href={{ form.documentcloud.text_url }}>{{ form.documentcloud.title }} (Text)</a>
    </noscript>

{% endif %}

{% if form.get_models|length > 0 %}
Database Tables
^^^^^^^^^^^^^^^
Data collected via {{ form.type_and_num|safe }} filings are written to the following tables:
{% for model in form.get_models %}
* `{{ model.klass_name }} <models.html#{{ model.klass_name|slugify }}>`_
{% endfor %}
{% endif %}

{% endfor %}
