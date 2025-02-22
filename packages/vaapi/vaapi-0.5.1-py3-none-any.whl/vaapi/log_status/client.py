import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..types.log_status import LogStatus

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)

class LogStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> LogStatus:
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
            f"api/log-status/{jsonable_encoder(id)}/", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(LogStatus, _response.json())  # type: ignore
            _response_json = _response.json()
            
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete the log status for one log.

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
            f"api/log-status/{jsonable_encoder(id)}/", method="DELETE", request_options=request_options
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
        log_id: int,
        *,
        BallModel: typing.Optional[int] = OMIT,
        BallCandidates: typing.Optional[int] = OMIT,
        BallCandidatesTop: typing.Optional[int] = OMIT,
        CameraMatrix: typing.Optional[int] = OMIT,
        CameraMatrixTop: typing.Optional[int] = OMIT,
        FieldPercept: typing.Optional[int] = OMIT,
        FieldPerceptTop: typing.Optional[int] = OMIT,
        GoalPercept: typing.Optional[int] = OMIT,
        GoalPerceptTop: typing.Optional[int] = OMIT,
        MultiBallPercept: typing.Optional[int] = OMIT,
        RansacLinePercept: typing.Optional[int] = OMIT,
        RansacCirclePercept2018: typing.Optional[int] = OMIT,
        ShortLinePercept: typing.Optional[int] = OMIT,
        ScanLineEdgelPercept: typing.Optional[int] = OMIT,
        ScanLineEdgelPerceptTop: typing.Optional[int] = OMIT,
        OdometryData: typing.Optional[int] = OMIT,
        IMUData: typing.Optional[int] = OMIT,
        FSRData: typing.Optional[int] = OMIT,
        ButtonData: typing.Optional[int] = OMIT,
        SensorJointData: typing.Optional[int] = OMIT,
        AccelerometerData: typing.Optional[int] = OMIT,
        InertialSensorData: typing.Optional[int] = OMIT,
        MotionStatus: typing.Optional[int] = OMIT,
        MotorJointData: typing.Optional[int] = OMIT,
        GyrometerData: typing.Optional[int] = OMIT,
        num_cognition_frames: typing.Optional[int] = OMIT,
        num_motion_frames: typing.Optional[int] = OMIT,
        num_jpg_bottom: typing.Optional[int] = OMIT,
        num_jpg_top: typing.Optional[int] = OMIT,
        num_bottom: typing.Optional[int] = OMIT,
        num_top: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogStatus:
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
            Updated annotationhttps://vat.berlin-united.com/

        Examples
        --------
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',  
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
            f"api/log-status/{jsonable_encoder(log_id)}/",
            method="PATCH",
            json={
                "BallModel": BallModel,
                "BallCandidates": BallCandidates,
                "BallCandidatesTop": BallCandidatesTop,
                "CameraMatrix": CameraMatrix,
                "CameraMatrixTop": CameraMatrixTop,
                "FieldPercept": FieldPercept,
                "FieldPerceptTop": FieldPerceptTop,
                "GoalPercept": GoalPercept,
                "GoalPerceptTop": GoalPerceptTop,
                "MultiBallPercept": MultiBallPercept,
                "RansacLinePercept": RansacLinePercept,
                "RansacCirclePercept2018": RansacCirclePercept2018,
                "ShortLinePercept": ShortLinePercept,
                "ScanLineEdgelPercept": ScanLineEdgelPercept,
                "ScanLineEdgelPerceptTop": ScanLineEdgelPerceptTop,
                "OdometryData": OdometryData,
                "IMUData": IMUData,
                "FSRData": FSRData,
                "ButtonData": ButtonData,
                "SensorJointData": SensorJointData,
                "AccelerometerData": AccelerometerData,
                "InertialSensorData": InertialSensorData,
                "MotionStatus": MotionStatus,
                "MotorJointData": MotorJointData,
                "GyrometerData": GyrometerData,
                "num_cognition_frames": num_cognition_frames,
                "num_motion_frames": num_motion_frames,
                "num_jpg_bottom": num_jpg_bottom,
                "num_jpg_top": num_jpg_top,
                "num_bottom": num_bottom,
                "num_top": num_top,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(LogStatus, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
            self, 
            #log_id: int, *, 
            request_options: typing.Optional[RequestOptions] = None,
            **filters: typing.Any) -> typing.List[LogStatus]:
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
        typing.List[LogStatus]
            LogStatus

        Examples
        --------
        ```python
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',  
            api_key="YOUR_API_KEY",
        )
        client.log_status.list(log_id=1)
        ```
        """
        query_params = {k: v for k, v in filters.items() if v is not None}
        _response = self._client_wrapper.httpx_client.request("api/log-status/", method="GET", request_options=request_options,params=query_params)
        #_response = self._client_wrapper.httpx_client.request(
        #    f"api/cognitionrepr/?log={jsonable_encoder(log_id)}", method="GET", request_options=request_options
        #)
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[LogStatus], _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        log_id: typing.Optional[int] = OMIT,
        BallModel: typing.Optional[int] = OMIT,
        BallCandidates: typing.Optional[int] = OMIT,
        BallCandidatesTop: typing.Optional[int] = OMIT,
        CameraMatrix: typing.Optional[int] = OMIT,
        CameraMatrixTop: typing.Optional[int] = OMIT,
        FieldPercept: typing.Optional[int] = OMIT,
        FieldPerceptTop: typing.Optional[int] = OMIT,
        GoalPercept: typing.Optional[int] = OMIT,
        GoalPerceptTop: typing.Optional[int] = OMIT,
        MultiBallPercept: typing.Optional[int] = OMIT,
        RansacLinePercept: typing.Optional[int] = OMIT,
        RansacCirclePercept2018: typing.Optional[int] = OMIT,
        ShortLinePercept: typing.Optional[int] = OMIT,
        ScanLineEdgelPercept: typing.Optional[int] = OMIT,
        ScanLineEdgelPerceptTop: typing.Optional[int] = OMIT,
        OdometryData: typing.Optional[int] = OMIT,
        IMUData: typing.Optional[int] = OMIT,
        FSRData: typing.Optional[int] = OMIT,
        ButtonData: typing.Optional[int] = OMIT,
        SensorJointData: typing.Optional[int] = OMIT,
        AccelerometerData: typing.Optional[int] = OMIT,
        InertialSensorData: typing.Optional[int] = OMIT,
        MotionStatus: typing.Optional[int] = OMIT,
        MotorJointData: typing.Optional[int] = OMIT,
        GyrometerData: typing.Optional[int] = OMIT,
        num_cognition_frames: typing.Optional[int] = OMIT,
        num_motion_frames: typing.Optional[int] = OMIT,
        num_jpg_bottom: typing.Optional[int] = OMIT,
        num_jpg_top: typing.Optional[int] = OMIT,
        num_bottom: typing.Optional[int] = OMIT,
        num_top: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogStatus:
        """

        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        ```python
        from vaapi.client import Vaapi

        client = Vaapi(
            base_url='https://vat.berlin-united.com/',  
            api_key="YOUR_API_KEY",
        )
        ```
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/log-status/",
            method="POST",
            json={
                "log_id": log_id,
                "BallModel": BallModel,
                "BallCandidates": BallCandidates,
                "BallCandidatesTop": BallCandidatesTop,
                "CameraMatrix": CameraMatrix,
                "CameraMatrixTop": CameraMatrixTop,
                "FieldPercept": FieldPercept,
                "FieldPerceptTop": FieldPerceptTop,
                "GoalPercept": GoalPercept,
                "GoalPerceptTop": GoalPerceptTop,
                "MultiBallPercept": MultiBallPercept,
                "RansacLinePercept": RansacLinePercept,
                "RansacCirclePercept2018": RansacCirclePercept2018,
                "ShortLinePercept": ShortLinePercept,
                "ScanLineEdgelPercept": ScanLineEdgelPercept,
                "ScanLineEdgelPerceptTop": ScanLineEdgelPerceptTop,
                "OdometryData": OdometryData,
                "IMUData": IMUData,
                "FSRData": FSRData,
                "ButtonData": ButtonData,
                "SensorJointData": SensorJointData,
                "AccelerometerData": AccelerometerData,
                "InertialSensorData": InertialSensorData,
                "MotionStatus": MotionStatus,
                "MotorJointData": MotorJointData,
                "GyrometerData": GyrometerData,
                "num_cognition_frames": num_cognition_frames,
                "num_motion_frames": num_motion_frames,
                "num_jpg_bottom": num_jpg_bottom,
                "num_jpg_top": num_jpg_top,
                "num_bottom": num_bottom,
                "num_top": num_top,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(LogStatus, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

