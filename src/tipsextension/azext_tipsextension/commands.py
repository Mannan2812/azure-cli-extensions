# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_tipsextension._client_factory import cf_tipsextension


def load_command_table(self, _):

    # TODO: Add command type here
    # tipsextension_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#None.{}',
    #    client_factory=cf_tipsextension)


    with self.command_group('tipsextension') as g:
        g.custom_command('create', 'get_all_datasets')
        g.custom_command('get-all-dataset', 'get_all_datasets')
        g.custom_command('get-dataset','get_dataset')
        g.custom_command('put-dataset','put_dataset')
        g.custom_command('delete-dataset','delete_dataset')
        g.custom_command('get-sub', 'get_dataset_sundirectories')
        # g.command('delete', 'delete')
        g.custom_command('list', 'list_tipsextension')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_tipsextension')


    with self.command_group('tipsextension', is_preview=True):
        pass

