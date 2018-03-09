#coding:utf-8

from fabric.api import *

env.user = 'ly'
env.host = ['10.18.141.232']
env.password = 'njzyb'

@runs_once
@task
def local_update():
	with lcd('/home/ly/tmp/ProjectDjangEx'):
		local('git add -A')
		local("git commit -m 'update'")
		local('git pull origin master')
		local('git push origin master')

@task
def remote_update():
	with cd('/home/ly/tmp/ProjectDjangEx'):
		run('git checkout master')
		run('git pull origin master')

@task
def deploy():
	local_update()
	remote_update()
