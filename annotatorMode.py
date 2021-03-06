from flask import Flask, request, jsonify
from easyRASH import app
from users import ret_url, get_static_json_file, session
from datetime import datetime
from time import strftime
import json, os


@app.route('/api/annotMode', methods=['POST'])
def annotMode():
	data=get_static_json_file("mutex.json")
	FMT= '%H:%M:%S'
	key = request.args["url"]
	role = request.args["role"]
	usr = request.args["usr"]
	flag = False	
	status = False
	for tsk in data :
		for url in tsk:
			if url==key  and (role!="Author "):
				time2=tsk[url]["time"]
				if time2 != "" and tsk[url]["mutex"]=="1" and tsk[url]["user"]!=usr :
					time1 = datetime.utcnow()
					interval=datetime.strptime(time1.strftime(FMT), FMT) - datetime.strptime(time2, FMT)
					if interval.seconds > 1800:
						flag = True
				if tsk[url]["mutex"]=="0" or flag or tsk[url]["user"]==usr:
					tsk[url]["mutex"]="1"
					tsk[url]["user"]=usr
					stamp = datetime.utcnow()
					status=True
					tsk[url]["time"]= stamp.strftime(FMT)
					with open(ret_url("mutex.json", "/json"), "w") as jfile:
						jfile.write(json.dumps(data, indent=4))
	return jsonify({'result': status})

@app.route('/api/escAnnot', methods=['POST'])
def escAnnot():
	data=get_static_json_file("mutex.json")
	key = request.args["url"]
	status=False
	for tsk in data:
		for url in tsk :
			if url==key and tsk[url]["mutex"]=="1":
				tsk[url]["mutex"]="0"
				tsk[url]["user"]=""
				tsk[url]["time"]=""
				print (data)
				with open(ret_url("mutex.json", "/json"), "w") as jfile:
					jfile.write(json.dumps(data, indent=4))
	return jsonify({'result': status})
