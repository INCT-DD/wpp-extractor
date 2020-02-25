import os.path
import subprocess
from shutil import which


class Server:
    @staticmethod
    def check():
        command_path = which('adb')
        if command_path:
            return command_path
        else:
            return False

    @staticmethod
    def kill():
        path = Server.check()
        if path:
            command = path + ' kill-server'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()
            return output, err
        else:
            return False

    @staticmethod
    def start_adb():
        path = Server.check()
        if path:
            command = path + ' start-server'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()
            return output, err
        else:
            return False
