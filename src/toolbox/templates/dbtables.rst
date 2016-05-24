================================
{{ group_name|capfirst }} tables
================================

{% block content %}{% endblock %}
{% for object in model_list %}

------------

*********************
{{ object.db_table }}
*********************

{{ object.doc.strip|safe }}

**Sample:** `{{ object.get_tsv_name }} <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/{{ object.get_tsv_name }}>`_

{% if object.FILING_FORMS|length > 0 %}
Filing forms
============

{% for form, sections in object.get_filing_forms_w_sections %}
{% if sections|length > 1 %}
* `{{ form.type_and_num|safe }} <filingforms.html#{{ form.type_and_num|slugify }}>`_ ({{ form.title|safe }})
{% for section in sections %}
    * {{ section.title|safe }}
{% endfor %}
{% elif sections|length == 1 %}
* `{{ form.type_and_num|safe }} <filingforms.html#{{ form.type_and_num|slugify }}>`_ ({{ form.title|safe }}): {{ sections.0.title|safe }}
{% else %}
* `{{ form.type_and_num|safe }} <filingforms.html#{{ form.type_and_num|slugify }}>`_ ({{ form.title|safe }})
{% endif %}
{% endfor %}
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
            <td>{{ field.name }}</td>
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
Look-up Codes
=============
{% for field in object.choice_fields %}

{{ field.name }}
----------------

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
                <td>{{ choice.0 }}</td>
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
* {{ doc }} ({% for object in objects %}`{{ object.start_page }}{% if object.end_page %}-{{ object.end_page }}{% endif %} <{{ object.canonical_url }}>`_{% if not forloop.last %}, {% endif %}{% endfor %})
{% endfor %}
{% endif %}

{% endif %}
{% endfor %}
