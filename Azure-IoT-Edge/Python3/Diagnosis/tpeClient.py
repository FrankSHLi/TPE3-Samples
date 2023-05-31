import json, os.path, time, shutil
import requests

class tpeClient:

    _headers = {}

    def __init__(self):
        self._tpe_url_prefix = 'http://172.31.0.1:59000/api/v1'
        self._headers['Content-Type'] = 'application/json'
        self._headers['Authorization'] = 'Bearer ' + os.environ['token']

    def invoke_api(self, method, end_point, payload, stream):
        result = {}
        cmd_url = self._tpe_url_prefix + end_point
        try:
            if method.lower() == 'put':
                response = requests.put(cmd_url, json=payload, headers=self._headers, verify=False)
            elif method.lower() == 'post':
                response = requests.post(cmd_url, json=payload, headers=self._headers, verify=False)
            elif method.lower() == 'delete':
                response = requests.delete(cmd_url, json=payload, headers=self._headers, verify=False)
            elif method.lower() == 'patch':
                response = requests.patch(cmd_url, json=payload, headers=self._headers, verify=False)
            elif method.lower() == 'get':
                if stream:
                    response = requests.get(cmd_url, json=payload, headers=self._headers, verify=False, stream=True)
                else:
                    response = requests.get(cmd_url, json=payload, headers=self._headers, verify=False)
        except Exception as e:
            print(time.strftime('%Y/%m/%d %H:%M:%S') + ' Exception: ' + str(e))
            return str(e)

        if response.status_code >= 200 and response.status_code < 300 :
            if stream:
                filename = '/host/log/' + os.environ['IOTEDGE_GATEWAYHOSTNAME'] + '_' + time.strftime('%Y-%m-%d_%H-%M-%S') + '.zip'
                with open(filename, 'wb') as dest:
                    shutil.copyfileobj(response.raw, dest)
                result['message'] = filename
            else:
                result['message'] = response.text
        else:
            result['message'] = response.text
        result['status'] = response.status_code
        # print(response.status_code)
        # print(response.text)
        return result

