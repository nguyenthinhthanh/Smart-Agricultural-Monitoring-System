# 🏡 Smart Agriculture IoT System

Hệ thống IoT thông minh cho nông nghiệp giúp giám sát môi trường, phát hiện bất thường và tự động hóa việc tưới tiêu nhằm tối ưu hóa sản xuất cây trồng.

## 🌱 Giới thiệu

Dự án **Smart Agriculture IoT System** sử dụng cảm biến môi trường và AI để thu thập, phân tích dữ liệu về môi trường nông nghiệp, giúp nông dân giám sát tình trạng cây trồng từ xa, cảnh báo các vấn đề và tự động hóa hệ thống tưới nước.

## 🚀 Chức năng chính

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
- Lên lịch tưới tự động.
- Dự đoán lượng nước cần tưới dựa trên AI và dữ liệu môi trường.

### 🔹 Phân loại trái cây
- Xác định trạng thái chín hoặc sống của trái cây bằng AI.

## 🔧 Công nghệ sử dụng

### 📡 Phần cứng
- **ESP32/STM32/Raspberry Pi**: Vi điều khiển trung tâm.
- **Cảm biến DHT11/DHT22**: Đo nhiệt độ và độ ẩm không khí.
- **Cảm biến độ ẩm đất**: Xác định độ ẩm đất.
- **Cảm biến ánh sáng LDR**: Đo cường độ ánh sáng.
- **Camera AI (ESP-EYE, Raspberry Pi Camera, OpenCV)**: Phát hiện sâu bệnh và phân loại trái cây.
- **Relay Module**: Điều khiển bơm nước tự động.

### 💻 Phần mềm
- **ESP-IDF/Arduino/STM32Cube**: Lập trình vi điều khiển.
- **MQTT/HTTP API**: Giao tiếp với server.
- **Firebase/InfluxDB**: Lưu trữ dữ liệu thời gian thực.
- **Node-RED**: Hiển thị dashboard giám sát.
- **Python + OpenCV + TensorFlow**: AI phát hiện sâu bệnh và phân loại trái cây.
- **Flutter/React Native**: Ứng dụng di động giám sát.

## 🏗 Kiến trúc hệ thống
1. **Thiết bị IoT (ESP32/STM32/Raspberry Pi)** thu thập dữ liệu từ cảm biến.
2. **Dữ liệu gửi lên server thông qua MQTT/HTTP API**.
3. **Dữ liệu được xử lý, lưu trữ và hiển thị trên dashboard/ứng dụng di động**.
4. **AI phân tích và đưa ra cảnh báo/tự động kích hoạt tưới nước**.

## 📌 Cách cài đặt

### 1️⃣ Clone repository
```sh
git clone https://github.com/your-username/smart-agriculture-iot.git
cd smart-agriculture-iot
