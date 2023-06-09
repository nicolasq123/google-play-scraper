from google_play_scraper import app as gapp
from flask import Flask
from flask import request, jsonify

app =Flask(__name__)

# kv, ours_key: result_key
trans_dict = {
    "icon": "icon",
    "screenshots": "screenshots",
    "name": "title",
    "package_name": "appId",
    "store_url": "url", 
    "category": "category",
    "description": "description",
    "videos": "video",
}


@app.route('/', methods=["GET"])
def index():
    data = {
        "c": 0,
        "d": {},
    }
    package = request.args.get("package")
    if not package:
        data["c"] = -1
        data["m"] = "package empty error"
        return jsonify(data) 

    lang = request.args.get("lang", "en")
    if not lang:
        lang = 'en'
    country = request.args.get("country", "us")
    if not country:
        country = "us"

    try:
        result = gapp(
            package,
            lang=lang,
            country=country
        )
        tmp = {}
        for k,v in trans_dict.items():
            tmp[k] = result.get(v, "")

        if tmp.get('videos') and isinstance(tmp['videos'], str):
            tmp['videos'] = [tmp['videos']]
        else:
            tmp['videos'] = []

        data['d'] = tmp
    except Exception as e:
        data = {
            "c": -1,
            "m": str(e),
        }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
