FROM python:3.11-alpine AS builder

WORKDIR /app

RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-alpine

RUN addgroup -g 1000 appuser && \
    adduser -D -u 1000 -G appuser appuser

WORKDIR /app

COPY --from=builder /root/.local /home/appuser/.local

COPY run.py .
COPY backend/ ./backend/
COPY templates/ ./templates/
COPY static/ ./static/

ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

CMD ["python", "run.py"]
