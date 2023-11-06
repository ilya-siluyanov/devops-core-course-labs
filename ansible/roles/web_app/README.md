# Ansible web-app role

Unfortunately, I have `linux/arm64/v8` platform for running playbooks, so for simplicity I built an appropriate image by my own and pushed it to the registry (No complete CI/CD :/)

## Role dependencies

```bash
> ansible-playbook -i inventory/default_aws_ec2.yml -e "docker_username=$DOCKER_USERNAME docker_password=$DOCKER_PASSWORD" playbooks/dev/app_python/main.yaml 

PLAY [all] **********************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Install pip] *****************************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Install prerequisites] *******************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Add Docker GPG apt Key] ******************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Add Docker Repository] *******************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Install docker] **************************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Install docker compose plugin] ***********************************************************************************************************************************************
ok: [192.168.64.2]

TASK [web_app : Target] *********************************************************************************************************************************************************************
ok: [192.168.64.2] => {
    "web_app_full_wipe": "VARIABLE IS NOT DEFINED!"
}

TASK [web_app : docker-authorize] ***********************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [web_app : ensures "/opt/app_python" dir exists] ***************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : Template docker-compose file] ***********************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : Start service] **************************************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : Stop service] ***************************************************************************************************************************************************************
skipping: [192.168.64.2]

TASK [web_app : ensures "/opt/app_python" removed] ******************************************************************************************************************************************
skipping: [192.168.64.2]

TASK [web_app : Logout from docker] *********************************************************************************************************************************************************
skipping: [192.168.64.2]

PLAY RECAP **********************************************************************************************************************************************************************************
192.168.64.2               : ok=12   changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
```

## Tags

```bash
> ansible-playbook -i inventory/default_aws_ec2.yml -e "docker_username=$DOCKER_USERNAME docker_password=$DOCKER_PASSWORD" --tags login playbooks/dev/app_python/main.yaml

PLAY [all] **********************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [web_app : docker-authorize] ***********************************************************************************************************************************************************
ok: [192.168.64.2]

PLAY RECAP **********************************************************************************************************************************************************************************
192.168.64.2               : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

## Wipe logic

```bash
> ansible-playbook -i inventory/default_aws_ec2.yml -e "docker_username=$DOCKER_USERNAME docker_password=$DOCKER_PASSWORD web_app_full_wipe=true" playbooks/dev/app_python/main.yaml

PLAY [all] **********************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Install pip] *****************************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Install prerequisites] *******************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Add Docker GPG apt Key] ******************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Add Docker Repository] *******************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Install docker] **************************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Install docker compose plugin] ***********************************************************************************************************************************************
ok: [192.168.64.2]

TASK [web_app : Target] *********************************************************************************************************************************************************************
ok: [192.168.64.2] => {
    "web_app_full_wipe": "true"
}

TASK [web_app : docker-authorize] ***********************************************************************************************************************************************************
skipping: [192.168.64.2]

TASK [web_app : ensures "/opt/app_python" dir exists] ***************************************************************************************************************************************
skipping: [192.168.64.2]

TASK [web_app : Template docker-compose file] ***********************************************************************************************************************************************
skipping: [192.168.64.2]

TASK [web_app : Start service] **************************************************************************************************************************************************************
skipping: [192.168.64.2]

TASK [web_app : Stop service] ***************************************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : ensures "/opt/app_python" removed] ******************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : Logout from docker] *********************************************************************************************************************************************************
ok: [192.168.64.2]

PLAY RECAP **********************************************************************************************************************************************************************************
192.168.64.2               : ok=11   changed=2    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0

```

## Separate Tag for Wipe

```bash
> ansible-playbook -i inventory/default_aws_ec2.yml -e "docker_username=$DOCKER_USERNAME docker_password=$DOCKER_PASSWORD web_app_full_wipe=true" --tags wipe playbooks/dev/app_python/main.yaml

PLAY [all] **********************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [web_app : Stop service] ***************************************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : ensures "/opt/app_python" removed] ******************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : Logout from docker] *********************************************************************************************************************************************************
ok: [192.168.64.2]

PLAY RECAP **********************************************************************************************************************************************************************************
192.168.64.2               : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Docker compose

See sources

## Bonus task

### Setup

```bash
> ansible-playbook -i inventory/default_aws_ec2.yml -e "docker_username=$DOCKER_USERNAME docker_password=$DOCKER_PASSWORD" --tags app_setup playbooks/dev/app_rust/main.yaml  

PLAY [all] **********************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [web_app : docker-authorize] ***********************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [web_app : ensures "/opt/app_rust" dir exists] *****************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : Template docker-compose file] ***********************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : Start service] **************************************************************************************************************************************************************
changed: [192.168.64.2]

PLAY RECAP **********************************************************************************************************************************************************************************
192.168.64.2               : ok=5    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Wiping

```bash
> ansible-playbook -i inventory/default_aws_ec2.yml -e "docker_username=$DOCKER_USERNAME docker_password=$DOCKER_PASSWORD web_app_full_wipe=true" --tags wipe playbooks/dev/app_rust/main.yaml

PLAY [all] **********************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [192.168.64.2]

TASK [web_app : Stop service] ***************************************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : ensures "/opt/app_rust" removed] ********************************************************************************************************************************************
changed: [192.168.64.2]

TASK [web_app : Logout from docker] *********************************************************************************************************************************************************
ok: [192.168.64.2]

PLAY RECAP **********************************************************************************************************************************************************************************
192.168.64.2               : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```