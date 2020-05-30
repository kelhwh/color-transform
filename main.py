import os
from cursesmenu import SelectionMenu
from module.preparing_paintings import cluster_paintings, load_paintings
from module.transform import transform_my_pic

artists_list = os.listdir('samples/')
bits_list = [8, 16, 32]
pic_list = os.listdir('test/')

def pick_artist():

    #artist = input('Please select one artist from the list {}: '.format(artists_list))
    artist_idx = SelectionMenu.get_selection(artists_list, 'Please select one artist from the list below:')
    #bits = input('How many bits you want the output to have?: ')
    bits_idx = SelectionMenu.get_selection([8,16,32], 'How many bits you want the output to have?')


    return artists_list[artist_idx], bits_list[bits_idx]



def get_input_pic():
    pic_list = os.listdir('test/')
    target_pic = SelectionMenu.get_selection(pic_list, 'Which picture you want to transform?')

    return target_pic


def main():

    print ('Hello! Welcome to color transform!')
    artist, bits = pick_artist()


    image_list = cluster_paintings(artist, bits)

    target_pic = 'test/{}'.format(pic_list[get_input_pic()])

    transform_my_pic(artist, target_pic,bits,image_list, output_width=300)








main()



