from datetime import datetime
import subprocess
from .Server import Server


class Device:
    id = str()

    def __init__(self, device_id):
        self.id = device_id

    @staticmethod
    def check_status(device_id):
        path = Server.check()
        if path:
            command = path + f' -s {device_id} get-state'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()
            return output.decode("utf-8").rstrip()
        else:
            return 'ADB NOT FOUND'

    def kill_wpp(self):
        path = Server.check()
        if path:
            command = path + f' -s {self.id} shell am force-stop com.whatsapp'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()
            return output.decode("utf-8").rstrip()
        else:
            return 'ADB NOT FOUND'

    def start_wpp(self):
        path = Server.check()
        if path:
            command = path + f' -s {self.id} shell am start -n com.whatsapp/.HomeActivity'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()
            return output.decode("utf-8").rstrip()
        else:
            return 'ADB NOT FOUND'

    def backup_wpp(self, output_dir):
        path = Server.check()
        if path:
            timestamp = str(datetime.now().timestamp()).replace('.', '')
            extcard_path = '/storage/extSdCard/'
            dump_path = f'{extcard_path}whatsapp-dump-{timestamp}/'

            # create the dump folder
            print('Creating dump folder...')
            command = path + f' -s {self.id} shell mkdir {dump_path}'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()

            # copy the key to the dump folder
            print('Dumping cryptographic key...')
            command = path + f' -s {self.id} shell "su -c cp /data/data/com.whatsapp/files/key {dump_path}"'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()

            # copy the databases to the dump folder
            print('Dumping databases...')
            command = path + f' -s {self.id} shell "su -c cp /data/data/com.whatsapp/databases/* {dump_path}"'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()

            # change permission of the dump folder
            print('Fixing permissions of the dump directory...')
            command = path + f' -s {self.id} shell "su -c chmod 777 -R {dump_path}"'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()

            # download the dump folder
            print('Downloading the dump...')
            command = path + f' -s {self.id} pull {dump_path} {output_dir}'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()

            # remove the dump folder
            print('Removing the dump directory...')
            command = path + f' -s {self.id} shell "su -c rm -rf {dump_path}"'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            process_status = process.wait()
