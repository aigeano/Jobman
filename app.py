 # imports
from flask import Flask, render_template, request
import json, requests, sys
# Inicialize the flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
        for index in range(1,255):
            res= []
            data = json.load(open("filtered.json"))
            fil = ['developer','technical','engineer','testing']

	    errors = ''
	    if request.method == "GET":
		    return render_template("index.html", errors=errors)
	    else:
		
                    key = request.form['keyword']
		    loc = request.form['location']

            if key and not loc :
                
                    k = key.lower()
                    count = 0 
                    res= []
                    for n in range(5750):
                            if k in data[n]['title'].lower() or k in data[n]['description'].lower():
                                    t =data[n]['title'].lower()
                                    if fil[0] not in t and fil[1] not in t and fil[2] not in t and fil[3] not in t :
                                            res.append( "job id: " + str(data[n]['id']) + " Job Title-> " + data[n]['title'])
                                            count = count + 1
                    if count==0:
                            res.append( "No matches found for "+ k)
                        
            elif loc and not key :
                    l = loc.lower()
                    count = 0
                    res = []
                    for n in range(5750):
                            t = data[n]['title'].lower()
                            for i in range(len(data[n]['tags'])):
                                    if 'LocationTag' in data[n]['tags'][i]['tag_type']:
                                            if l in data[n]['tags'][i]['name']:
                                                    if fil[0] not in t and fil[1] not in t and fil[2] not in t and fil[3] not in t :
                                                            res.append( "job id: " + str(data[n]['id']) + " and Job Title-> " + data[n]['title'])
                                                            count = count +1
                    if count == 0 :
                            res.append( "No matches found for location "+ l)
                  
            elif loc and key :
	            a = key.lower()
                    b = loc.lower()
                    count = 0 
                    res = []
                    for n in range(5750):
                            t = data[n]['title'].lower()
                            for i in range(len(data[n]['tags'])):
                                    if 'LocationTag' in data[n]['tags'][i]['tag_type']:
                                            if b in data[n]['tags'][i]['name']:
                                                    if a in data[n]['title'].lower() or a in data[n]['description'].lower():
                                                            if fil[0] not in t and fil[1] not in t and fil[2] not in t and fil[3] not in t :
                                                                    res.append( "job id: " + str(data[n]['id']) + " and Job Title-> " + data[n]['title'])
                                                                    count = count + 1
                    if count == 0 :
                           res.append( "No matches Found. Try another combination")
            
            
            else :
                   res = []
                   for n in range(5750):
                           t = data[n]['title'].lower()
                           if fil[0] not in t and fil[1] not in t and fil[2] not in t and fil[3] not in t :
                                   res.append( "job id: " + str(data[n]['id']) + "and Job Title-> " + data[n]['title'])
                    
             		
            data = {
	        'result': res,
				
			}			
            return render_template('data.html', data=data)
            return render_template('index.html', errors=errors)


if __name__ == '__main__':
	app.run()
