import pylibdmtx.pylibdmtx as dmtx
from PIL import Image
import numpy as np

def create_gs1_datamatrix(data_string, module_size=12, dpi=600):
    """
    GS1 DataMatrix 생성 - 고해상도 버전
    
    Args:
        data_string (str): GS1 데이터 문자열
        module_size (int): 각 모듈(점)의 크기 (픽셀)
        dpi (int): 출력 해상도
    """
    try:
        # FNC1을 시작 문자로 추가 (GS1)
        fnc1 = bytes([232])
        data_bytes = fnc1 + data_string.encode('ascii')
        
        # DataMatrix 생성
        encoded = dmtx.encode(data_bytes)
        
        # 기본 이미지 생성
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
        
        # 이미지를 흑백으로 변환
        img = img.convert('L')
        
        # 임계값을 사용하여 선명한 흑백 이미지로 변환
        threshold = 128
        img = img.point(lambda x: 0 if x < threshold else 255, '1')
        
        # 이미지 크기 조정 (안티앨리어싱 없이)
        if module_size != 1:
            # NumPy 배열로 변환
            img_array = np.array(img)
            
            # 각 픽셀을 module_size x module_size로 확장
            img_array = img_array.repeat(module_size, axis=0).repeat(module_size, axis=1)
            
            # 다시 이미지로 변환
            img = Image.fromarray(img_array)
        
        # 여백 추가 (흰색)
        border = module_size * 2  # 모듈 크기의 2배만큼 여백
        new_size = (img.width + border * 2, img.height + border * 2)
        new_img = Image.new('1', new_size, 255)
        new_img.paste(img, (border, border))
        
        # 최종 이미지 저장 (고해상도)
        new_img.save('gs1_datamatrix_hires.png', dpi=(dpi, dpi), quality=95)
        print(f"DataMatrix 생성 완료! (모듈 크기: {module_size}px, DPI: {dpi})")
        
        return new_img
        
    except Exception as e:
        print(f"오류 발생: {e}")
        return None

# 테스트
if __name__ == "__main__":
    # 테스트 데이터
    test_data = "01188002825303681125011421250114TLAS456401"
    
    # 여러 가지 설정으로 테스트
    # 1. 기본 고해상도 버전
    create_gs1_datamatrix(test_data, module_size=12, dpi=600)
    
    # 2. 더 큰 모듈 크기 버전
    create_gs1_datamatrix(test_data, module_size=16, dpi=600)
    
    # 3. 초고해상도 버전
    create_gs1_datamatrix(test_data, module_size=20, dpi=1200)