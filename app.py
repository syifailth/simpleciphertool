from flask import Flask,request,render_template
from algorithm import encrypt_caesar,encrypt_rot13,encrypt_vigenre,decrypt_caesar,decrypt_rot13
from algorithm import playfair_encrypt,decrypt_vigenre,encrypt_affine,decrypt_rot13

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def ciphertool():
    encrypted_text = ''
    algorithm = request.form.get('algorithm')

    if request.method == 'POST':
        if algorithm == 'vigenre':
            plain_text = request.form['plain_text']
            key = request.form['key']
            encrypted_text = encrypt_vigenre(plain_text,key)
        elif algorithm == 'caesar':
            plain_text = request.form['plain_text']
            key = request.form['key']
            encrypted_text = encrypt_caesar(plain_text,int(key))
        elif algorithm == 'affine':
            plain_text = request.form['plain_text']
            key = request.form['key']
            key2 = request.form['key2']
            encrypted_text = encrypt_affine(plain_text,int(key),int(key2))
        elif algorithm == 'playfair':
            plain_text = request.form['plain_text']
            key = request.form['key']
            encrypted_text = playfair_encrypt(plain_text,key)
        else:
            plain_text = request.form['plain_text']
            encrypted_text = encrypt_rot13(plain_text)

    return render_template('index.html',encrypted_text=encrypted_text,decision=algorithm)

@app.route('/decrypt/<algorithm>',methods=['GET','POST'])
def decrypttool(algorithm):
    decrypted_text = ''

    if request.method == 'POST':
        if algorithm == 'vigenre':
            plain_text = request.form['plain_text']
            key = request.form['key']
            decrypted_text = decrypt_vigenre(plain_text,key)
        elif algorithm == 'caesar':
            plain_text = request.form['plain_text']
            key = request.form['key']
            decrypted_text = decrypt_caesar(plain_text,int(key))
        else:
            plain_text = request.form['plain_text']
            decrypted_text = decrypt_rot13(plain_text)

    return render_template('index.html',decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)

