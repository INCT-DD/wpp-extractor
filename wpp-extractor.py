import argparse
import os
from modules.Server import Server
from modules.Device import Device


def dir_path(string):
    if os.path.isdir(string):
        if os.access(string, os.W_OK):
            return string
        else:
            raise IOError(13, 'Permission denied')
    else:
        raise NotADirectoryError(string)


def main():
    parser = argparse.ArgumentParser(description='A simple tool to extract WhatsApp data from rooted phones.')
    parser.add_argument('device_id', type=str,
                        help='The device-id from where to pull the WhatsApp data.')
    parser.add_argument('output_dir', nargs='?', type=dir_path, default='./',
                        help='The path where to save the dumped data.')

    args = parser.parse_args()

    device_status = Device.check_status(args.device_id)

    if device_status == 'device':
        device = Device(args.device_id)
        print(f'Connected to device-id: {device.id}')
    elif device_status == 'ADB NOT FOUND':
        print(device_status)
        quit()
    else:
        print(f'Device unavailable.')
        quit()

    # kill WhatsApp so it doesn't touch the databases during our dump
    device.kill_wpp()
    device.backup_wpp(args.output_dir)
    device.start_wpp()


if __name__ == '__main__':
    main()
