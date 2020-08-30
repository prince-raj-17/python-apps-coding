import os
import cat_service


def main():
    print_header()
    folder = get_or_create_output_folder()
    print('found or created folder: ' + folder)
    download_cats(folder)
    # display cat


def print_header():
    print("-------------------------------------------")
    print("              CAT FACTORY ")
    print("-------------------------------------------")


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)
    print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Creating new directory at {}".format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats....')
    cat_count = 8
    for i in range(1, cat_count+1):
        name = 'lolcat {}'.format(i)
        print('Downloading cat' + name)
        cat_service.get_cat(folder, name)

    print("Done.")





if __name__ == '__main__':
    main()
