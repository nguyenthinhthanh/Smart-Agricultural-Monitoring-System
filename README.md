# Smart Agriculture IoT System

Hệ thống IoT thông minh cho nông nghiệp giúp giám sát môi trường, phát hiện bất thường và tự động hóa việc tưới tiêu nhằm tối ưu hóa sản xuất cây trồng.

# Table of Contents

- [Giới thiệu](#giới-thiệu)
- [Chức năng chính](#chức-năng-chính)
  - [Giám sát môi trường](#-giám-sát-môi-trường)
  - [Phát hiện và cảnh báo bất thường](#-phát-hiện-và-cảnh-báo-bất-thường)
  - [Tự động hóa tưới nước](#-tự-động-hóa-tưới-nước)
  - [Phân loại trái cây](#-phân-loại-trái-cây)
- [Công nghệ sử dụng](#công-nghệ-sử-dụng)
  - [Phần cứng](#phần-cứng)
  - [Phần mềm](#phần-mềm)
- [Kiến trúc hệ thống](#kiến-trúc-hệ-thống)
- [Cách cài đặt](#cách-cài-đặt)
- [Đóng góp](#đóng-góp)
- [Giấy phép](#giấy-phép)


## Giới thiệu

Dự án **Smart Agriculture IoT System** sử dụng cảm biến môi trường và AI để thu thập, phân tích dữ liệu về môi trường nông nghiệp, giúp nông dân giám sát tình trạng cây trồng từ xa, cảnh báo các vấn đề và tự động hóa hệ thống tưới nước.

## Chức năng chính

### 🔹 Giám sát môi trường
- Đo nhiệt độ, độ ẩm không khí.
- Đo độ ẩm đất.
- Đo cường độ ánh sáng.

### 🔹 Phát hiện và cảnh báo bất thường
- Phát hiện sâu bệnh trên cây bằng AI.
- Cảnh báo khi điều kiện môi trường vượt ngưỡng nguy hiểm.

### 🔹 Tự động hóa tưới nước
- Kích hoạt tưới khi độ ẩm đất thấp.
- Tắt tưới khi đủ nước.
- Dự đoán lượng nước cần tưới dựa trên AI và dữ liệu môi trường.

### 🔹 Phân loại trái cây
- Xác định trạng thái chín hoặc sống của trái cây bằng AI.

## Công nghệ sử dụng

### Phần cứng
- **Yolobit**: Vi điều khiển.
- **Cảm biến DHT20**: Đo nhiệt độ và độ ẩm không khí.
- **Cảm biến độ ẩm đất**: Xác định độ ẩm đất.
- **Cảm biến ánh sáng LDR**: Đo cường độ ánh sáng.
- **Quạt mini**: Điều chỉnh nhiệt độ.
- **Máy bơm mini**: Bơm nước cho cây.
- **Màn hình LCD 16x2**: Hiện thị thông tin về môi trường.
- **Relay Module**: Điều khiển bơm nước tự động.

### Phần mềm
- **Ohstem app**: Lập trình yolobit.
- **Pycharm**: Hiện thực gateway (module gateway được skip).

## Kiến trúc hệ thống
1. **Thiết bị IoT (ESP32/STM32/Raspberry Pi)** thu thập dữ liệu từ cảm biến.
2. **Dữ liệu gửi lên server Adafruit IO thông qua MQTT API**.
3. **Dữ liệu được xử lý, lưu trữ và hiển thị trên dashboard/ứng dụng di động**.
4. **AI phân tích và đưa ra cảnh báo/tự động kích hoạt tưới nước**.

## Cách cài đặt

### 1️⃣ Clone repository
```sh
https://github.com/nguyenthinhthanh/Smart-Agricultural-Monitoring-System
```
### 2️⃣ Ohstem app
```sh
https://app.ohstem.vn/#!/share/yolobit/2ueZLqKiwWhT22JSFLtOwb8Sw0w  
```
## Đóng góp
Bạn có ý tưởng cải thiện trò chơi? Hãy mở Pull Request hoặc Issue trên GitHub!

## Giấy phép
Null.
