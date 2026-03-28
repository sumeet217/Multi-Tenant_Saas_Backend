# ---------- Base Image ----------
FROM python:3.12-slim

# ---------- Environment Variables ----------
# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Show logs instantly
ENV PYTHONUNBUFFERED=1

# ---------- Working Directory ----------
WORKDIR /app

# ---------- System Dependencies ----------
# Required for PostgreSQL + building packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# ---------- Install Python Dependencies ----------
# Copy requirements first for Docker caching
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Copy Project Files ----------
COPY . .

# ---------- Expose Port ----------
EXPOSE 8000

# ---------- Default Command ----------
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
