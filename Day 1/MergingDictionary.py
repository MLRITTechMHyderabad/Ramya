dict1 = {'Name': "Ramya", 'Location': "Hyd", 'Gender': "Female"}
dict2 = {'Name': "Umesh", 'Location': "Uppal", 'age': 21}

merged_dict = {}


for key in dict1:
    merged_dict[key] = dict1[key]

for key in dict2:
    if key in merged_dict:
        merged_dict[key] = [merged_dict[key], dict2[key]]
    else:
        merged_dict[key] = dict2[key]

print(merged_dict)