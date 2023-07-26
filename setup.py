# Import module setuptools, một gói hỗ trợ trong việc thiết lập và quản lý các gói Python
import setuptools

# Mở file README.md, đọc nội dung và lưu vào biến long_description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Định nghĩa biến __version__ để sử dụng trong thiết lập gói
__version__ = "0.0.0"

# Định nghĩa các biến liên quan đến thông tin dự án
REPO_NAME = "Chicken_disease"
AUTHOR_USER_NAME = "ddthang86"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "ddthang86@gmail.com"

# Cấu hình thông tin dự án với hàm setuptools.setup()
setuptools.setup(
    name=SRC_REPO,  # Tên gói (package) sẽ được sử dụng trong PyPI
    version=__version__,  # Phiên bản của gói
    author=AUTHOR_USER_NAME,  # Tác giả của gói
    author_email=AUTHOR_EMAIL,  # Địa chỉ email của tác giả
    description="A small python package for CNN app",  # Mô tả ngắn về gói
    long_description=long_description,  # Nội dung mô tả dài (lấy từ README.md)
    long_description_content="text/markdown",  # Định dạng của long_description là markdown
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # Đường dẫn đến repository trên GitHub
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },  # Các đường dẫn liên quan đến dự án khác
    package_dir={"": "src"},  # Định nghĩa thư mục gốc chứa mã nguồn (source code)
    packages=setuptools.find_packages(where="src")  # Các gói con sẽ được tìm thấy trong thư mục "src"
)
