# Template Author: NhanDD <hp.duongducnhan@gmail.com>


SITE={{cookiecutter.cmk_dev_site}}
SITE_PATH=/omd/sites/${SITE}

AGENT_PATH=/usr/lib/check_mk_agent/plugins/
PLUGIN_PATH=${SITE_PATH}/local/lib/check_mk/base/plugins/agent_based
WATO_PATH=${SITE_PATH}/local/share/check_mk/web/plugins/wato
AGENT_SPECIAL_PATH=${SITE_PATH}/local/share/check_mk/agents/special
CHECKS_PATH=${SITE_PATH}/local/share/check_mk/checks
LIB_PATH=${SITE_PATH}/local/lib/nagios/plugins

CMK_RUN_HOST={{cookiecutter.cmk_dev_hostname}}

ACTIVE_CHECK_VERSION=1.0.0


# run in OMD[site]
dev-check-agent:
	cmk -d ${CMK_RUN_HOST}

# run in OMD[site]
dev-debug-agent:
	cmk --debug --checks={{cookiecutter.agent_id}} -vvn ${CMK_RUN_HOST}

# run in OMD[site]
dev-detect-plugins:
	cmk --detect-plugins={{cookiecutter.agent_id}} -vI ${CMK_RUN_HOST}


PROJECT_DIR={{cookiecutter.agent_id}}
AGENT_ID={{cookiecutter.agent_id}}

# run in plugin directory (where Makefile is)
dev-deploy-plugin:
#	agent
	sudo cp ./active_check/agent_${AGENT_ID}.py ${LIB_PATH}/agent_${AGENT_ID}.py
	sudo chmod +x ${LIB_PATH}/agent_${AGENT_ID}.py
#	agent invoker
	sudo cp ./check_invoker/agent_${AGENT_ID}.py ${CHECKS_PATH}/agent_${AGENT_ID}.py
	sudo chmod +x ${CHECKS_PATH}/agent_${AGENT_ID}.py
#	wato
	sudo cp ./wato/${AGENT_ID}_register.py ${WATO_PATH}/${AGENT_ID}_register.py

#   after copy done, MUST restart OMD, 
	sudo omd restart ${SITE}


dev-undeploy-plugin:
	sudo rm -f ${AGENT_SPECIAL_PATH}/agent_${AGENT_ID}.py
	sudo rm -f ${CHECKS_PATH}/agent_${AGENT_ID}.py
	sudo rm -f ${WATO_PATH}/${AGENT_ID}_register.py

	sudo omd restart ${SITE}


# create MKP, run in OMD[site]
# mkp config file should be at var/check_mk/packages (in OMD[site])
dev-create-mkp:
	sudo cp ./info ${SITE_PATH}/var/check_mk/packages/{{cookiecutter.agent_id}}
	sudo chown ${USER}:${USER} ${SITE_PATH}/var/check_mk/packages/{{cookiecutter.agent_id}}

dev-pack-kmp: 
	mkp package {{cookiecutter.agent_id}}
	ls -alh ${SITE_PATH}/var/check_mk/packages_local/ | grep {{cookiecutter.agent_id}}
	ls -alh ${SITE_PATH}/local/share/check_mk/enabled_packages/

dev-copy-packed-mkp:
	sudo cp ${SITE_PATH}/var/check_mk/packages_local/{AGENT_ID}-${ACTIVE_CHECK_VERSION}.mkp ${PWD}/${AGENT_ID}-${ACTIVE_CHECK_VERSION}.mkp
	sudo chown ${USER}:${USER} ${PWD}/${AGENT_ID}-${ACTIVE_CHECK_VERSION}.mkp


dev-mkp-remove:
	mkp list | grep {{cookiecutter.agent_id}}
	mkp disable {{cookiecutter.agent_id}} {{cookiecutter.mkp_version}}
	mkp remove {{cookiecutter.agent_id}} {{cookiecutter.mkp_version}}


dev-install:
	poetry install && poetry shell 

dev-run-test:
	poetry run pytest

dev-run-check:
	poetry run python run_check.py


# ---------------------------------
# bump2version
newver-patch:
	poetry run bump2version patch

newver-minor:
	poetry run bump2version minor

newver-major:
	poetry run bump2version major
# End------------------------------


# ---------------------------------
# mkp packer
mkp-pack:
	poetry run python mkp_packer.py

mkp-copy-to-site:
	sudo cp ${PWD}/${AGENT_ID}-${ACTIVE_CHECK_VERSION}.mkp ${SITE_PATH}/${AGENT_ID}-${ACTIVE_CHECK_VERSION}.mkp
# End------------------------------

#  ____             _                                  _   
# |  _ \  ___ _ __ | | ___  _   _ _ __ ___   ___ _ __ | |_ 
# | | | |/ _ \ '_ \| |/ _ \| | | | '_ ` _ \ / _ \ '_ \| __|
# | |_| |  __/ |_) | | (_) | |_| | | | | | |  __/ | | | |_ 
# |____/ \___| .__/|_|\___/ \__, |_| |_| |_|\___|_| |_|\__|
#            |_|            |___/                          
# DEPLOY using MKP instruction
# in this project directory run command
# 		$ make mkp-pack
# file mkp <plugin-id>-<verion>.mkp will be created in project directory
# then send command
#		$ make mkp-copy-to-site 
# to copy mkp file to OMD[site] at home directory
# inside OMD[site] bashshell 
# run command to add and enable plugin
#		OMD[nhanddsite]:~ mkp add ~/<plugin-id>-<verion>.mkp
#		OMD[nhanddsite]:~ mkp enable <plugin-id> <version>
# End------------------------------