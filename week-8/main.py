import argparse
from PIL import Image

def main(args):
    print(args.input_path)


    image = Image.open(args.input_path)
    image.convert("RGB")
    
    (width, height) = image.size
    pixels = image.load()
    print(f"Image Size: width={width}, height={height}")

    sorted_image = Image.new("RGB", (width, height))
    sorted_pixels = sorted_image.load()


    for y in range(height):

        row = []
        for x in range(width):
            # Pixes 0-255
            pix = pixels[x, y]
            row.append(pix)

        sorted_row = sorted(row, key=lambda pix: pix[0])

        for x in range(width):
            sorted_pixels[x,y] = sorted_row[x]


    sorted_image.save("sorted_image.jpg")
    sorted_image.show()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Pixel Sorter")
    parser.add_argument("--input-path")
    

    args = parser.parse_args()

    main(args)
