#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.annotations.filing_forms import all_filing_forms

class Command(CalAccessCommand):
    help = 'Generate documentation for CAL-ACCESS forms'

    def handle(self, *args, **kwargs):
        self.docs_dir = os.path.join(
            settings.REPO_DIR,
            'docs',
            'calaccess',
            'filingforms',
        )
        os.path.exists(self.docs_dir) or os.makedirs(self.docs_dir)

        group_dict = {}

        for form in all_filing_forms:
            try:
                group_dict[form.group.lower()].append(form)
            except KeyError:
                group_dict[form.group.lower()] = [form]

        for group, forms in group_dict.iteritems():
            context = {
                'group_name': group,
                'form_list': forms,
                'form_count': len(forms),
            }

            template_name = '{}_forms.rst'.format(group.replace(' ', '_'))
            rendered = render_to_string(template_name, context)
            target_file = os.path.join(
                self.docs_dir,
                template_name,
            )

            with open(target_file, 'w') as f:
                f.write(rendered)
