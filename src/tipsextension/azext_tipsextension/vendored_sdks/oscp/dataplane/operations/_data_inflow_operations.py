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
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DataInflowOperations(object):
    """DataInflowOperations operations.

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

    def put_data_inflow(
        self,
        name,  # type: str
        data_inflow,  # type: "_models.DataInflow"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DataInflow"
        """Inserts or updates the data inflow for a workspace.

        Inserts or updates the data inflow for a workspace.

        :param name: The data inflow name.
        :type name: str
        :param data_inflow: The data inflow object.
        :type data_inflow: ~oscp.dataplane.models.DataInflow
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataInflow, or the result of cls(response)
        :rtype: ~oscp.dataplane.models.DataInflow
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DataInflow"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.put_data_inflow.metadata['url']  # type: ignore
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
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
        body_content = self._serialize.body(data_inflow, 'DataInflow')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('DataInflow', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    put_data_inflow.metadata = {'url': '/dataInflows/{name}'}  # type: ignore

    def get_data_inflow(
        self,
        name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DataInflow"
        """Retrieves the data inflow for given name and workspace.

        Retrieves the data inflow for given name and workspace.

        :param name: The data inflow name.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataInflow, or the result of cls(response)
        :rtype: ~oscp.dataplane.models.DataInflow
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DataInflow"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        accept = "application/json, text/json"

        # Construct URL
        url = self.get_data_inflow.metadata['url']  # type: ignore
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
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

        deserialized = self._deserialize('DataInflow', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_data_inflow.metadata = {'url': '/dataInflows/{name}'}  # type: ignore

    def delete_data_inflow(
        self,
        name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DataInflow"
        """Deletes  the data inflow for given name and workspace.

        Deletes  the data inflow for given name and workspace.

        :param name: The data inflow name.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataInflow, or the result of cls(response)
        :rtype: ~oscp.dataplane.models.DataInflow
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DataInflow"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        accept = "application/json, text/json"

        # Construct URL
        url = self.delete_data_inflow.metadata['url']  # type: ignore
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('DataInflow', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delete_data_inflow.metadata = {'url': '/dataInflows/{name}'}  # type: ignore

    def get_all_data_inflows(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.DataInflow"]
        """Retrieves all the data inflows for given workspace.

        Retrieves all the data inflows for given workspace.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of DataInflow, or the result of cls(response)
        :rtype: list[~oscp.dataplane.models.DataInflow]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.DataInflow"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        accept = "application/json, text/json"

        # Construct URL
        url = self.get_all_data_inflows.metadata['url']  # type: ignore

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

        deserialized = self._deserialize('[DataInflow]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_all_data_inflows.metadata = {'url': '/dataInflows'}  # type: ignore

    def post_data_inflow_run(
        self,
        name,  # type: str
        data_inflow_run,  # type: "_models.DataInflowRun"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DataInflowRun"
        """Inserts the data inflow run request for a workspace.

        Inserts the data inflow run request for a workspace.

        :param name: The data inflow name.
        :type name: str
        :param data_inflow_run: The data inflow run object.
        :type data_inflow_run: ~oscp.dataplane.models.DataInflowRun
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataInflowRun, or the result of cls(response)
        :rtype: ~oscp.dataplane.models.DataInflowRun
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DataInflowRun"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json, text/json"

        # Construct URL
        url = self.post_data_inflow_run.metadata['url']  # type: ignore
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
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
        body_content = self._serialize.body(data_inflow_run, 'DataInflowRun')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('DataInflowRun', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    post_data_inflow_run.metadata = {'url': '/dataInflows/{name}/run'}  # type: ignore
