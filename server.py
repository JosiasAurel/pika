
from flask import Flask, request, redirect
import secrets
from tinydb import TinyDB, Query

db = TinyDB('./urlsdb.json')

query = Query()

octo = Flask(__name__)

def gen_rand_url():
    return secrets.token_urlsafe(4)

#print(gen_rand_url())

@octo.route("/short", methods=['POST'])
def handle_short():
    data = request.get_json(force=True)
    #print(data)
    done = db.insert({'original_url':data['url'], 'short_url':gen_rand_url() })
    print(done)
    return {'url':data['url']}

#dynamic route test for short url
@octo.route("/<url>")
def handle_req(url):
    req_url = db.search(query['short_url'] == url)
    return redirect(req_url[0]['original_url'], code=302)

if __name__ == "__main__":
    octo.run(debug=True)


