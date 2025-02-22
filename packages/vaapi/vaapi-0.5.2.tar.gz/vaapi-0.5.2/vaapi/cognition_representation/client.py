import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..types.cognition_representation import CognitionRepresentation

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)

class CognitionRepresentationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> CognitionRepresentation:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',  
            api_key="YOUR_API_KEY",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/cognitionrepr/{jsonable_encoder(id)}/", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CognitionRepresentation, _response.json())  # type: ignore
            _response_json = _response.json()
            
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a Motion Representation.

        <Warning>This action can't be undone!</Warning>

        You will need to supply the logs's unique ID. You can find the ID in 
        the django admin panel or in the log settings in the UI. 
        Parameters
        ----------
        id : int
            A unique integer value identifying this annotation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',  
            api_key="YOUR_API_KEY",
        )
        client.annotations.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/cognitionrepr/{jsonable_encoder(id)}/", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: int,
        *,
        log_id: typing.Optional[int] = OMIT,
        frame_number: typing.Optional[int] = OMIT,
        representation_name: typing.Optional[str] = OMIT,
        representation_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CognitionRepresentation:
        """
        Update attributes for an existing annotation.

        You will need to supply the annotation's unique ID. You can find the ID in the Label Studio UI listed at the top of the annotation in its tab. It is also listed in the History panel when viewing the annotation. Or you can use [Get all task annotations](list) to find all annotation IDs.

        For information about the JSON format used in the result, see [Label Studio JSON format of annotated tasks](https://labelstud.io/guide/export#Label-Studio-JSON-format-of-annotated-tasks).

        Parameters
        ----------
        id : int
            A unique integer value identifying this annotation.

        result : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Labeling result in JSON format. Read more about the format in [the Label Studio documentation.](https://labelstud.io/guide/task_format)

        task : typing.Optional[int]
            Corresponding task for this annotation

        project : typing.Optional[int]
            Project ID for this annotation

        completed_by : typing.Optional[int]
            User ID of the person who created this annotation

        updated_by : typing.Optional[int]
            Last user who updated this annotation

        was_cancelled : typing.Optional[bool]
            User skipped the task

        ground_truth : typing.Optional[bool]
            This annotation is a Ground Truth

        lead_time : typing.Optional[float]
            How much time it took to annotate the task (in seconds)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Annotation
            Updated annotation

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.annotations.update(
            id=1,
            result=[
                {
                    "original_width": 1920,
                    "original_height": 1080,
                    "image_rotation": 0,
                    "from_name": "bboxes",
                    "to_name": "image",
                    "type": "rectanglelabels",
                    "value": {
                        "x": 20,
                        "y": 30,
                        "width": 50,
                        "height": 60,
                        "rotation": 0,
                        "values": {"rectanglelabels": ["Person"]},
                    },
                }
            ],
            was_cancelled=False,
            ground_truth=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/cognitionrepr/{jsonable_encoder(id)}/",
            method="PATCH",
            json={
                "log_id": log_id,
                "frame_number": frame_number,
                "representation_name": representation_name,
                "representation_data": representation_data,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CognitionRepresentation, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
            self, 
            #log_id: int, *, 
            request_options: typing.Optional[RequestOptions] = None,
            **filters: typing.Any) -> typing.List[CognitionRepresentation]:
        """
        List all logs.

        You will need to supply the event ID. You can find this in ...

        Parameters
        ----------
        log_id : int
            Game ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CognitionRepresentation]
            CognitionRepresentation

        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',  
            api_key="YOUR_API_KEY",
        )
        client.annotations.list(
            id=1,
        )
        """
        query_params = {k: v for k, v in filters.items() if v is not None}
        _response = self._client_wrapper.httpx_client.request("api/cognitionrepr/", method="GET", request_options=request_options,params=query_params)
        #_response = self._client_wrapper.httpx_client.request(
        #    f"api/cognitionrepr/?log={jsonable_encoder(log_id)}", method="GET", request_options=request_options
        #)
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[CognitionRepresentation], _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        log_id: typing.Optional[int] = OMIT,
        frame_number: typing.Optional[int] = OMIT,
        representation_name: typing.Optional[str] = OMIT,
        representation_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CognitionRepresentation:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',  
            api_key="YOUR_API_KEY",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/cognitionrepr/",
            method="POST",
            json={
                "log_id": log_id,
                "frame_number": frame_number,
                "representation_name": representation_name,
                "representation_data": representation_data,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CognitionRepresentation, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def bulk_create(
        self,
        *,
        repr_list: typing.List[CognitionRepresentation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CognitionRepresentation:
        """
        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',  
            api_key="YOUR_API_KEY",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/cognitionrepr/",
            method="POST",
            json=repr_list,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CognitionRepresentation, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
    
    def get_repr_count(
            self,
            request_options: typing.Optional[RequestOptions] = None,
            **filters: typing.Any) -> typing.Optional[int]:
        """
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',  
            api_key="YOUR_API_KEY",
        )
        """
        query_params = {k: v for k, v in filters.items() if v is not None}
        _response = self._client_wrapper.httpx_client.request("api/cognitionrepr/count/", method="GET", request_options=request_options,params=query_params)
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.Dict[str, typing.Any], _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)