# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from .vendored_sdks.oscp.dataplane import OpenSupplyChainPlatformServiceAPI as dpclient
from .vendored_sdks.oscp.dataplane.models._models import *

def initialize_client(auth):
    client = dpclient(base_headers = {
    "Authorization": f"Bearer {auth}"
})
    return client
def create_tipsextension(cmd, resource_group_name, tipsextension_name, location=None, tags=None):
    raise CLIError('TODO: Implement `tipsextension create`')


def list_tipsextension(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `tipsextension list`')


def update_tipsextension(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance

def get_all_datasets(auth):
    client = initialize_client(auth)
    res = client.dataset.get_all_datasets()
    for dataset in res:
        print(f"Name: {dataset.name}")
def get_dataset(auth, dataset_name):
    client = initialize_client(auth)
    res = client.dataset.get(dataset_name)
    print(res)
def put_dataset(auth, dataset_name, disabled):
    client = initialize_client(auth)
    disabled = False
    dataset = Dataset(name= dataset_name, is_disabled = disabled)
    print(dataset)
    res = client.dataset.put(dataset_name, dataset)
    print(res)
def delete_dataset(auth, dataset_name):
    client = initialize_client(auth)
    res = client.dataset.delete(dataset_name)
    print(res)
def get_dataset_sundirectories(auth, dataset_name):
    client = initialize_client(auth)
    res = client.dataset.get_sub_directories_of_dataset(dataset_name)
    print(res)
