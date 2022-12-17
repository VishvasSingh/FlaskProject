from flask import Flask , request
import requests
app = Flask(__name__)

stores = [
    {
        "name": "Apple store",
        "items": [
        {
            "name":"ipad air 5",
            "price":"52000"
        }

        ]
    }
]

gadgets = [
    {
        "category" : "phone",
        "names":[
            {
                "name":"Iphone",
                "special_features" : "expensive"
            },
            {
                "name":"one plus",
                "special_features": "fast charging"
            },
            {
                "name":"nokia",
                "special_features": "can we used as a weapon"
            }
        ]
    },
    {
        "category" : "tablet",
        "names": [
            {
                "name" : "ipad",
                "special_features" : "brilliant device"
            },
            {
                "name":"android tab",
                "special_features" : "just a big phone"
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return  {"stores":stores}

def get_a_device(category , special_feature=None):
    for each_dict in gadgets:
        if category == each_dict["category"] and special_feature is None:
            return each_dict
        elif category == each_dict["category"] and special_feature is not None:
            for each_device in each_dict["names"]:
                if special_feature == each_device["special_features"]:
                    return each_device

    return gadgets


@app.get("/fav_device")
def get_fav_device():
    return {"fav_device": get_a_device("123")}

@app.post("/fav_device")
def add_fav_device():
    request_data = request.get_json()
    gadgets.append(request_data)
    return gadgets,201

@app.post("/fav_device/<string:name>/item")
def add_new_kind_of_device(name):
    request_data = request.get_json()
    for each_list in gadgets:
        if each_list["category"]==name:
            each_list["names"].append(request_data)
            return request_data,201
    return {}, 404

@app.get("/fav_device/<string:name>/item")
def get_category(name):
    for each_list in gadgets:
        if each_list["category"]==name:
            return each_list
    return {}

# @app.get("/fav_device/<string:name>/item/<string:itemname>")
# def get_category(name,itemname):
#     for each_list in gadgets:
#         if each_list["category"]==name:
#             for each_name in each_list["names"]:
#                 if itemname == each_name[name]:
#                     return each_name
#     return {}

response = requests.get("http://api.kanye.rest")
print(response.json())
