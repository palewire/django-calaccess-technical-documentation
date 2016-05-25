#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from re import sub
from django.conf import settings
from django.template.loader import render_to_string
from django.core.management.base import BaseCommand
from calaccess_raw.annotations.filing_forms import all_filing_forms


class Command(BaseCommand):
    help = 'Generate documentation for CAL-ACCESS forms'

    def add_arguments(self, parser):
        parser.add_argument(
            "--refresh-dc-cache",
            action="store_true",
            dest="refresh-dc-cache",
            default=False,
            help="Request and cache current metadata from DocumentCloud API."
        )

    def handle(self, *args, **options):
        self.docs_dir = os.path.join(
            settings.REPO_DIR,
            'docs',
            'calaccess',
            'filingforms',
        )
        os.path.exists(self.docs_dir) or os.makedirs(self.docs_dir)

        group_dict = {}

        for form in all_filing_forms:
            if options['refresh-dc-data'] and form.documentcloud:
                form.documentcloud._cache_metadata()
            try:
                group_dict[form.group.lower()].append(form)
            except KeyError:
                group_dict[form.group.lower()] = [form]

        for group, forms in group_dict.iteritems():
            template_name = '{}_forms.rst'.format(group.replace(' ', '_'))
            context = {
                'group_name': group,
                'form_list': forms,
                'form_count': len(forms),
                'template_name': template_name,
                'command_name': sub(r'(.+\.)*', '', self.__class__.__module__),
            }

            rendered = render_to_string(template_name, context)
            target_file = os.path.join(
                self.docs_dir,
                template_name,
            )

            with open(target_file, 'w') as f:
                f.write(rendered)
