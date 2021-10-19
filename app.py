from typing import OrderedDict
from flask import Flask, jsonify, render_template, request
import json
from collections import OrderedDict
app = Flask(__name__)


@app.route('/')
def greetings():
    return "<center><h1>GREETINGS!!</h1><a href='product/get'>/product/get</a> is the GET endpoint <br><br><a href='product/post'>/product/post</a> is the POST endpoint</center>"


@app.route('/product/get', methods=['GET'])
def get_request():
    with open('product.json', 'r') as j:
        data = json.load(j)
    return jsonify({'product': data})


@app.route('/product/post', methods=['POST', 'GET'])
def post_request():
    return render_template('post.html')


@app.route('/handle_data', methods=['POST'])
def handle_data():
    if request.method == "POST":
        with open('product.json', 'r') as j:
            data = json.load(j)
        category = request.form['category']
        name = request.form['name']
        rating = request.form['rating']
        image = request.form['image']
        description = request.form['description']
        size = (request.form['size']).split()
        condition = request.form['condition']
        color = request.form['color']
        price = request.form['price']
        availability = request.form['avail']
        discount = request.form['discount']
        keywords = (request.form['keywords']).split()
        new_dict = OrderedDict()
        new_dict = {"id": data[len(data) - 1]["id"]+1, "category": category, "name": name, "rating": rating, "image": image, "description": description,
                    "available": availability, "size": size, "condition": condition, "color": color, "price": price, "keywords": keywords, "discount": discount}
        data.append(new_dict)
        with open('product.json', 'w') as j:
            json.dump(data, j)
    return render_template('after_post.html')


if __name__ == '__main__':
    app.run(debug=True)
