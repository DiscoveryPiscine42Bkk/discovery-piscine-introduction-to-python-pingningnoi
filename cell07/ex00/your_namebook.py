def array_of_names(persons_dict):
    full_names_list = []
    
    for first_name, last_name in persons_dict.items():
    
        capitalized_first_name = first_name.capitalize()
        capitalized_last_name = last_name.capitalize()
        
        full_name = f"{capitalized_first_name} {capitalized_last_name}"
        
        full_names_list.append(full_name)
      
    return full_names_list

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))