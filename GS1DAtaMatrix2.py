from pylibdmtx.pylibdmtx import encode
from PIL import Image
import io

# 데이터
data = "01188002825303681125011421250114TLAS456401"

# DataMatrix 코드 생성
encoded = encode(data.encode('utf-8'))

# 이미지로 변환
image = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)

# 이미지 표시 (로컬에서 실행 시)
image.show()

# 이미지 저장
image.save("GS1_DataMatrix_Code.png")
print("DataMatrix 코드가 'GS1_DataMatrix_Code.png'로 저장되었습니다.")
