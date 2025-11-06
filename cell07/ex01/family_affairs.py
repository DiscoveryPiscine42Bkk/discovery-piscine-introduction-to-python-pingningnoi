def find_the_redheads(family_dict):

    redhead_filter = filter(
        lambda name: family_dict[name] == "red", 
        family_dict.keys()                      
    )
    
    return list(redhead_filter)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))