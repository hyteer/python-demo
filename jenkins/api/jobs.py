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

# get jobs
def show_jobs():
    jobs = server.get_jobs(folder_depth=1)
    print(jobs)
    for job in jobs:
        print('Job: ',job)

# create job
def create_job(job_name):
    server.create_job(job_name, jenkins.EMPTY_FOLDER_XML)

# build job
#server.build_job(api_job,{'SRV_NAME': 'service-order'})
#server.build_job(debug_job)

# get last build No.
last_build_number = server.get_job_info('Debug/apitest')['lastCompletedBuild']['number']
#build_info = server.get_build_info('Debug/apitest', last_build_number)
print("No:",last_build_number)
#print("Info:", build_info)
#jbs = server.get_job_info_regex('^Debug/',folder_depth=1)
#print("Jobs:",jbs)
#show_jobs()
