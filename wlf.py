# Wolf ram alpha API
import Data
import wolframalpha
from sp_function import *


def get_ans(q):

    # App id obtained by the above steps
    app_id = 'Y8K4RR-3HQ74A8TVT'

    # Instance of wolf ram alpha
    # client class

    client = wolframalpha.Client(app_id)

    # Stores the response from
    # wolf ram alpha
    res = client.query(q)

    # Includes only text from the response
    answer = next(res.results).text

    print(f"Linux Assistant: {answer}")
    g_speak(answer)
