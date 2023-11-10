import os
import base64
import urllib3
import json

 
http = urllib3.PoolManager()

slack_endpoint = os.environ['slack_endpoint']
weather_endpoint = os.environ['weather_endpoint']
 
# slack_endpoint = "https://hooks.slack.com/services/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"
# weather_endpoint = "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/016000.json"
 
 
def lambda_handler(event, context):
    # get weather result
    weather_result = get_weather()
    if weather_result["success"]:
        # compose weather info to markdown message
        weather_msg = compose_weather_message(weather_result["data"])
        forward_slack_message(weather_msg)
    else:
        weather_msg = weather_result["error_message"]
    forward_slack_message(weather_msg)
 
 
def forward_slack_message(message_content):
    msg = {
        "channel": "#weatherchannel",
        "username": "nancy",
        "text": message_content,
        "icon_emoji": ""
    }
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST', slack_endpoint, body=encoded_msg)
 
 
def compose_weather_message(weather):
    return "*{0}  _{1}_  {2} 地域の天気情報です*\n{3}\n{4}".format(
        weather['publishingOffice'],
        weather['reportDatetime'],
        weather['targetArea'],
        weather['headlineText'],
        weather['text']
    )
 
 
def get_weather():
    result = {"success": True, "error_message": "OK"}
    try:
        resp = http.request(method="GET", url=weather_endpoint, headers={"Content-Type": "application/json"})
        if resp.status == 200 and resp.data:
            weather = json.loads(resp.data)
            # print(weather)
            result["data"] = weather
        else:
            msg = "Failed get weather, response code: {0}, response: {1}".format(resp.status, resp)
            print(msg)
            result["success"] = False
            result["error_message"] = msg
        return result
    except Exception as e:
        result["success"] = False
        result["error_message"] = str(e)
        print("天気予報の情報取得に失敗しました")
    return result
