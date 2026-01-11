import sys
from prediction_service import predict

try:
    result = predict("smoke_test_data")
    print(f"Smoke Test Başarılı. Sonuç: {result}")
    sys.exit(0)
except Exception as e:
    print(f"Smoke Test Başarısız! Hata: {e}")
    sys.exit(1)