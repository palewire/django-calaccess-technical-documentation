{% extends "base.rst" %}
{% load misc_tags %}

{% block content %}
===============================
{{ group_name|capfirst }} forms
===============================

{% block intro %}{% endblock %}

{% for form in form_list %}

------------

{{ form.type_and_num|safe }}
---------------

{{ form.title|safe }}

{{ form.description|safe }}
{% if form.sections|length > 0 %}
Sections
````````
{% for section in form.sections %}
* {{ section.title|safe }} {% if section.documentcloud.start_page %}(`p. {{ section.documentcloud.start_page }}{% if section.documentcloud.end_page %}-{{ section.documentcloud.end_page }}{% endif%} <{{ section.documentcloud.canonical_url }}>`_){% endif %}

{% endfor %}
{% endif %}

{% if form.get_models|length > 0 %}
Database tables
```````````````

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    {% for model in form.get_models %}
        <tr>
            <td>
                <a href="../dbtables/{{ model.klass_group }}_tables.html#{{ model.db_table|format_page_anchor }}">
                    {{ model.db_table }}
                </a>
            </td>
        </tr>
    {% endfor %}
    </tbody>
    </table>
    </div>
{% endif %}


{% if form.documentcloud_id %}
Sample
``````

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

{% endfor %}
{% endblock %}

