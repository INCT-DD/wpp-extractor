# wpp-extractor

## A simple tool to extract WhatsApp data from rooted phones.

### Requirements:

* A rooted android phone with a SD card;
* An ADB installation;

### Initial steps:

Before running the tool your phone should be rooted and you should have it connected to your PC via USB.

Once you have the phone connected, restart the ADB server and then list your devices so you can get an 
authorization prompt on your phone:

```
$ adb kill-server
$ adb start-server
$ adb devices
```

Check the box to always allow connections from the PC you're running the tool and click "OK".

You'll have to authorize root access to the phone from the adb shell. To have it pre-authorized, please run:

```
$ adb shell
$ su -
```

This will raise an authorization prompt from your root management application. Make sure to check the box that always
allow root access to the phone and then click "OK".

Once it's authorized, you should be able to use this tool to extract the WhatsApp data from your phone.

This software tries to minimize the chances of data loss but the operation isn't risk free so make sure to backup
your data at least once before running the tool.
