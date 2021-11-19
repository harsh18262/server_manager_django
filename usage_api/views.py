from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from paramiko import pkey
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import paramiko
import re
import json
from dashboard.views import pass_db
import io

# Create your views here.


@api_view(["GET"])
def memusage(request):
    ssh = get_ssh(request)
    try:
        stdin, stdout, stderr = ssh.exec_command("cat /proc/meminfo| head -n 3")
        string = stdout.read().decode()
        string = string.replace("kB", "")
        string = string.replace("\n", ",")
        string = string.replace(" ", "")

        res = []
        for sub in string.split(","):
            if ":" in sub:
                res.append(map(str.strip, sub.split(":", 1)))
        res = dict(res)

        return Response(res)
    except Exception as err:
        data = str(err)
        if err:
            print(err)

        ssh.close()

    return Response("Someting went wrong")


@api_view(["GET"])
def cpuusage(request):
    ssh = get_ssh(request)
    try:
        stdin, stdout, stderr = ssh.exec_command("cat /proc/meminfo| head -n 3")
        string = stdout.read().decode()
        stdin, stdout, stderr = ssh.exec_command("ps aux --sort -%cpu,-rss")
        data = stdout.read().decode().split("\n")

        usage = [i.split(None, 10) for i in data]
        del usage[0]

        total_usage = []

        i = 0
        for element in range(len(usage) - 1):
            element = usage[i]
            usage_cpu = element[2]
            total_usage.append(usage_cpu)
            i += 1

        total_usage = sum(float(i) for i in total_usage)

        total_free = (100 * 4) - float(total_usage)  # int(get_cpus()['cpus'])

        cpu_used = {"free": total_free, "used": float(total_usage), "all": usage}

        data = cpu_used
        return Response(cpu_used)

    except Exception as err:
        data = str(err)
        if err:
            print(err)

        ssh.close()

    return Response("Someting went wrong")


def get_ssh(request):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Establishing SSH connection")
    db = pass_db()
    server = request.GET.get("server")
    entry = db.find_entries(title=server, first=True)
    key_string = entry.notes
    key_string = key_string.replace("\\n", "\n")
    key_file = io.StringIO(key_string)

    private_key = private_key_find(key_file)

    ssh.connect(
        hostname=entry.title,
        username=entry.username,
        password=entry.password,
        pkey=private_key,
    )
    print(f"Connected to the server")

    return ssh


def private_key_find(key_file):
    try:
        return paramiko.RSAKey.from_private_key(key_file)
    except:
        try:
            return paramiko.ecdsakey.ECDSAKey.from_private_key(key_file)
        except:
            try:
                return paramiko.ed25519key.Ed25519Key.from_private_key(key_file)
            except:
                return paramiko.dsskey.DSSKey.from_private_key(key_file)
