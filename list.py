k = [1, 2, 3, 4]
l = [1]

n = [k, l]

for i in n:
	if len(i) > 1:
		print "len: ", len(i)
		component_type = i[0]
		component_name = i[1:len(i)]
	else:
		component_type = i[0]
		component_name = i[0]

	print i
	print "component name: ", component_name
	print "component type: ", component_type

