import argparse
from PIL import Image

def main(args):
    print(args.input_path)

    image = Image.open(args.input_path)

    size = image.size


    print(f"Image Size: width={size[0]}, height={size[1]}")

    pixels = image.load()


    pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Pixel Sorter")
    parser.add_argument("--input-path")
    

    args = parser.parse_args()

    main(args)