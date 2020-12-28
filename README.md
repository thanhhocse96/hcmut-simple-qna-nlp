# Hệ thống xử lý ngôn ngữ tự nhiên đơn giản
## Nội dung
[Nội dung bài tập](https://drive.google.com/file/d/1sSPWcUkvci_aKBjv4-u38atOiJQGqm09/view?usp=sharing)
## 1. Một số thư viện
1. Chuyển đổi tiếng Việt có dấu thành không dấu: utils/no_accent_vietnamese được tham khảo từ đây: [vohaitrieu](https://gist.github.com/thuandt/3421905#gistcomment-2966421)

## 2. Xây dựng ngữ pháp cơ bản
### 2.1 Tập từ và Thẻ
Từ các câu trong input tạo được tập từ trong thư mục _corpus/corpus.csv_ trong đó loại từ được ký hiệu theo một số thẻ được đề xuất trong [1]:
+ N: danh từ
+ V: động từ
+ PREP: giới từ
+ ADV: trạng từ
+ P: Đại từ
+ NUM: Số từ
### 2.2 Ngữ pháp
Các luật ngữ pháp cơ bản được sử dụng [1]:
+ S -> NP VP
+ NP -> N
+ PP -> PREP N
+ VP -> V NP
+ VP -> ADV V NP

## 3. Một số thư mục và chức năng:
1. data: định nghĩa lớp chức năng của dữ liệu đầu vào
2. corpus: định nghĩa một bộ từ đơn giản của bài tập
3. utils: một số chức năng phụ trợ cho các lớp được định nghĩa trong lời giải
4. baseNLP: một số lớp nền tảng cho việc phát triển lời giải
5. input
6. output
7. models

## Tài liệu tham khảo
1. [A syntactic componentfor Vietnamese language processing](https://core.ac.uk/download/pdf/193897487.pdf), Phuong Le-Hong et al
