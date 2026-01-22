from flask import Flask, render_template, request
from predict import predict_wine


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None


    if request.method == 'POST':
        features = [float(request.form[f'f{i}']) for i in range(13)]
        prediction = predict_wine(features)


    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)