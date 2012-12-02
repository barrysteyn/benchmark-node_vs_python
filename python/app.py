from flask import Flask
app = Flask(__name__)

@app.route('/')
def IOTest(): #Will read "Lorem Ipsum" to disk, and then write it back
    lorem_ipsum = []
    
    #Read Lorem from disk
    f = open("lorem_ipsum_input.txt","r")
   
    for line in f:
        lorem_ipsum.append(line)

    f.close()

    #Write Lorem to disk
    f = open("lorem_ipsum_output.txt","w")
    for line in lorem_ipsum:
        f.write(line)

    f.close()

    return "<p1>Lorem read and written to disk</p1>"

if __name__ == '__main__':
    app.run()
