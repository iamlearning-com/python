# Ma trận dữ liệu và bảng tần số

Trong thực hiện nghiên cứu: 
- Dữ liệu:
     - Variables: là những đặc điểm bạn quan tâm
     - Cases: là con người, con vật, hay thứ mà bạn đang quan sát.
<br/>
<br/>
 - Cách sắp xếp và trình bày quan sát: Một cuộc thi đấu bóng rổ <br/>
 
![image](https://github.com/iamlearning-com/python/assets/154884867/01e99f53-97e8-41db-b5ee-05eb1c94ccc6)
<br/>

## Xắp xếp các quan sát thành ma trận

| Ma trận dữ liệu | Tuổi | Chiều cao | Bàn thắng | Team | Màu tóc |
| --------------- | ---- | --------- | --------- | ---- | ------- |
| Player 1 | 18 | 184 | 0 | A | Đen |
| Player 2 | 23 | 180 | 2 | B | Nâu |
| Player 3 | 19 | 178 | 5 | A | Vàng |
| Player 4 | 21 | 172 | 6 | D | Đen |
| Player 5 | 18 | 175 | 8 | C | Đen |
| ... |  |  |  |  |  |
| Player 120 | 24 | 187 | 4 | A | Đen |

Nếu các quan sát được biểu diễn bị thiếu dữ liệu, ta có thể bỏ chúng đi để sau này có thể thực hiện phân tích.
<br/>
Khi có càng nhiều dữ liệu ta không thể trình bày hết 100 hay 1000 dòng cho người liên quan thấy được. Thay vì đó ta sẽ sử dụng <b>bảng tần suất</b>.

- Bảng tần suất chỉ ra giá trị của một biến phân bố theo quan sát.

 - Công thức tính tỷ lệ:   $Tỷ lệ =  \frac{ tần suất } { tổng } * 100$


| Màu tóc | Tần suất | Tỷ lệ (%) |
| ------- | -------- | ----- |
| Đen | 70 | 58.33 |
| Nâu | 23 | 19.17 |
| Vàng | 20 | 16.67 |
| Khác | 7 | 5.83 |
| Tổng | 120 | 100 |

- Ví dụ về Bảng tần suất chỉ IQ của đội:
Khi ta lập bảng tuần xuất dạng như cân nặng, chiều cao, iq, có nhiều các giá trị khác nhau vì vậy đây không phải là một điều hay. Ta có thể gom nhóm dữ liệu và chia đều cho mỗi giá trị. <br/>

![image](https://github.com/iamlearning-com/python/assets/154884867/bfb20988-2152-4ec2-b803-5b446824b825)
