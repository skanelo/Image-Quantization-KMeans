import argparse
from utils import quantizer

if __name__ == "__main__":  
    # Argument parser construction
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to the input image")
    ap.add_argument("-c", "--clusters", required = True, type = int, help = "# of clusters")
    args = vars(ap.parse_args())
    
    clusters, img_path = args["clusters"], args["image"]
    quantizer(clusters, img_path)