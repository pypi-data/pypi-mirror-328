import requests
import traceback
from collections import OrderedDict
from ..constants.error_constants import ErrorConstants
from ..utils import mask_fields_in_data
from ..loggers.logger import Logger

logger = Logger()


class Service:
    # extension optional
    request_base_url = ""
    mask_request_headers_fields = []
    mask_request_data_fields = []
    mask_response_headers_fields = []
    mask_response_data_fields = []

    class Request:
        # extension optional
        default_headers = {}
        default_data = {}
        default_json = {}

        def __init__(
            self,
            url="",
            parameters=None,
            method="GET",
            headers=None,
            cookies=None,
            data=None,
            json=None,
            files=None,
            verify_ssl=True
        ):
            """
            data and json are mutually exclusive parameters
            data can accept any Content-Type header
            json will add the application/json Content-Type header
            """
            # apply default headers
            self.headers = self.default_headers.copy()
            self.headers.update({} if headers is None else headers)

            # apply default data and json
            if isinstance(data, dict):
                self.data = self.default_data.copy()
                self.data.update({} if data is None else data)
            else:
                self.data = data

            if isinstance(json, dict):
                self.json = self.default_json.copy()
                self.json.update({} if json is None else json)
            else:
                self.json = json

            # defaults
            self.parameters = {} if parameters is None else parameters
            self.cookies = {} if cookies is None else cookies
            self.files = {} if files is None else files

            self.url = url
            self.method = method
            self.verify_ssl = verify_ssl

    class Response:
        def __init__(
            self,
            status_code=400,
            headers=None,
            cookies=None,
            data=None
        ):
            # defaults
            self.headers = {} if headers is None else headers
            self.cookies = {} if cookies is None else cookies
            self.data = {} if data is None else data

            self.status_code = status_code

    def __init__(self, *args, **kwargs):
        pass

    def request(self, *args, **kwargs):
        return self.invoke(self.Request(*args, **kwargs))

    def invoke(self, request):
        logger.debug(f"{self.__class__.__name__}.invoke", priority=2)
        logger.debug(f"request url: {self.request_base_url + request.url}")
        logger.debug(f"request method: {request.method}")
        logger.debug(f"request headers: {mask_fields_in_data(request.headers, self.mask_request_headers_fields)}")
        logger.debug(f"request cookies: {request.cookies}")
        if request.data:
            logger.debug(f"request data: {mask_fields_in_data(request.data, self.mask_request_data_fields)}")
        else:
            logger.debug(f"request json: {mask_fields_in_data(request.json, self.mask_request_data_fields)}")

        # open all files before sending them
        opened_request_files = OrderedDict()
        for key, file in request.files.items():
            opened_request_files[key] = open(file, "rb")

        try:
            requests_response = requests.request(
                url=self.request_base_url + request.url,
                params=request.parameters,
                method=request.method,
                headers=request.headers,
                cookies=request.cookies,
                data=request.data,
                json=request.json,
                files=opened_request_files,
                verify=request.verify_ssl
            )

            response_status_code = requests_response.status_code
            response_headers = dict(requests_response.headers)
            response_cookies = dict(requests_response.cookies)

            try:
                response_data = requests_response.json()
            except:  # noqa
                response_data = requests_response.text

            logger.debug(f"{self.__class__.__name__}.invoke - Response", priority=3)
            logger.debug(f"response status code: {response_status_code}")
            logger.debug(f"response headers: {mask_fields_in_data(response_headers, self.mask_response_headers_fields)}")
            logger.debug(f"response cookies: {response_cookies}")
            logger.debug(f"response data: {mask_fields_in_data(response_data, self.mask_response_data_fields)}")

        except Exception as e:
            logger.error(f"{self.__class__.__name__}.invoke - error", priority=3)
            logger.error(f"{e.__class__.__name__}: {str(e)}")
            logger.error(traceback.format_exc())
            response_status_code = 500
            response_headers = {}
            response_cookies = {}
            response_data = {"error": ErrorConstants.App.INTERNAL_SERVER_ERROR}

        return self.Response(
            status_code=response_status_code,
            headers=response_headers,
            cookies=response_cookies,
            data=response_data
        )
