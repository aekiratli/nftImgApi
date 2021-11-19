

from flask import Flask, abort, send_file
import json
import requests
from io import BytesIO

url = "https://supply-fetch.vercel.app/"
img_ipfs = "https://gateway.pinata.cloud/ipfs/QmcJV2Kvta4ffP54Y3zW58zKYFMzwivEkkyp1rF2vp2pqX/"

file = open('nfts.json', 'r')
data = json.load(file)
application = Flask(__name__)


@application.route('/image/<filename>')
def get_image(filename):

    token_id = filename.split(".")[0]

    supply = requests.get(url).text

    if int(token_id) > (int(supply)-1):
        abort(404)

    image = requests.get(str(img_ipfs+str(token_id)+".png"))
    img = BytesIO(image.content)
    return send_file(img, mimetype='image/gif')