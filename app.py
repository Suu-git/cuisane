from flask import Flask, render_template, request
import guessing_alphabet
Score_alphabet=0
BScore_alphabet=0
app = Flask(__name__,template_folder="templates")

@app.route('/')
def home():
	return render_template('alphabet.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
	global Score_alphabet
	global BScore_alphabet
	if request.method == 'POST':
		try:
			url=request.form['imageconverted']
			word_to_detect=request.form['word_to_detect']
			guessing_alphabet.download_image_ipg(url, 'Alphabet/images/', 'data')
			predicted_alphabet=guessing_alphabet.detecting_image_alphabet('Alphabet/images/data.png')
			if word_to_detect==predicted_alphabet:
				Score_alphabet=Score_alphabet+1
				if BScore_alphabet<Score_alphabet:
					BScore_alphabet = Score_alphabet
			else:
				Score_alphabet=0
			return render_template('alphabet.html',output="WORD: "+str(word_to_detect)+"\n"+"YOU: "+str(predicted_alphabet), score="SCORE: "+str(Score_alphabet),best_score="BEST: "+str(BScore_alphabet))
		except:
			return render_template('alphabet.html', output="PREDICTED NUMBER: ")
	return render_template('alphabet.html', score="SCORE: "+str(Score_alphabet))



if __name__ == '__main__':
    app.run(debug=True)