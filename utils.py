import cv2
import numpy as np
from sklearn.cluster import MiniBatchKMeans

def quantizer(clusters: int, img_path: str) -> None:
    """Quantizes an image based on a colour palette that K-means creates
    and saves the quantized image on the disk

    Args:
        clusters (int): The number of the clusters i.e. the number of colours
        img_path (str): The path of the input image
    """
    # Load the image
    image = cv2.imread(img_path)
    h, w = image.shape[:2]

    # Conversion to L*a*b* gamut for perptual meaning
    image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # reshape the image into a feature vector for k-means
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # Apply K-means and create the quantized image
    clf = MiniBatchKMeans(n_clusters = clusters)
    labels = clf.fit_predict(image)
    quantized = clf.cluster_centers_.astype("uint8")[labels]

    # Reshape the feature vectors to back to images
    quantized = quantized.reshape((h, w, 3))
    image = image.reshape((h, w, 3))

    # Convert from L*a*b* to RGB
    quantized = cv2.cvtColor(quantized, cv2.COLOR_LAB2BGR, cv2.CV_8U)
    image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR, cv2.CV_8U)

    # Save the images on te disk
    cv2.imwrite(f"color_quantization_{clusters}.jpg", np.hstack([image, quantized]))
    # Display the image
    #cv2.imshow("Color Quantization Before & After", np.hstack([image, quantized]))
    #cv2.waitKey(0)