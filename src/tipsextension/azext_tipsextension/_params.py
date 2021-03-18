# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType
from .vendored_sdks.oscp.dataplane.models._models import Dataset

def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    tipsextension_name_type = CLIArgumentType(options_list='--tipsextension-name-name', help='Name of the Tipsextension.', id_part='name')

    with self.argument_context('tipsextension') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('dataset_name',  options_list=['--name', '-n'])
        c.argument('auth', options_list=['--auth','-a'])
        c.argument('disabled', options_list = ['--disabled','-d'] )
    with self.argument_context('tipsextension list') as c:
        c.argument('tipsextension_name', tipsextension_name_type, id_part=None)
