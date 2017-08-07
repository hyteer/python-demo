import jenkins

jenkins_server_url='http://jenkins.ci.snsshop.net'
jenkins_url='http://10.100.100.131:8080'
user_id='jk_test'
api_token='76547d8b7a3e3022aeb02833c2a5fcb0'
api_job = 'Debug/apitest'
debug_job = 'Debug/debug'

server=jenkins.Jenkins(jenkins_url, username=user_id, password=api_token)
print('Jenkins Version:%s'% server.get_version())
user = server.get_whoami()
print('User: %s' % user['fullName'])

def show_jobs():
    jobs = server.get_jobs(folder_depth=1)
    print(jobs)
    for job in jobs:
        print('Job: ',job)

def create_job(job_name):
    server.create_job(job_name, jenkins.EMPTY_FOLDER_XML)

#server.build_job(api_job,{'SRV_NAME': 'service-order'})
server.build_job(debug_job)
#show_jobs()

#server.build_job(job_name)