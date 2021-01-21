from flask import Flask, render_template
import datetime as d
import random as rd

def GetMovie():
    fileSeen=open('seen.txt','r')
    today = d.datetime.now()
    dayWeek=today.weekday()
    dayToday=str(today.year)+"/"+str(today.month)+"/"+str(today.day)
    new=True
    last_seen_day=fileSeen.read()
    if dayToday == last_seen_day or dayWeek != 0:
        #print("same week")
        fileSeen.close()
        new=False
    else:
        fileSeen.close()
        fileSeen=open('seen.txt','w')
        fileSeen.write(str(dayToday))
        #print("new week")

    getMovies=open('list.txt','r')
    listMovies=getMovies.read().splitlines()
    if new==True:
        movie=rd.choice(listMovies)
        current=open('current.txt','w')
        current.write(movie)
        listMovies.remove(movie)
    else:
        movie=open('current.txt','r').read()

    getMovies.close()
    final=''
    for i in range(len(listMovies)):
        if i < (len(listMovies)-1):
            final+=str(listMovies[i])+'\n'
        else:
            final+=str(listMovies[i])
    finalMovies=open('list.txt','w')
    finalMovies.write(final)
    return movie

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movie',methods=['POST'])
def movie():
    mov=GetMovie()
    return render_template('index.html', movie_week=mov)

if __name__=="__main__":
    app.run(debug=True)