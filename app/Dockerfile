# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Final Image
FROM python:3.11-slim
WORKDIR /app

# Create a non-root user
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser

# Copy only the necessary files
COPY --from=builder /root/.local /home/appuser/.local
COPY main.py .

# Update PATH for the non-root user
ENV PATH=/home/appuser/.local/bin:$PATH

USER appuser
EXPOSE 8080

CMD ["python", "main.py"]
