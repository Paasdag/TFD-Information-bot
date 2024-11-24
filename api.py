import requests

api_key = ""
#put Nexon api key here ^

def get_user_info(username_tfd):
    modified_name = username_tfd.replace("#", "%23")
    
    url = "https://open.api.nexon.com/tfd/v1/id?user_name=" + modified_name
    headers = {
        "Content-Type": "application/json",
        "x-nxopen-api-key": api_key,
    }
    response = requests.get(url, headers=headers)
    
    data = response.json()
    l_ouid = data.get("ouid", "Invalid name")
    
    url2 = f"https://open.api.nexon.com/tfd/v1/user/basic?ouid=" + l_ouid
    
    response2 = requests.get(url2, headers=headers)
    data2 = response2.json()
    
    user_info = {
        "username": data2["user_name"],
        "platformtype": data2["platform_type"],
        "mastery": data2["mastery_rank_level"],
        "language": data2["game_language"]
    }
    

    return user_info

def get_ouid(username_tfd):
    modified_name = username_tfd.replace("#", "%23")
    url = "https://open.api.nexon.com/tfd/v1/id?user_name=" + modified_name
    headers = {
        "Content-Type": "application/json",
        "x-nxopen-api-key": api_key,
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    ouid = data.get("ouid", "Invalid name")
    return ouid