from pymol import cmd
import re



def afgroups(rename=False) :

	regexp = re.compile("fold_(.*)_model_([0-9]*)")
	all_objects = cmd.get_object_list("(all)")

	for object_name in all_objects :
		reresult = regexp.match(object_name)
		if reresult is None : continue
		group_name = reresult.group(1)
		model_index = reresult.group(2)

		print(f"{object_name} -> group = {group_name}, index = {model_index}")

		cmd.group(group_name, members=object_name)
		if rename :
			new_name = f"{group_name}-{model_index}"
			print(f"rename {object_name} -> {new_name}")
			cmd.set_name(object_name, new_name)




cmd.extend("afgroups", afgroups)
cmd.afgroups = afgroups
