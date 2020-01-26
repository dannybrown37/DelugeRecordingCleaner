import os
import glob
import xml.etree.ElementTree as ET
from shutil import copyfile


class DelugeRecordingsCleaner(object):

    def __init__(self):
        self.get_names_of_recordings_in_record_folder()
        self.traverse_folders_for_used_samples()
        self.move_unused_recordings_out_of_record_folder()

    def get_names_of_recordings_in_record_folder(self):
        self.recordings = []
        for filename in glob.glob("SAMPLES/RECORD/*.wav"):
            self.recordings += [filename.replace("\\", "/")]
        # print(self.recordings) # just for testing

    def traverse_folders_for_used_samples(self):
        self.all_used_recs = []
        for folder in ["KITS", "SONGS", "SYNTHS"]:
            for filename in glob.glob("{}/*.XML".format(folder)):
                tree = ET.parse(filename)
                root = tree.getroot()
                search_xpath = ".//*[@fileName]"
                elements = root.findall(search_xpath)
                used_files = [a.attrib["fileName"] for a in elements]
                used_recs = [a for a in used_files if "SAMPLES/RECORD/" in a]
                self.all_used_recs += used_recs
        self.all_used_files = sorted(set(self.all_used_recs))
        # print(self.all_used_files) # just for testing

    def move_unused_recordings_out_of_record_folder(self):
        move = sorted(set(self.all_used_recs) ^ set(self.recordings))
        for path in move:
            try:
                copyfile(path, path.replace("RECORD/", "UNUSED RECORDINGS/"))
            except IOError:
                os.mkdir("SAMPLES/UNUSED RECORDINGS/")
                copyfile(path, path.replace("RECORD/", "UNUSED RECORDINGS/"))
            os.remove(path)

if __name__ == "__main__":
    DelugeRecordingsCleaner()