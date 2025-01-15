import segno

# 데이터
data = "01188002825303681125011421250114TLAS456401"

# GS1 DataMatrix 생성
qr = segno.make(data, micro=False)
qr.save("gs1_datamatrix.png", scale=10)
