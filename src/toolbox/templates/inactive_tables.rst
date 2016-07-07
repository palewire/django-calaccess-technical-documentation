{% extends "dbtables.rst" %}

{% block intro %}
We've classifed the following {{ model_count }} tables because:

1. An empty .TSV file of the same name is included in the daily CAL-ACCESS exports; or
2. The date field on the table indicating when each record was created contains only dates older than three years ago.
{% endblock %}
