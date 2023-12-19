import opengraph_py3


def get_content(url):
    keys = ('title', 'description', 'url', 'type', 'image')
    correct_dict = {}
    content = opengraph_py3.OpenGraph(url)
    for key, value in content.items():
        if key in keys:
            correct_dict[key] = value
    return correct_dict


