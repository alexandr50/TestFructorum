import opengraph_py3


def get_content(url):
    keys = ('title', 'description', 'url', 'type', 'image')
    correct_dict = {}
    # video = opengraph_py3.OpenGraph("https://lenta.ru/news/2023/08/11/pitt_jolie_divorce/")
    content = opengraph_py3.OpenGraph(url)
    for key, value in content.items():
        if key in keys:
            correct_dict[key] = value
    return correct_dict


# print(get_content('https://lenta.ru/news/2023/08/11/pitt_jolie_divorce/'))
    # for k, v  in video.items():
    #     print(f'{k}:  {v}')
