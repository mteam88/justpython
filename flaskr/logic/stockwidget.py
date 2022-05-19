class StockWidget():
    def __init__(self, ticker):
        self.ticker = ticker
    def __repr__(self):
        return "Internal Error: Use children classes not StockWidget"

class TradingViewStockWidget(StockWidget):
    tviewtemplate = \
    '''
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container" style="height:50%;">
    <div id="tradingview_962a1"></div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.widget(
    {{
    "autosize": true,
    "symbol": "{ticker}",
    "interval": "D",
    "timezone": "Etc/UTC",
    "theme": "dark",
    "style": "1",
    "locale": "en",
    "toolbar_bg": "#f1f3f6",
    "enable_publishing": false,
    "hide_top_toolbar": true,
    "save_image": false,
    "show_popup_button": true,
    "popup_width": "1000",
    "popup_height": "650",
    "container_id": "tradingview_962a1"
    }}
    );
    </script>
    </div>
    <!-- TradingView Widget END -->
    '''    
    def __init__(self, ticker):
        super().__init__(ticker)

    def __repr__(self, width=200, height=500, **kwargs):
        return TradingViewStockWidget.tviewtemplate.format(ticker=self.ticker, **kwargs)

stockwidgets = [
    TradingViewStockWidget("NASDAQ:TSLA")
]