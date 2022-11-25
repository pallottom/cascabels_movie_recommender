a_dict = {'title': '10 Years (2011)', 'rating': '3'}

def convert(a_dict):
    my_dict ={}
    my_dict[a_dict["title"]]=int(a_dict["rating"])
    return my_dict


print(convert(a_dict))