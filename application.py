from flask import Flask, render_template, request
from simple_recommender import recommend, recommend_nmf
from deneme_1_2_3 import recommend_nmf2, films
from def_convert_dict import convert

#print(films)

app = Flask(__name__)


@app.route('/')
def hello_fun():
    return render_template("main.html", movies = films, title1="Cascabel")

@app.route("/recommendations") 
def recommender():
     #user_input_from_app = request.args
     user_input_from_app = dict(request.args)
     print("++++++++++++++++++++++++++++++++++++")
     print(f"this is the dictionary : {user_input_from_app}")
     my_dict = convert(user_input_from_app)
     print("------------------------------------")
     print(f"this is my_dict : {my_dict}")
     print("bu bir testtir")
     top3_films = recommend_nmf2(my_dict)
     return render_template("recommender.html", films_var = top3_films)

if __name__ == '__main__':
    app.run(debug=True, port=5000)























