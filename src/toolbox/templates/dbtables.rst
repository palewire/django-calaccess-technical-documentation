{% extends "base.rst" %}
{% block content %}
================================
{{ group_name|capfirst }} tables
================================

{% block intro %}{% endblock %}
{% for object in model_list %}

------------

*********************
{{ object.db_table }}
*********************

{{ object.doc.strip|safe }}

**Sample:** `{{ object.get_tsv_name }} <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/{{ object.get_tsv_name }}>`_

.. raw:: html

    <iframe src="http://raw.githubusercontent.com/california-civic-data-coalition/django-calaccess-raw-data/master/example/test-data/tsv/CVR_SO_CD.TSV"></iframe>

{% if object.FILING_FORMS|length > 0 %}
Forms
=====

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        {% for form, sections in object.get_filing_forms_w_sections %}
        <tr>
            <td>
                <a href="../filingforms/{{ form.group|lower }}_forms.html#{{ form.type_and_num|slugify }}">{{ form.type_and_num|safe }}</a>:
                {{ form.title|safe }}
            </td>
        </tr>
        {% for section in sections %}
        <tr>
            <td>- {{ section.title|safe }}</td>
        </tr>
        {% endfor %}
        {% endfor %}
    </tbody>
    </table>
{% endif %}

{% if object.get_unique_key_list|length > 0 %}
Unique key
==========

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <tbody valign="top">
        <tr>
        {% for field in object.get_unique_key_list %}
            <td><code>{{ field }}</code></td>
        {% endfor %}
        </tr>
    </tbody>
    </table>
{% endif %}

Fields
======

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    {% for field in object.get_field_list %}
    {% if field.name != "id" %}
        <tr>
            <td><code>{{ field.db_column }}</code></td>
            <td>{{ field.description }}</td>
            <td>{% if field.is_unique_key %}Yes{% else %}No{% endif %}</td>
            <td>{{ field.definition|capfirst }}</td>
        </tr>
    {% endif %}
    {% endfor %}
    </tbody>
    </table>
    </div>

{% if object.choice_fields|length > 0 %}
Lookup Codes
============
{% for field in object.choice_fields %}

``{{ field.name }}``
--------------------

.. raw:: html

    <div class="wy-table-responsive">
        <table border="1" class="docutils">
        <thead valign="bottom">
            <tr>
                <th class="head">Code</th>
                <th class="head">Definition</th>
            </tr>
        </thead>
        <tbody valign="top">
        {% for choice in field.choices %}
            <tr>
                <td><code>{{ choice.0 }}</code></td>
                <td>{{ choice.1 }}</td>
            </tr>
        {% endfor %}
        </tbody>
        {% if field.documentcloud_pages|length > 0%}
        <tfoot class="footnote">
        <tr>
        <td colspan=2>
           <small>
            Sources:
                {% for doc, objects in field.docs.items %} {{ doc }} ({% for object in objects %}<a class="reference external image-reference" href="{{ object.canonical_url }}">{{ object.formatted_page_nums }}</a>{% if not forloop.last %}, {% endif %}{% endfor %}){% if not forloop.last %}, {% endif %}{% endfor %}
            </small>
        </td>
        </tr>
        </tfoot>
        {% endif %}
        </table>
    </div>
{% endfor %}

{% if object.DOCUMENTCLOUD_PAGES|length > 0 %}
Source Docs
^^^^^^^^^^^
{% for doc, objects in object.docs.items %}
* {{ doc }} ({% for object in objects %}`{{ object.formatted_page_nums }} <{{ object.canonical_url }}>`_{% if not forloop.last %}, {% endif %}{% endfor %})
{% endfor %}
{% endif %}

{% endif %}
{% endfor %}
{% endblock %}
