import os
from cursesmenu import SelectionMenu
from module.preparing_paintings import cluster_paintings, load_paintings
from module.transform import transform_my_pic

artists_list = os.listdir('samples/')
bits_list = [8, 16, 32]
pic_list = os.listdir('test/')
methods_list = ['closest', 'farthest']

def pick_artist():

    #artist = input('Please select one artist from the list {}: '.format(artists_list))
    artist_idx = SelectionMenu.get_selection(artists_list, 'Please select one artist from the list below:')
    #bits = input('How many bits you want the output to have?: ')
    bits_idx = SelectionMenu.get_selection([8,16,32], 'How many bits you want the output to have?')

    artist = artists_list[artist_idx]
    bits = bits_list[bits_idx]

    return artist, bits


def get_input_pic():
    target_idx = SelectionMenu.get_selection(pic_list, 'Which picture you want to transform?')
    target_pic = 'test/{}'.format(pic_list[target_idx])

    return target_pic

def select_method():
    method = SelectionMenu.get_selection(methods_list, 'Which picture you want to transform?')

    return methods_list[method]


def main():

    retry = 0
    while retry==0:
        print ('Hello! Welcome to color transform!')
        artist, bits = pick_artist()

        image_list = cluster_paintings(artist, bits)
        target_pic = get_input_pic()
        method = select_method()

        transform_my_pic(artist, target_pic,bits,image_list, output_width=300, method=method)

        retry = SelectionMenu.get_selection(['Yes', 'No'], 'Do you want to try another picture?')







main()



