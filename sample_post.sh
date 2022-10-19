#!/usr/bin/env bash
PORT=5000
echo "Port: $PORT"

echo "ADF and KPSS test on sample Time Series: [1, 2, 3, 4]"

# POST method test_stationarity
curl -d '{  
   "timeseries":[1, 2, 3, 4]
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/test_stationarity