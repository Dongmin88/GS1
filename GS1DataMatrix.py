from pylibdmtx.pylibdmtx import encode
from PIL import Image
import io

def generate_and_print(data):
    # Generate datamatrix
    encoded = encode(data.encode('utf8'))
    
    # Convert to PIL Image
    datamatrix = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    
    # Resize datamatrix to desired size
    dm_size_px = (120, 120)
    datamatrix = datamatrix.resize(dm_size_px, Image.NEAREST)

    # Create white picture
    picture_size_px = (200, 200)
    picture = Image.new('RGB', picture_size_px, color='white')

    # Position the datamatrix
    barcode_position_px = (40, 40)
    picture.paste(datamatrix, barcode_position_px)

    # Save the image
    picture.save("datamatrix.png")

# GS1 데이터
gs1_data = "(01)18800282530368(17)250114(10)TLAS456401"

generate_and_print(gs1_data)