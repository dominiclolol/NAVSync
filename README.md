# NAVSync - v1.0

NAVSync v1.0 is a Python tool that monitors the real-time Net Asset Value (NAV) of a specified Exchange-Traded Fund (ETF) by tracking its components using live market data via Yahoo Finance's WebSocket API. Invesco's QQQ has already been defined in this project, but the structure will support any valid user-defined ETF.

## Usage
_(Execute within the project directory.)_

To start logging data:
``` bash
python app.py <ETF_SYMBOL> <optional_duration>
```

## ⚠️ Notes for users

Ensure you have an active internet connection, live data requires WebSocket access to Yahoo Finance.

For accurate live NAV calculations, **ensure the data in ```etf_static_data.py``` is up to date!**

The scripts are designed to work with any valid ETF defined in ```etf_static_data.py```, so feel free to add any you would like to analyze! See the example of Invsco's QQQ in ```etf_static_data.py``` to see how this can be done, and what static data is required.

## ⚙️ Configuration
The logging format and level can be configured at the top of ```websocket_client.py```. By default, it prints real-time updates to the terminal using logging.INFO.

## ⚒️ Planned updates

**v1.1** Analytics & Insights: Volume analysis, liquidity metrics and real-time premium/discount monitoring to help with arbitrage detection.

## Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
```

## Disclaimer

This tool is **educational** and not intended for financial trading or professional use. It is provided as-is, without any guarantees of accuracy or reliability. Use at your own risk.