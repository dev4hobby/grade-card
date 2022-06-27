from . import np, cv2, convert_from_bytes

def convert_bytes_as_pages(bytes, dpi=500):
    pages = convert_from_bytes(bytes, dpi)
    pages = [cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR) for page in pages]
    return pages