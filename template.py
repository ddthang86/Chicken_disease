# Import các module cần thiết
import os
from pathlib import Path
import logging

# Cấu hình logging để hiển thị các thông báo với level INFO và định dạng thời gian và nội dung thông báo
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Tên của dự án
project_name = "cnnClassifier"

# Danh sách các đường dẫn tới các file và thư mục cần tạo hoặc kiểm tra
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Duyệt qua từng đường dẫn trong danh sách các file và thư mục
for filepath in list_of_files:
    # Chuyển đổi đường dẫn thành đối tượng Path
    filepath = Path(filepath)
    # Tách đường dẫn và tên file
    filedir, filename = os.path.split(filepath)

    # Nếu đường dẫn đến file có giá trị (không trống)
    if filedir !="":
        # Tạo thư mục nếu chưa tồn tại, nếu tồn tại thì bỏ qua (exist_ok=True)
        os.makedirs(filedir, exist_ok=True)
        # Ghi log thông báo về việc tạo thư mục cho file cụ thể
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Kiểm tra xem file có không tồn tại hoặc có kích thước bằng 0 byte
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Nếu thỏa mãn điều kiện, mở file với chế độ ghi ("w") nhưng không ghi gì cả (pass)
        with open(filepath, "w") as f:
            pass
            # Ghi log thông báo về việc tạo file rỗng
            logging.info(f"Creating empty file: {filepath}")

    else:
        # Nếu file đã tồn tại và không rỗng, ghi log thông báo
        logging.info(f"{filename} is already exists")