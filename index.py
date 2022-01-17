

from flask import Flask, abort, send_file
import json
import requests
from io import BytesIO

url = "https://supply-fetch.vercel.app/"
img_ipfs = "https://gateway.pinata.cloud/ipfs/QmQdrUc7aiFPLLXvwwyxMUCoNRSasNH1ZZPxDkEZ2uLagR/"
application = Flask(__name__)


@application.route('/image/<filename>')
def get_image(filename):

    token_id = filename.split(".")[0]

    supply = requests.get(url).text

    image = requests.get(str(img_ipfs+str(token_id)+".png"))
    img = BytesIO(image.content)
    return send_file(img, mimetype='image/gif')
