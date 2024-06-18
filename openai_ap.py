from openai import OpenAI
apikey = "sk-proj-Hm2r8BSlz1POuVgDoJrUT3BlbkFJ7mU52FAwa5dTHIjbYrMj"


def gpt_getanswer(text):
    client = OpenAI(api_key=apikey)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response[0]['text']
