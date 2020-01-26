# Deluge Recording Cleaner

Tool to move unused recordings from the SAMPLES/RECORD folder on a 
Synthstrom Deluge SD card to a separate folder called UNUSED RECORDINGS. 

It is highly recommended that you use this program on a local backup
of your SD card, confirm it did what you wanted it to do, then update
your SD card with the updated files. Please keep your backups should
anything have been inadvertently deleted that you wanted to keep.

Instructions for use:

1. Make sure you have Python 3.7 or later installed on your computer. 
   https://www.python.org/

2. Download the files from this repository. 

3. Put `clean.py` in the root folder of your Deluge backup. 
   i.e., at the same level as the KITS, SAMPLES, SONGS, and SYNTHS folders

4. Run `clean.py`.

5. A new folder was created in your SAMPLES folder titled UNUSED RECORDINGS.
   These are recordings that do not appear to be used by any kit, song, or 
   synth on your SD card. You can manually listen to these and delete as 
   desired. They are no longer in the SAMPLES/RECORD folder.

----------------------------------------------------------------------

NOTE: Files from the Deluge prior to firmware version 3 seem to cause
errors with this program as they use a multi-node XML format that 
breaks the parser the program uses. 

The problem is that the beginning of the files look like this:

```
<?xml version="1.0" encoding="UTF-8"?>
<firmwareVersion>2.1.0</firmwareVersion>
<earliestCompatibleFirmware>2.1.0</earliestCompatibleFirmware>
<sound>
    etc...
```

The fix is to move the second and third lines so that the files
look like this:

```
<?xml version="1.0" encoding="UTF-8"?>
<sound>
	<firmwareVersion>2.1.0</firmwareVersion>
	<earliestCompatibleFirmware>2.1.0</earliestCompatibleFirmware>
    etc...
```

If you have files like this, the file paths will be output after
running the program for you to make any fixes you'd like to make.
