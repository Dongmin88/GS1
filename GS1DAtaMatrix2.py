from treepoem import generate_barcode
from PIL import Image
import os


def generate_gs1_datamatrix(data):
    # 데이터 분할 (AI와 값을 분리)
    gtin = data[2:16]         # GTIN-14
    date = data[18:24]        # Date
    serial = data[26:32]      # Serial
    extra = data[32:]         # Extra data
    
    # GS1 형식으로 재구성 (괄호와 함께)
    gs1_data = f"(01){gtin}(11){date}(21){serial}{extra}"
    
    # Generate GS1 DataMatrix
    datamatrix = generate_barcode(
        barcode_type='gs1datamatrix',
        data=gs1_data,
        options={
            "parsefnc": True,  # FNC1 처리를 위한 옵션
            "format": "square",
            "version": "26x26"
        }
    )
    
    # Resize datamatrix
    dm_size_px = (120, 120)
    datamatrix = datamatrix.resize(dm_size_px, Image.NEAREST)

    # Create white background
    picture_size_px = (200, 200)
    picture = Image.new('L', picture_size_px, color='white')

    # Position the datamatrix
    barcode_position_px = (40, 40)
    picture.paste(datamatrix, barcode_position_px)

    # Save the image
    picture.save("gs1_datamatrix.png")

# 원본 데이터
raw_data = "01188002825303681125011421250114TLAS456401"

generate_gs1_datamatrix(raw_data)