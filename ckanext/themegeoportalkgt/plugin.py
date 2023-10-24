# encoding: utf-8
from __future__ import annotations

from typing import Any, Callable

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import os
import ckan.lib.base as base
from ckan.common import CKANConfig, config
from ckan.config.declaration import Declaration, Key

def show_most_popular_groups():
    '''Return the value of the most_popular_groups config setting.

    To enable showing the most popular groups, add this line to the
    [app:main] section of your CKAN config file::

      ckan.example_theme.show_most_popular_groups = True

    Returns ``False`` by default, if the setting is not in the config file.

    :rtype: bool

    '''
    value = config.get('ckan.example_theme.show_most_popular_groups')
    return value


def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        {}, {'sort': 'package_count desc', 'all_fields': True})

    # Truncate the list to the 10 most popular groups only.
    groups = groups[:10]

    return groups

def no_registering(context, data_dict):
    return {'success': False, 'msg': toolkit._('''You cannot register for this
        site.''')}

class ThemegeoportalkgtPlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IConfigDeclaration)
    plugins.implements(plugins.IConfigurable, inherit=True)
    plugins.implements(plugins.IAuthFunctions, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, ckan_config):
        here = os.path.dirname(__file__)
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(ckan_config, 'templates')
        toolkit.add_public_directory(ckan_config, 'public')
        possible_licences_path = os.path.join(here,
                                              'resources',
                                              'json-list-of-licenses.json')
        if os.path.isfile(possible_licences_path):
            ckan_config['licenses_group_url'] = 'file://' \
                + possible_licences_path


    def get_helpers(self) -> dict[str, Callable[..., Any]]:
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'example_theme_most_popular_groups': most_popular_groups,
                'example_theme_show_most_popular_groups':
                show_most_popular_groups,
                }

    # IConfigDeclaration

    def declare_config_options(self, declaration: Declaration, key: Key):
        declaration.declare_bool(
            key.ckan.example_theme.show_most_popular_groups)

    def get_auth_functions(self):
        return {
            'user_create': no_registering
        }