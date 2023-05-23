import os
from flask import Flask, flash, request, redirect, url_for, render_template, session
from werkzeug.utils import secure_filename
import webview


app = Flask(__name__)
#window = webview.create_window('File flask-python-desk',app)
UPLOAD_FOLDER = './static'
app.config['SECRET_KEY'] = "123olamundo123"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx','py'}



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


var = 'File_Not_Found'
lista = []
arquivo = []
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        
        file  = request.files['file' ]
        file1 = request.files['file1']
        file2 = request.files['file2']
        file3 = request.files['file3']
        file4 = request.files['file4']
        
        # Se o usuario nao selecionar um arquivo, o navegador envia um
        # arquivo vazio sem um nome de arquivo.
        
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        
        if file and allowed_file(file.filename ):
            filename = secure_filename(file.filename)            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],   filename  ) )
            lista.clear()
            lista.append(filename)           
         
    
        if file1 and allowed_file(file1.filename ):
            filename = secure_filename(file1.filename)            
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'],   filename  ) )
           
            lista.append(filename) 

        else:
            lista.append(var)



        if file4 and allowed_file(file4.filename ):
            filename = secure_filename(file4.filename)            
            file4.save(os.path.join(app.config['UPLOAD_FOLDER'],   filename  ) )
           
            lista.append(filename) 

        else:
            lista.append(var)

        if file2 and allowed_file(file2.filename ):
            filename = secure_filename(file2.filename)            
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'],   filename  ) )
           
            lista.append(filename) 

        else:
            lista.append(var)  

        if file3 and allowed_file(file3.filename ):
            filename = secure_filename(file3.filename)            
            file3.save(os.path.join(app.config['UPLOAD_FOLDER'],   filename  ) )
           
            lista.append(filename) 

        else:
            lista.append(var)      

        if file2 and allowed_file(file2.filename ):
            filename = secure_filename(file2.filename)            
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'],   filename  ) )
           
            lista.append(filename) 

        else:
            lista.append(var)


        return redirect(url_for('receber'  ))

    return render_template('index.html')
   

@app.route('/receber')
def receber():
    '''return send_from_directory(app.config["UPLOAD_FOLDER"], name   )'''
   
    return render_template('/recebr.html' , teste = lista[0] ,teste1 = lista[1], teste2 = lista[2], teste3 = lista[3], teste4 = lista[4], var = var  )







if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
    #webview.start()