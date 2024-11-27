# Distributed via ansible - mit.zabbix-agent.package

import subprocess

def get_service_name(name):
    name_split = name.split()
    if name_split[0] == 'BY_SERVICE_DESCRIPTION':
        service = name_split[1]
        process = subprocess.run(
            "systemctl cat "+service+"|grep Description",
            capture_output=True, shell=True, encoding='utf8')
        description_from_systemctl = process.stdout.split('=')
        if len(description_from_systemctl)==2:
            description = description_from_systemctl[1].rstrip()
        else:
            description = "no description found"
        return description + " ("+service+")"
    else:
        return name

