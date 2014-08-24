 # imports
from flask import Flask, render_template, request
import json, requests, sys
# Inicialize the flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
        url = "https://api.angel.co/1/jobs.json"
        data = json.loads(requests.get(url).text)

	errors = ''
	if request.method == "GET":
		return render_template("index.html", errors=errors)
	else:
		
                key  = request.form['keyword']
		loc = request.form['location']

        if key and not loc :
                
                k = key.lower()
                count = 0 
                res= []
                for n in range(50):
                        if k in data["jobs"][n]['title'].lower() or k in data["jobs"][n]['description'].lower():
                                res.append( "job id: " + str(data["jobs"][n]['id']) + " and Job Title-> " + data["jobs"][n]['title'])
                                count = count + 1
                if count==0:
                        res.append( "No matches found for "+ k)
                        
        elif loc and not key :
                l = loc.lower()
                count = 0
                res = []
                for n in range(50):
                        for i in range(len(data["jobs"][n]['tags'])):
                                if 'LocationTag' in data["jobs"][n]['tags'][i]['tag_type']:
                                        if l in data["jobs"][n]['tags'][i]['name']:
                                                res.append( "job id: " + str(data["jobs"][n]['id']) + " and Job Title-> " + data["jobs"][n]['title'])
                                                count = count +1
                if count == 0 :
                        res.append( "No matches found for location "+ l)
                  
        elif loc and key :
	        a = key.lower()
                b = loc.lower()
                count = 0 
                res = []
                for n in range(50):
                        for i in range(len(data["jobs"][n]['tags'])):
                                if 'LocationTag' in data["jobs"][n]['tags'][i]['tag_type']:
                                        if b in data["jobs"][n]['tags'][i]['name']:
                                                if a in data["jobs"][n]['title'].lower() or a in data["jobs"][n]['description'].lower():
                                                        res.append( "job id: " + str(data["jobs"][n]['id']) + " and Job Title-> " + data["jobs"][n]['title'])
                                                        count = count + 1
                if count == 0 :
                       res.append( "No matches Found. Try another combination")
            
            
        else :
               res = []
               for n in range(50):
                       res.append( "job id: " + str(data["jobs"][n]['id']) + "and Job Title-> " + data["jobs"][n]['title'])
                   
             		
        data = {
	        'result': res,
				
			}			
        return render_template('data.html', data=data)
        return render_template('index.html', errors=errors)


if __name__ == '__main__':
	app.run()