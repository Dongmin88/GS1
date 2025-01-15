from pylibdmtx.pylibdmtx import decode
from PIL import Image

# 이미지 파일 열기
image_path = "GS1_DataMatrix_Code.png"
image = Image.open(image_path)

# DataMatrix 디코딩
decoded_data = decode(image)
if decoded_data:
    print("디코딩된 데이터:", decoded_data[0].data.decode('utf-8'))
else:
    print("DataMatrix를 디코딩할 수 없습니다.")
