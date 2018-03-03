import optparse, os, sys
"""
Argument: le path d'un dossier pour lequel on veut que tous ses sous-dossiers
          et fichiers aient des noms corrects.
          Par exemple remplacer les espaces par _

Grâce aux regedit keys qui accompagnent ce fichier,
ce script est accessible via un clic droit dans le Windows Explorer, que
ce soit sur le dossier ou à l'intérieur du dossier sur la page blanche.
"""

parser = optparse.OptionParser()
parser.add_option("-p", "--path", action="store", dest="path")
opts = parser.parse_args(sys.argv[1:])[0]


def correct_paths(dir_path):
    paths = []
    for (path, dir_names, file_names) in os.walk(dir_path):
        for d in dir_names:
            paths.append(os.path.join(path, d))
    for (path, dir_names, file_names) in os.walk(dir_path):
        for f in file_names:
            paths.append(os.path.join(path, f))
    for p in paths[::-1]:
        directory = os.path.dirname(p)
        basename = os.path.basename(p)
        new_path = os.path.join(directory, filtrer(basename))
        if not p == new_path:
            os.rename(p, new_path)




def filtrer(path):
    chars = []
    point_pos = []
    for i in range(len(path)):
        if path[i] in [" ", "(", ")", "[", "]", "<", ">"]:
            chars.append("_")
        elif path[i] in ["é", "è", "ê"]:
            chars.append("e")
        elif path[i] == "ç":
            chars.append("c")
        elif path[i] == "à":
            chars.append("a")
        elif path[i] == ".":
            point_pos.append(i)
            chars.append(".")
        else:
            chars.append(path[i])
    if len(point_pos) > 1:
        for i in point_pos[:-1]:
            chars[i] = "_"
    return ''.join(chars)

correct_paths(opts.path)
