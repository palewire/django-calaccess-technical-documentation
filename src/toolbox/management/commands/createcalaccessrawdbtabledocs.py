#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from re import sub
from django.conf import settings
from calaccess_raw import get_model_list
from django.template.loader import render_to_string
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generate documentation for raw CAL-ACCESS database tables'

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
            'dbtables',
        )
        self.refresh_dc_cache = options['refresh-dc-cache']
        if self.refresh_dc_cache:
            self.docs_cached = []

        os.path.exists(self.docs_dir) or os.makedirs(self.docs_dir)

        model_list = get_model_list()
        group_list = {}
        for m in model_list:
            # add doc_title (key) and list of documentcloud objects (value) to each model
            m.docs = {}
            for doc in sorted(
                m().DOCUMENTCLOUD_PAGES,
                key=lambda x: x.start_page
            ):
                if self.refresh_dc_cache and doc.id not in self.docs_cached:
                    doc._cache_metadata()
                    self.docs_cached.append(doc.id)
                try:
                    m.docs[doc.title].append(doc)
                except KeyError:
                    m.docs[doc.title] = [doc]
            # add choice field list to model
            m.choice_fields = []
            for field in m._meta.fields:
                if len(field.choices) > 0:
                    # add doc title, page_url list to each choice field
                    field.docs = {}
                    for doc in sorted(
                        field.documentcloud_pages,
                        key=lambda x: x.start_page
                    ):
                        if self.refresh_dc_cache and doc.id not in self.docs_cached:
                            doc._cache_metadata()
                            self.docs_cached.append(doc.id)
                        try:
                            field.docs[doc.title].append(doc)
                        except KeyError:
                            field.docs[doc.title] = [doc]
                    m.choice_fields.append(field)
            try:
                group_list[m().klass_group].append(m)
            except KeyError:
                group_list[m().klass_group] = [m]

        for group, models in group_list.iteritems():
            template_name = '{}_tables.rst'.format(group)

            context = {
                'group_name': group,
                'model_list': models,
                'model_count': len(models),
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
