# -*- python -*-
import sys
sys.path.insert(0, "/var/www/gamook")

from flask import Flask, request, app, render_template, make_response
import sys, os
import MySQLdb 
from config import * 
import json

meta = """<link rel="stylesheet" href="http://%(server_root)s/css/style.css" type="text/css" charset="utf-8">
<link type="text/css" href="http://%(server_root)s/css/ui-lightness/jquery-ui-1.8.24.custom.css" rel="Stylesheet" />	
<script type="text/javascript" src="http://%(server_root)s/js/jquery-1.8.2.min.js"></script>
<script type="text/javascript" src="http://%(server_root)s/js/jquery-ui-1.8.24.custom.min.js"></script>""" % {'server_root' : SERVER_ROOT}


app.debug = True

# create the application
application = Flask(__name__)

@application.route('/',methods=['GET'])
def play(): 
    return 'Welcome!',200

@application.errorhandler(400)
def page_not_found(e):
    return render_template('400.html',error_string = str(e)), 404

@application.errorhandler(404)
def page_not_found(e):
    return render_template('four-oh-four.html',error_string = str(e)), 404

@application.errorhandler(500)
def page_not_found(e):
    return render_template('500.html',error_string = str(e)), 404

@application.route('/new_world',methods=['GET'])
def new_world(): 
    return render_template('new-world.html',server_root=SERVER_ROOT,meta=meta), 200

@application.route('/builder',methods=['GET'])
def builder(): 
    # Need a world id
    pid = request.args.get('pid',False)
    if pid: 
        SQL = "SELECT title, content, wid FROM places WHERE pid=%s"
        db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
        cursor = db.cursor()
        cursor.execute(SQL,(pid,))
        for (title,content,wid) in cursor: 
            place = {'title' : title, 'content' : content, 'pid' : pid}
            SQL = "SELECT title, initial_state FROM worlds WHERE wid=%s"
            db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
            cursor = db.cursor()
            cursor.execute(SQL,(wid,))
            for (world_title,initial_state) in cursor: 
                world = {'title' : world_title, 'state' : initial_state, 'wid' : wid}
                return render_template('build-world.html',server_root=SERVER_ROOT,meta=meta,world=world,place=place), 200

    else:
        return 'No pid supplied',400

# Ajax only call to the POST method.
@application.route('/builder',methods=['POST'])
def init_builder(): 
    # Should be adding a new world
    title = request.form['world_name']
    state = request.form['initial_state']
    db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
    cursor = db.cursor()
    SQL = "INSERT INTO worlds (title,initial_state) VALUES (%s,%s)"
    cursor.execute(SQL,(title,state))
    wid = cursor.lastrowid
    SQL = "INSERT INTO places (title,wid) VALUES (%s,%s)"
    cursor.execute(SQL,('Starting place...',wid))
    pid = cursor.lastrowid
    db.commit()
    db.close()
    # world = {'wid' : wid, 'title' : title, 'state' : state}
    # place = {'pid' : pid, 'title' : 'Starting place...', 'content' : ''}
    return str(pid),200

@application.route('/places',methods=['GET'])
def places():
    wid = request.args.get('wid',False)
    if wid: 
        db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
        cursor = db.cursor()
        SQL = """select pid, title from places where wid=%s"""
        cursor.execute(SQL,(wid,))
        results = []
        for (pid,title) in cursor: 
            results.append({'id' : pid, 'title' : title})
        return json.dumps(results)
    else: 
        return "No known wid "+str(wid),400

@application.route('/place',methods=['POST'])
def storePlace():
    try: 
        for elt in ['title','introduction','pid']: 
            if not (elt in request.form): 
                return 'No '+elt+' supplied',400
            
        pid = int(request.form['pid'])
        title = request.form['title']
        introduction = request.form['introduction']
        db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
        cursor = db.cursor()
        if pid == -1:
            # New world!
            if not ('state' in request.form): 
                return 'No initital state specified.',400

            SQL = """insert into places (title,content) values (%s,%s)"""
            cursor.execute(SQL,(title,introduction))
            pid = cursor.lastrowid

            ## parse state, store state
        else:
            SQL= """update places set title=%s, content=%s where pid=%s"""
            cursor.execute(SQL,(title,introduction,pid))

        db.commit()
        db.close()
        return json.dumps(pid),200
    except Exception as e: 
        return "Bolloxed cuz "+str(e),500

@application.route('/worlds',methods=['POST'])
def getWorlds(): 
    db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
    cursor = db.cursor()

@application.route('/js/<path:jsfile>',methods=['GET'])
def getJS(jsfile): 
    return pathRender('/js/',jsfile,ty='application/javascript ; charset=utf-8')

@application.route('/img/<path:imgfile>',methods=['GET'])
def getIMG(imgfile): 
    suffix = (re.split('\.',imgfile))[-1]
    return pathRender('/img/',imgfile, ty=('image/'+suffix))

@application.route('/css/<path:cssfile>',methods=['GET'])
def getCSS(cssfile):
    return pathRender('/css/',cssfile,ty='text/css ; charset=utf-8')

def pathRender(subdir,fname,ty="text/plain"): 
    path = BASE_DIR + subdir + fname  
    if os.path.exists(path):
        response = make_response(open(path).read())
        response.headers["Content-Type"] = ty
        return response
        f = open(path,'rb')
        return f.read(),200
    else:
        return render_template('four-oh-four.html',error_string=path), 404

def makePlace(words,imagepath,db):
    cursor = db.cursor()
    SQL="insert into places (words,imagepath) values (%s,%s)"
    cursor.execute(SQL,(words,imagepath))
    pid = cursor.lastrowid
    db.commit()
    return pid

    
