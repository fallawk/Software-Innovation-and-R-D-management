#!flask/bin/python
from flask import Flask, jsonify, abort
from timeit import time

app = Flask(__name__)

sys_config = {
    #cam list must has the same length as window list
    'min_update_period': 120,
    'cam_list': [0, 1, 2, 3],   
    'window_list': [
	#canteenID: windowID
        (0, 0),
	(0, 1),
	(1, 0),
	(1, 1)       
    ]
}

now = time.time()
cached_data = {
    '0': { #canteen id
	'0' : { #window id
	    'queue_len': 10,
	    'unit_time': 5, #in seconds
	    'timestamp': now
	}
    }
}


@app.route('/')
def index():
    print("visiting index")
    return "Hello, World!"


@app.route('/query/<int:canteenID>/<int:windowID>', methods=['GET'])
def query_api_window(canteenID, windowID):
    print(canteenID, windowID)
    if canteenID >= 0 and windowID >= 0:
        if canteenID in cached_data.keys():
            if windowID in cached_data[canteenID].keys():
                now = time.time()
                if int(now - cached_data[canteenID][windowID]['timestamp']) <= sys_config['min_update_period']:
                    return cached_data[canteenID][windowID]	
    return jsonify({'data': 0})


@app.route('/query/<int:canteenID>', methods=['GET'])
def query_api_canteen(canteenID):
    print(canteenID)
    return jsonify({'data': 0})


if __name__ == '__main__':
    app.run(debug=True)
