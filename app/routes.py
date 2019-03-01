from app import app
from flask import render_template, jsonify, request
import requests
from app.forms import FlickrForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    photos = []


    form = FlickrForm()

    if form.validate_on_submit():
        search = form.title.data
        print(search)


        url = 'https://api.flickr.com/services/rest/?&api_key=ec3753885115b39d675e6b4b90555a91&method=flickr.photos.search&format=json&text={}&nojsoncallback=1'.format(search)

        photos = requests.get(url).json()
        print(photos)


    return render_template('index.html', photos=photos, form=form)
