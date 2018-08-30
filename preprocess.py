import os
import shutil


def junk_remover(
        root,
        target="labelsxml",
        source="images",
        ext='xml',
        fol="unlabelled"):
    if not (os.path.exists(os.path.join(root, fol))):
        os.mkdir(os.path.join(root, fol))
    for cat in sorted(os.listdir(os.path.join(root, source))):
        for f in sorted(os.listdir(os.path.join(root, source, cat))):
            if not os.path.exists(os.path.join(
                    root, target, cat, f[:-3] + ext)):
                if not os.path.exists(os.path.join(root, fol, cat)):
                    os.mkdir(os.path.join(root, fol, cat))
                shutil.move(
                    os.path.join(
                        root, source, cat, f), os.path.join(
                        root, fol, cat))


def renamifier(root, target):
    d = os.path.join(root, target)
    for f in os.listdir(d):
        for i in os.listdir(d + "/" + f):
            if f not in i:
                os.rename(
                    d + "/" + f + "/" + i,
                    d + "/" + f + "/" + f + "_" + i)
