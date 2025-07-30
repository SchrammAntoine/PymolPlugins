from pymol import cmd


def get_reference(reference) :
	all_objects = cmd.get_object_list("(all)")
	if reference in all_objects : return reference

	matching_object = cmd.get_object_list(reference)
	if len(matching_object) == 1 :
		return matching_object[0]

	if len(matching_object) >1 :
		print(f"Ambigous object for reference = {reference}")
		print(f"This could refer to :")
		for name in matching_object : print(f"\t- {name}")
		return

	if matching_object is None :
		print(f"No object found for reference = {reference}")
		return

def get_mobile_objects(others) :
	mobile_objects = cmd.get_object_list(others)
	if mobile_objects :
		return mobile_objects
	else :
		print(f"no object found matching {others}")

def malign(reference, others="*") :

	reference = get_reference(reference)
	if reference is None : return

	mobile_objects = get_mobile_objects(others)
	if mobile_objects is None : return

	for obj in mobile_objects :
		if obj == reference : continue
		print(f"Align {obj} onto {reference}")
		cmd.align(obj, reference)



cmd.extend("malign", malign)
cmd.malign = malign



# end