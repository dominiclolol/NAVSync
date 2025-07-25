import sys
from core.etf_static_data import etf_dict
from core.etf_tracker import ETF_tracker
from core.websocket_client import start_websocket



def main():
    if len(sys.argv) < 2:
        raise TypeError("Usage: python main.py <ETF_SYMBOL> <optional_duration>")
    
    etf_symbol = sys.argv[1].upper()

    duration = None 
    if len(sys.argv) >= 3:
        try:
            duration = int(sys.argv[2])
        except ValueError:
            print(f"{sys.argv[2]} is not a valid integer duration. Using default (infinite) duration instead.")

    try:
        etf = etf_dict[etf_symbol]
        print(f"ETF Selected: {etf_symbol}")
        
        etf_tracker = ETF_tracker(etf)
        start_websocket(etf_tracker, duration)
    except KeyError:
        print(f"{etf_symbol} is not defined. Please choose an ETF from: {list(etf_dict.keys())}")



if __name__ == "__main__":
    main()