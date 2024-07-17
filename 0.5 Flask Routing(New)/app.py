from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return ('''<html>
    <p>Home page</p>
    
    
    <a href="/space1">space section</a>
    <a href="/food">Food section</a>
    <a href="/pet1">pet section</a><</html>''')

@app.route('/food')
def food():
    return ('''<html>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1xsNuMDOveR1e0l8fMUaE6X-7KgVBS4NJdQ&s"><a href="/food3">Food section num 3</a></html>''')

@app.route('/food2')
def food2():
    return('<html><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0Lj3_8eh0xYQLDhyh1pYwOF6l00mL7hIfww&s"><a href="/food2">Food section num 2</a></html>')


@app.route('/food3')
def food3():
    return ('''<html><img width="200" src="https://www.modernhoney.com/wp-content/uploads/2022/05/Double-Double-Cheeseburger-with-Fries-Recipe-scaled.jpg"><a href="/food2">food section num 2</a></html>''')

       
@app.route('/pet1')
def pet1():
    return ('''<html><img  src="https://s.puainta.com/static/uploadimages/4096567/4404bc0354bf4eaba3bdbb1820709fc9.webp"><a href="/pet2">pet section num 2</a></html>''')

@app.route('/pet2')
def pet2():
    return ('''<html><img  src="https://modernfarmer.com/wp-content/uploads/2017/12/Funny-Sheep-Facts-1200x800.jpg"><a href="/pet3">pet section num 3</a></html>''')

@app.route('/space1')
def space1():
    return ('''<html><img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Webb%27s_First_Deep_Field.jpg/1200px-Webb%27s_First_Deep_Field.jpg"><a href="/space2">space section num 2</a></html>''')


@app.route('/space2')
def space2():
    return ('''<html><img  src="https://starwalk.space/gallery/images/biggest-water-sourse-in-space/1920x1080.jpg"><a href="/space3">space section num 3</a></html>''')

 


@app.route('/space3')
def space3():
    return ('''<html><img  src="https://starwalk.space/gallery/images/what-is-space/1920x1080.jpg"></html>''')

if __name__ == '__main__':   
    app.run(debug=True)   