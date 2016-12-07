import os

from novaclient import client
from novaclient import utils

from flask import Flask
from flask import render_template

app = Flask(__name__)

def get_nova_credentials_v2():
    d = {}
    d['version'] = '2'
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

credentials = get_nova_credentials_v2()
nc = client.Client(**credentials)

@app.route('/hypervisor/list')
def hypervisor_list(hypervisors=None):
    return render_template('hypervisor_list.html', hypervisors=nc.hypervisors.list()) 

@app.route('/instance/list')
def instance_list():
    return render_template('instance_list.html', instances=nc.servers.list()) 

if __name__ == '__main__':
    app.run()
