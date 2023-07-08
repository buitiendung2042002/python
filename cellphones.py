import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL của trang web cellphones
url = 'https://www.cellphones.com.vn'

# Gửi yêu cầu GET đến trang web và lấy nội dung HTML
response = requests.get(url)
html_content = response.content

# Sử dụng BeautifulSoup để phân tích cú pháp HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Tìm các phần tử chứa thông tin về điện thoại
phone_elements = soup.find_all('div', class_='product-item')

# Danh sách để lưu trữ dữ liệu điện thoại
phone_data = []

# Lặp qua từng phần tử và trích xuất thông tin cần thiết
for phone_element in phone_elements:
    name = phone_element.find('h3', class_='product-title').text.strip()
    price = phone_element.find('span', class_='product-price').text.strip()

    # Truy cập vào trang thông tin chi tiết của điện thoại
    detail_url = phone_element.find('a')['href']
    detail_response = requests.get(detail_url)
    detail_content = detail_response.content
    detail_soup = BeautifulSoup(detail_content, 'html.parser')

    # Trích xuất thông tin chi tiết từ trang thông tin chi tiết
    detail_info = detail_soup.find('div', class_='product-detail')

    # Tạo từ điển dữ liệu cho mỗi điện thoại và thêm vào danh sách phone_data
    phone_dict = {
        'Tên': name,
        'Giá khuyến mãi': price,
        'URL': detail_url
    }
    phone_data.append(phone_dict)


def get_info_phone(data):
    output = []
    for temp in data:
        try:
            tmp_arr = []
            tmp_dict = {}
            url = temp['URL']
            name = temp['Tên']
            gia_km = temp['Giá khuyến mãi']

            tmp_arr += [name, gia_km]

            tmp_dict = {
                'pin': '',
                'cam': '',
                'chip': '',
                'display': '',
                'type_display': '',
                'sac': '',
                'storage': '',   
            }

            tmp_arr += [tmp_dict, url]
            output.append(tmp_arr)
        except Exception as e:
            return f"lỗi: {e}"
    
    return output


def data_to_csv(data):
    columns = ['Tên', 'Giá khuyến mãi', 'Thông số kỹ thuật', 'URL']
    df = pd.DataFrame(data, columns=columns)
    df.to_csv("data_phone.csv", index=False)


# Ghi dữ liệu vào file CSV
formatted_data = get_info_phone(phone_data)
data_to_csv(formatted_data)
