import os, json, re
from flask import Flask, request, jsonify
app=Flask(__name__)
CATALOG=os.path.join(os.path.dirname(__file__),'catalog.json')
@app.get('/')
def home(): return jsonify(service='NovaEra DJ Audio',status='online',mode='authorized-audio-catalog')
@app.get('/health')
def health(): return jsonify(ok=True)
@app.get('/resolve')
def resolve():
    video_id=request.args.get('id','')
    if not re.fullmatch(r'[A-Za-z0-9_-]{11}',video_id): return jsonify(error='invalid_video_id'),400
    try:
        with open(CATALOG,encoding='utf-8') as f: catalog=json.load(f)
    except (OSError,ValueError): return jsonify(error='catalog_unavailable'),500
    url=catalog.get(video_id)
    if not isinstance(url,str) or not url.startswith('https://'):
        return jsonify(error='audio_not_configured_for_video',detail='Add an authorized direct audio URL to catalog.json'),404
    return jsonify(url=url)
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.getenv('PORT','10000')))
