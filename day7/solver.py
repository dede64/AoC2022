import re

FS_SIZE = 70000000
MIN_SPACE = 30000000

class Folder:

    def __init__(self, name):

        self.parent = None
        self.childs = {}
        self.files = {}
        self.size = 0

        self.name = name
        

    def add_child(self, child):
        if not child.name in self.childs.keys():
            self.childs[child.name] = child
            child.parent = self

    def get_size(self):
        self.size = 0
        for child in self.childs.values():
            self.size += child.get_size()
        self.size += self.get_files_size()
        
        return self.size

    def get_files_size(self):
        tmp = 0
        for fl in self.files.values():
            tmp += fl.size
        return tmp

    def add_file(self, file):
        if not file.name in self.files:
            self.files[file.name] = file

    def get_result_size(self):

        tmp = 0

        if self.size <= 100000:
            tmp += self.size

        for child in self.childs.values():
            tmp += child.get_result_size()

        return tmp

class File:

    def __init__(self, name, size):
        
        self.name = name
        self.size = size
            
def find_minimal_folder_to_delete(folder, del_min, smallest_size = FS_SIZE):

    tmp_size = smallest_size

    for child in folder.childs.values():
        tmp = find_minimal_folder_to_delete(child, del_min=del_min, smallest_size=tmp_size)
        if tmp >= del_min and tmp < tmp_size:
            tmp_size = tmp
    if folder.size >= del_min and folder.size < tmp_size:
        tmp_size = folder.size

    if tmp_size >= del_min and tmp_size < smallest_size:
        return tmp_size
    else:
        return smallest_size

# Load the file
input_file = open('day7/input_1.txt', 'r')
lines = input_file.readlines()


home_dir = Folder(name="/")
active_dir = home_dir

for line in lines:

    # Strip spaces at the ends.
    line = line.strip()

    # Check if line is command.
    if line[0] == '$':

        if line == "$ ls":
            continue
        
        # Get target directory to move in.
        cd_cmd = re.match(r'\$ cd ([\w\.\/]+)', line)
        if cd_cmd and len(cd_cmd.groups()) == 1:
            cd_cmd = cd_cmd.groups()

            if cd_cmd[0] == "/":
                active_dir = home_dir
            elif cd_cmd[0] == "..":
                active_dir = active_dir.parent
            else:
                active_dir = active_dir.childs[cd_cmd[0]]

    # If line is not command, it is either a file or a directory.
    else:

        folders = re.match(r'dir ([\w\.]+)', line)
        files = re.match(r'([0-9]+) ([\w\.]+)', line)

        # Folder string is matched.
        if folders and len(folders.groups()) > 0:
            folders = folders.groups()
            active_dir.add_child(child=Folder(name=folders[0]))

        # File string is matched.
        elif files and len(files.groups()) > 1:
            files = files.groups()
            active_dir.add_file(file=File(name=files[1], size=int(files[0])))

home_dir.get_size()

# Part 1
print(home_dir.get_result_size())

# Part 2
used_space = home_dir.size
available_size = FS_SIZE - used_space
del_min = MIN_SPACE - available_size
print(find_minimal_folder_to_delete(home_dir, del_min=del_min, smallest_size=FS_SIZE))
