import yfinance as yf
import time
import threading
import logging



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[logging.StreamHandler()]
)



class MessageHandler:
    def __init__(self, etf_tracker):
        self.tracker = etf_tracker

    def __call__(self, message):
        try:
            ticker = message['id']
            price = message['price']
            direction = message.get('change', 0)
            self.tracker.process_update(ticker, price)

            if direction < 0:
                arrow = "↓"
            elif direction > 0:
                arrow = "↑"
            else:
                arrow = "_"
            log_msg = f"{arrow} {ticker:<5} ${price:<8.2f} {self.tracker.etf_ticker:<5} ${self.tracker.etf_price:<8.2f} NAV   ${self.tracker.nav:.3f}"
            logging.info(log_msg)

        except KeyError as e:
            logging.warning(f"Missing key {e} in message: {message}")



def start_websocket(ETF_tracker : object, duration=None):
    """
    Start a WebSocket connection to listen for live price updates for an ETF and its components.

    Has (optional) duration time in seconds to keep the connection alive. If None, runs indefinitely (until interrupted via Ctrl+C).
    """
    message_handler = MessageHandler(ETF_tracker)

    ws = yf.WebSocket(verbose=False)
    ws.subscribe(symbols=ETF_tracker.all_tickers)

    listener_thread = threading.Thread(target=ws.listen, args=(message_handler,))
    listener_thread.daemon = True
    listener_thread.start()

    print(f"Listening{' for ' + str(duration) + ' seconds' if duration else ' indefinitely'}. Press Ctrl+C to stop.")
    try:
        if duration is not None:
            time.sleep(duration)
            print(f"{duration} seconds elapsed. Unsubscribing and closing WebSocket.")
        else:
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected. Unsubscribing and closing WebSocket.")
    finally:
        ws.unsubscribe(symbols=ETF_tracker.all_tickers)
        ws.close()

        if listener_thread.is_alive():
            listener_thread.join(timeout=5)
            if listener_thread.is_alive():
                print("Warning: Listener thread did not terminate gracefully.")

    print("Script finished.")
