# helpers.py

import json
import time
from selenium.common import WebDriverException

def retrieve_phone_code(driver) -> str:
    """Devuelve un número de confirmación de teléfono como string.
    Se utilizará después de solicitar el código de confirmación en la aplicación."""
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utilizar 'retrieve_phone_code' solo después de haber solicitado el código en la aplicación.")
        return code