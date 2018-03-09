import os
import shutil

def junk_remover(root, target="labelsxml", source="images", fol="unlabelled"):
	if not (os.path.exists(os.path.join(root, fol))):
		os.mkdir(os.path.join(root, fol))
	for cat in sorted(os.listdir(os.path.join(root,source)):
		for f in sorted(os.listdir(os.path.join(root,source,cat))):
			if not os.path.exists(os.path.join(root,target,f)):
				if not os.path.exists(os.path.join(root, fol, cat):
					os.mkdir(os.path.join(root, fol, cat))
				shutil.move(os.path.join(root, source, cat, f), os.path.join(root, fol, cat))





