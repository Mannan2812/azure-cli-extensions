# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.2.1, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, IO, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DeliveryNodeOperations(object):
    """DeliveryNodeOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~oscp.dataplane.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get(
        self,
        delivery_node_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DeliveryNode"
        """Retrieves the delivery node for given workspace ID and delivery node ID.

        Retrieves the delivery node for given workspace ID and delivery node ID.

        :param delivery_node_id: The delivery node identifier.
        :type delivery_node_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeliveryNode, or the result of cls(response)
        :rtype: ~oscp.dataplane.models.DeliveryNode
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeliveryNode"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        accept = "application/json, text/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'deliveryNodeId': self._serialize.url("delivery_node_id", delivery_node_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('DeliveryNode', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/deliveryNodes/{deliveryNodeId}'}  # type: ignore

    def put(
        self,
        delivery_node_id,  # type: str
        delivery_node,  # type: "_models.DeliveryNode"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DeliveryNode"
        """Inserts or updates the delivery node for given workspace ID and delivery node ID.

        Inserts or updates the delivery node for given workspace ID and delivery node ID.

        :param delivery_node_id: The delivery node identifier.
        :type delivery_node_id: str
        :param delivery_node: The delivery node to be inserted.
        :type delivery_node: ~oscp.dataplane.models.DeliveryNode
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeliveryNode, or the result of cls(response)
        :rtype: ~oscp.dataplane.models.DeliveryNode
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeliveryNode"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.put.metadata['url']  # type: ignore
        path_format_arguments = {
            'deliveryNodeId': self._serialize.url("delivery_node_id", delivery_node_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(delivery_node, 'DeliveryNode')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('DeliveryNode', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    put.metadata = {'url': '/deliveryNodes/{deliveryNodeId}'}  # type: ignore

    def delete(
        self,
        delivery_node_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Deletes the delivery node for given workspace ID and delivery node ID.

        Deletes the delivery node for given workspace ID and delivery node ID.

        :param delivery_node_id: The delivery node identifier.
        :type delivery_node_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        accept = "text/plain, application/json, text/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'deliveryNodeId': self._serialize.url("delivery_node_id", delivery_node_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.status_code == 200:
            deserialized = self._deserialize('IO', pipeline_response)

        if response.status_code == 200:
            deserialized = self._deserialize('IO', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delete.metadata = {'url': '/deliveryNodes/{deliveryNodeId}'}  # type: ignore

    def bulk_put(
        self,
        delivery_nodes,  # type: List["_models.DeliveryNode"]
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.BulkResponseItemOfDeliveryNode"]
        """bulk_put.

        :param delivery_nodes:
        :type delivery_nodes: list[~oscp.dataplane.models.DeliveryNode]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of BulkResponseItemOfDeliveryNode, or the result of cls(response)
        :rtype: list[~oscp.dataplane.models.BulkResponseItemOfDeliveryNode]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.BulkResponseItemOfDeliveryNode"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.bulk_put.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(delivery_nodes, '[DeliveryNode]')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('[BulkResponseItemOfDeliveryNode]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    bulk_put.metadata = {'url': '/deliveryNodes'}  # type: ignore

    def bulk_delete(
        self,
        delivery_node_ids,  # type: List[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.BulkResponseItemOfString"]
        """bulk_delete.

        :param delivery_node_ids:
        :type delivery_node_ids: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of BulkResponseItemOfString, or the result of cls(response)
        :rtype: list[~oscp.dataplane.models.BulkResponseItemOfString]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.BulkResponseItemOfString"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.bulk_delete.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(delivery_node_ids, '[str]')
        body_content_kwargs['content'] = body_content
        request = self._client.delete(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('[BulkResponseItemOfString]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    bulk_delete.metadata = {'url': '/deliveryNodes'}  # type: ignore

    def get_all_delivery_nodes(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.DeliveryNode"]
        """get_all_delivery_nodes.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of DeliveryNode, or the result of cls(response)
        :rtype: list[~oscp.dataplane.models.DeliveryNode]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.DeliveryNode"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        accept = "application/json, text/json"

        # Construct URL
        url = self.get_all_delivery_nodes.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('[DeliveryNode]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_all_delivery_nodes.metadata = {'url': '/deliveryNodes'}  # type: ignore
