# -*- python -*-
#
# Author: Gavin Mendel-Gleason
# Copyright: Peer Production License (see http://p2pfoundation.net/Peer_Production_License)
# 
# The main url handler for Gamook

import sys
sys.path.insert(0, "/var/www/gamook")

from flask import Flask, request, app, render_template, make_response
import sys, os
import MySQLdb 
from config import * 
import json
import re 

import interpreter

meta = """<link rel="stylesheet" href="http://%(server_root)s/css/style.css" type="text/css" charset="utf-8">
<link type="text/css" href="http://%(server_root)s/css/ui-lightness/jquery-ui-1.8.24.custom.css" rel="Stylesheet" />	
<script type="text/javascript" src="http://%(server_root)s/js/jquery-1.8.2.min.js"></script>
<script type="text/javascript" src="http://%(server_root)s/js/jquery-ui-1.8.24.custom.min.js"></script>
<script type="text/javascript" src="http://%(server_root)s/js/gamook.js"></script>""" % {'server_root' : SERVER_ROOT}

app.debug = True

# create the application
application = Flask(__name__)

##################
# Errors 
##################

@application.errorhandler(400)
def page_not_found(e):
    return render_template('400.html',error_string = str(e)), 404

@application.errorhandler(404)
def page_not_found(e):
    return render_template('four-oh-four.html',error_string = str(e)), 404

@application.errorhandler(500)
def page_not_found(e):
    return render_template('500.html',error_string = str(e)), 404

###################
# Pages
###################

@application.route('/',methods=['GET'])
def play(): 
    return render_template('index.html',server_root=SERVER_ROOT,meta=meta),200

@application.route('/worlds',methods=['GET'])
def worlds(): 
    return render_template('worlds.html',server_root=SERVER_ROOT,meta=meta),200

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

###################
# API
###################

# Ajax only call to the POST method.
@application.route('/api/create-world',methods=['POST'])
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
    return json.dumps(pid),200

@application.route('/api/places',methods=['GET'])
def places():
    wid = request.args.get('wid',False)
    if wid: 
        db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
        cursor = db.cursor()
        SQL = """select pid, title from places where wid=%s"""
        cursor.execute(SQL,(wid,))
        results = []
        for (pid,title) in cursor: 
            results.append({'pid' : pid, 'title' : title})
        return json.dumps(results)
    else: 
        return "No known wid "+str(wid),400

@application.route('/api/place',methods=['GET'])
def place():
    pid = request.args.get('pid',False)
    if pid: 
        db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
        cursor = db.cursor()
        SQL = """select pid, title, content from places where pid=%s"""
        cursor.execute(SQL,(pid,))
        for (pid,title,content) in cursor:
            place = {'pid' : pid, 'title' : title, 'introduction' : content}
            return json.dumps(place)
    else: 
        return "No known pid "+str(pid),400


@application.route('/api/place',methods=['DELETE'])
def deletePlace():
    pid = request.form['pid']
    if pid: 
        db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
        cursor = db.cursor() 
        SQL = """delete from places where pid=%s"""
        cursor.execute(SQL,(pid,))
        return json.dumps({})
    else: 
        return "No known pid "+str(pid),400

@application.route('/api/place',methods=['POST'])
def storePlace():
    try: 
        for elt in ['title','introduction','pid','wid']: 
            if not (elt in request.form): 
                return 'No '+elt+' supplied',400
            
        pid = int(request.form['pid'])
        wid = int(request.form['wid'])
        title = request.form['title']
        introduction = request.form['introduction']
        db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
        cursor = db.cursor()
        if pid == -1:
            SQL = """insert into places (title,content,wid) values (%s,%s,%s)"""
            cursor.execute(SQL,(title,introduction,wid))
            pid = cursor.lastrowid
        else:
            SQL= """update places set title=%s, content=%s where pid=%s"""
            cursor.execute(SQL,(title,introduction,pid))

        db.commit()
        db.close()
        return json.dumps(pid),200
    except Exception as e: 
        return "Bolloxed cuz "+str(e),500

@application.route('/api/worlds',methods=['GET'])
def getWorlds(): 
    db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
    cursor = db.cursor()
    SQL = """select p.pid, w.wid, w.title 
             from worlds as w, places as p
             where w.wid = p.wid
             and p.pid in (select min(p2.pid) from places as p2 
                           where p2.wid = p.wid)"""
    cursor.execute(SQL)
    result = []
    for (pid,wid,title) in cursor: 
        result.append({'pid' : pid, 'wid' : wid, 'title' : title})
    return json.dumps(result),200

@application.route('/api/world',methods=['POST'])
def updateWorld(): 
    for elt in ['title','initial_state','wid']: 
        if not (elt in request.form): 
            return 'No '+elt+' supplied',400
            
    wid = int(request.form['wid'])
    title = request.form['title']
    initial_state = request.form['initial_state']

    db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
    cursor = db.cursor() 
    SQL = """update worlds set title=%s, initial_state=%s where wid=%s"""
    cursor.execute(SQL,(title,initial_state,wid))
    db.commit()
    db.close()

    return "ok",200

@application.route('/api/world',methods=['DELETE'])
def deleteWorld(): 
    wid = request.args.get('wid',False)
    if wid: 
        db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
        cursor = db.cursor()
        SQL = """delete from kripke 
                 where edge_id in 
                 (select edge_id from 
                   (select distinct k.edge_id from kripke as k, places as p 
                    where p.wid=%s
                    and (p.pid = k.source_id or p.pid = k.destination_id))
                  as e)""" 
        cursor.execute(SQL,(wid,))
        SQL = """delete from places where wid=%s"""
        cursor.execute(SQL,(wid,))
        SQL = """delete from worlds where wid=%s"""
        cursor.execute(SQL,(wid,))
        db.commit()
        db.close()
        return "ok",200
    else: 
        return "No known wid", 400

@application.route('/api/transitions',methods=['GET'])
def getTransitions(): 
    pid = request.args.get('pid',False)
    if (not pid): 
        return 'No pid supplied',400    
    source_id = request.args.get('pid')
    db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
    cursor = db.cursor() 
    SQL = """select title,destination_id,predicate,effects,edge_id,description
             from kripke, places 
             where source_id = %s 
             and destination_id=pid"""
    cursor.execute(SQL,(pid,))
    result = [] 
    for (destination,destination_id,predicate,effects,edge_id,description) in cursor: 
        result.append({'destination_id' : destination_id, 
                       'destination' : destination,
                       'edge_id' : edge_id,
                       'predicate' : predicate, 
                       'effects' : effects, 
                       'description' : description,
                       'source_id' : source_id})
    return json.dumps(result),200

@application.route('/api/transition',methods=['POST'])
def addTransition(): 
    for elt in ['predicate','effects','destination', 'destination_id','source_id','description']: 
        if not (elt in request.form): 
            return 'No '+elt+' supplied',400

    source_id = request.form['source_id']
    destination_id = request.form['destination_id']
    destination = request.form['destination']
    description = request.form['description']
    effects = request.form['effects']
    predicate = request.form['predicate']
    wid = request.form['wid']

    db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
    cursor = db.cursor() 
    
    if destination_id == '-1':
        (destination_name,destination_id) = getDestination(destination,wid);
    if destination_id == '-1': 
        return "No such destination "+str(destination),400

    SQL = """insert into kripke (source_id, destination_id,predicate,effects,description) VALUES (%s,%s,%s,%s,%s)"""
    cursor.execute(SQL,(source_id,destination_id,predicate,effects,description)); 
    edge_id = cursor.lastrowid 
    db.commit()
    db.close()
    return json.dumps(edge_id),200

@application.route('/api/transition',methods=['DELETE'])
def deleteTransition():
    edge_id = request.args.get('edge_id')
    if not edge_id: 
        return 'No edge_id supplied',400

    db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
    cursor = db.cursor() 
    SQL = """delete from kripke where edge_id =%s"""
    cursor.execute(SQL,(edge_id,))
    db.commit()
    db.close()
    return "ok",200

@application.route('/api/transition',methods=['PUT'])
def updateTransition(): 
    for elt in ['predicate','effects','destination', 'destination_id','source_id','wid','edge_id','description']: 
        if not (elt in request.form): 
            return 'No '+elt+' supplied',400

    edge_id = request.form['edge_id']
    source_id = request.form['source_id']
    destination_id = request.form['destination_id']
    destination = request.form['destination']
    description = request.form['description']
    effects = request.form['effects']
    predicate = request.form['predicate']
    wid = request.form['wid']
        
    if destination_id == '-1':
        (destination_name,destination_id) = getDestination(destination,wid)
    else:
        destination_name = getDestinationName(int(destination_id)) # this will error out if destination is not an integer

    if destination_id == '-1': 
        return "No such destination "+str(destination),400

    db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
    cursor = db.cursor() 
    SQL = """update kripke set predicate =%s, effects=%s, destination_id=%s, source_id=%s, description=%s where edge_id =%s"""
    cursor.execute(SQL,(predicate,effects,destination,source_id,description,edge_id))
    db.commit()
    db.close()
    # ugly to return the destination name, but convenient.
    return json.dumps((destination_name,destination_id)),200
        
@application.route('/api/transition/destination',methods=['GET'])
def destination():
    destination = request.args.get('destination',False)
    wid = request.args.get('wid',False)
    if not destination: 
        return 'No destination supplied',400
    if not wid: 
        return 'No wid supplied',400

    return json.dumps(getDestination(destination,wid))

@application.route('/api/num',methods=['GET'])
def num(): 
    n = request.args.get('num',False)
    if n:
        return n,200
    else: 
        return "0",200

###################
# Static Content
###################

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

###################
# Library functions
###################

def getDestination(destination,wid): 
    db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
    cursor = db.cursor() 

    destination_id = '-1'
    SQL = """select title,pid from places where title like %s and wid=%s"""
    cursor.execute(SQL,(destination + '%',wid))
    res = cursor.fetchone()
    if res: 
        (destination,destination_id) = res
    if destination_id == '-1': 
        conv = False
        try: 
            conv = int(destination)
        except Exception as e:
            pass

        if not conv: 
            try: 
                conv = int(float(destination))
            except Exception as e:
                pass

        if not conv: 
            try: 
                integer,rest = re.split('\.',destination)
                conv = int(integer)
            except Exception as e:
                pass

        if not conv: 
            return '-1'

        SQL = """select title,pid from places where pid = %s and wid=%s"""     
        cursor.execute(SQL,(conv,wid)) # completely evil: float . int 
        res = cursor.fetchone()
        if res:
            (destination,destination_id) = res
    return (destination,destination_id)
    
def getDestinationName(destination_id): 
    db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB)
    cursor = db.cursor() 

    SQL = """select title from places where pid=%s"""
    cursor.execute(SQL,(pid,))
    for (title,) in cursor: 
        return title
