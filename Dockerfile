# 1. 升级基础镜像到较新的 3.11 版本
FROM python:3.11-slim
WORKDIR /app

# 2. 强制升级 pip 和 setuptools，修补扫出来的高危漏洞！
RUN pip install --no-cache-dir --upgrade pip setuptools

COPY app.py .
EXPOSE 8000
CMD ["python", "app.py"]
