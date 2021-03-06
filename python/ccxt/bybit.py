# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.decimal_to_precision import TRUNCATE, TICK_SIZE
from ccxt.base.errors import ArgumentsRequired, SameLeverage, OrderCancelled
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidArguments
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import RequestTimeout
from ccxt.base.exchange import Exchange


class bybit(Exchange):
    def describe(self):
        return self.deep_extend(super(bybit, self).describe(), {
            "id": "bybit",
            "name": "ByBit",
            "countries": [
                "SG",
            ],
            "version": "v1",
            "rateLimit": 250,
            "certified": False,
            'timeframes': {
                '1m': '1',
                '5m': '5',
                '1h': '60',
                '3h': '180',
                '6h': '360',
                '12h': '720',
                '1d': 'D',
            },
            # new metainfo interface
            "has": {
                "fetchClosedOrders": True,
                "fetchOrderBooks": False,
                "fetchOHLCV": True,
                "fetchCurrencies": False,
                "fetchTransactions": False,
                "fetchOrder": True,
                "transferToExchange": False,
                "createDepositAddress": False,
                "cancelOrders": False,
                "fetchDepositAddress": False,
                "fetchOpenOrders": True,
                "transfer": False,
                "fetchTradingFee": False,
                "fetchOrders": True,
                "fetchLedger": False,
                "fetchTicker": True,
                "cancelAllOrders": False,
                "fetchL2OrderBook": False,
                "createLimitOrder": True,
                "createMarketOrder": True,
                "fetchBalance": True,
                "fetchWithdrawals": False,
                "fetchTradingFees": False,
                "fetchMarkets": True,
                "fetchTradingLimits": False,
                "CORS": False,
                "fetchBidsAsks": False,
                "fetchOrderBook": True,
                "createOrder": True,
                "fetchDeposits": False,
                "deposit": False,
                "withdraw": False,
                "fetchTickers": True,
                "cancelOrder": True,
                "fetchMyTrades": False,
                "fetchDepositAddresses": False,
            },
            "hostname": "bybit.com",
            "urls": {
                "logo": "https://boaexchange.com/4cdef72eb47d4a759d2c72e619f48827.png",
                "api": {
                    "v1": "https://api.{hostname}",
                },
                "www": "https://www.bybit.com",
                "doc": [
                ],
                "fees": [
                ],
            },
            "api": {
                "public": {
                    "get": [
                        "v2/public/tickers",
                        "v2/public/orderBook/L2",
                        "v2/public/symbols",
                        "v2/public/kline/list"
                    ]
                },
                "private": {
                    "get": [
                        "open-api/order/list",
                        "open-api/stop-order/list",
                        "open-api/wallet/fund/records",
                        "user/leverage",
                        "position/list",
                        "open-api/funding/prev-funding-rate",
                        "open-api/funding/prev-funding",
                        "open-api/funding/predicted-funding",
                        "v2/private/execution/list",
                    ],
                    "post": [
                        "open-api/order/create",
                        "open-api/order/cancel",
                        "open-api/stop-order/create",
                        "open-api/stop-order/cancel",
                        "user/leverage/save",
                        "position/change-position-margin",
                    ],
                }
            },
            "requiredCredentials": {
                "secret": True,
                "apiKey": True,
            },
            "fees": {
                "trading": {
                    "tierBased": False,
                    "percentage": False,
                    "maker": 0.00025,
                    "taker": 0.00075,
                },
                "funding": {
                    "tierBased": False,
                    "percentage": False,
                    "withdraw": {
                    },
                    "deposit": {
                    },
                },
            },
            "exceptions": {
                10002: RequestTimeout,
                10003: AuthenticationError,
                10004: AuthenticationError,
                10005: PermissionDenied,
                10006: DDoSProtection,
                10007: PermissionDenied,
                20001: OrderNotFound,
                20003: ArgumentsRequired,
                20004: InvalidArguments,
                20005: ArgumentsRequired,
                20006: InvalidArguments,
                20007: ArgumentsRequired,
                20008: InvalidArguments,
                20009: ArgumentsRequired,
                20010: InvalidArguments,
                20011: InvalidArguments,
                20012: InvalidArguments,
                20013: ArgumentsRequired,
                20014: InvalidArguments,
                20015: ArgumentsRequired,
                20016: InvalidArguments,
                20017: ArgumentsRequired,
                20018: InvalidArguments,
                20019: ArgumentsRequired,
                20020: ArgumentsRequired,
                20021: ArgumentsRequired,
                20022: ArgumentsRequired,
                20023: InvalidArguments,
                20031: InvalidArguments,
                20070: ArgumentsRequired,
                20071: InvalidArguments,
                30001: InvalidArguments,
                30002: InvalidOrder,
                30003: InvalidArguments,
                30004: InvalidArguments,
                30005: InvalidArguments,
                30006: ArgumentsRequired,
                30007: InvalidArguments,
                30008: InvalidArguments,
                30009: InvalidArguments,
                30010: InsufficientFunds,
                30011: InvalidOrder,
                30012: InvalidOrder,
                30013: InvalidOrder,
                30014: InvalidOrder,
                30015: InvalidOrder,
                30016: InvalidOrder,
                30017: InvalidOrder,
                30018: InvalidOrder,
                30019: InvalidOrder,
                30020: InvalidOrder,
                30021: InsufficientFunds,
                30022: InvalidOrder,
                30023: InvalidOrder,
                30024: InvalidOrder,
                30025: InvalidOrder,
                30027: InvalidOrder,
                30028: InvalidOrder,
                30029: InvalidOrder,
                30030: InvalidOrder,
                30031: InsufficientFunds,
                30032: OrderNotFound,
                30033: InvalidOrder,
                30034: OrderNotFound,
                30035: ExchangeError,
                30036: ExchangeError,
                30037: OrderCancelled,
                30040: ExchangeError,
                30041: ExchangeError,
                30042: InsufficientFunds,
                30043: ExchangeError,
                30044: ExchangeError,
                30045: ExchangeError,
                30049: InsufficientFunds,
                30050: ExchangeError,
                30051: ExchangeError,
                30052: ExchangeError,
                30054: ExchangeError,
                30057: InvalidOrder,
                30063: InvalidOrder,
                30067: InsufficientFunds,
                30068: ExchangeError,
                33004: AuthenticationError,
                34015: SameLeverage
            },
            "options": {
                # price precision by quote currency code
                "pricePrecisionByCode": {
                    "USD": 3,
                },
                "symbolSeparator": "_",
                "tag": {
                },
            },
            "precisionMode": TICK_SIZE,
            "commonCurrencies": {
            },
        })

    def cost_to_precision(self, symbol, cost):
        return int(float(self.decimal_to_precision(cost, TRUNCATE, self.markets[symbol]["precision"]["price"],
                                                   self.precisionMode)))

    def nonce(self):
        return self.milliseconds()

    def create_order(self, symbol, _type, side, amount, price=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        market = self.market(symbol)
        order = {
            "symbol": market["id"],
            "qty": self.amount_to_precision(symbol, amount),
            "side": side.capitalize(),
            "time_in_force": "GoodTillCancel",
            "order_type": _type.capitalize()
        }
        if price:
            order["price"] = self.price_to_precision(symbol, price)
        if params.get("stop_px"):
            response = self.private_post_open_api_stop_order_create(self.extend(order, params))
        else:
            response = self.private_post_open_api_order_create(self.extend(order, params))

        return self.extend(self.parse_order(response["result"], market), {"status": "open"})

    def cancel_order(self, _id, symbol=None, params=None):
        if params is None:
            params = {}
        try:
            return self.cancel_regular_order(_id, symbol, params)
        except OrderNotFound:
            return self.cancel_stop_order(_id, symbol, params)

    def cancel_regular_order(self, _id, symbol=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        request = {"order_id": _id}
        response = self.private_post_open_api_order_cancel(self.extend(request, params))
        result = response["result"]
        return self.parse_order(result)

    def cancel_stop_order(self, _id, symbol=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        market = self.market(symbol)
        request = {"stop_order_id": _id, "symbol": market['id']}
        response = self.private_post_open_api_stop_order_cancel(self.extend(request, params))
        result = response["result"]
        return self.parse_order(result)

    def parse_ohlcv(self, ohlcv, market=None, timeframe='1m', since=None, limit=None):
        timestamp = int(self.safe_string(ohlcv, 'open_time')) * 1000
        return [
            timestamp,
            self.safe_float(ohlcv, 'open'),
            self.safe_float(ohlcv, 'high'),
            self.safe_float(ohlcv, 'low'),
            self.safe_float(ohlcv, 'close'),
            self.safe_float(ohlcv, 'volume'),
        ]

    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'interval': self.timeframes[timeframe],
        }
        if limit is not None:
            request['limit'] = limit  # default 100, max 500
        # if since is not set, they will return candles starting from 2017-01-01
        if since is not None:
            if len(str(int(since))) == 13:
                since //= 1000
            request['from'] = since  # starting date filter for results
        response = self.public_get_v2_public_kline_list(self.extend(request, params))
        result = self.safe_value(response, "result")
        return self.parse_ohlcvs(result, market, timeframe, since, limit)

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request["symbol"] = market["id"]
        response = self.private_get_v2_private_execution_list(self.extend(request, params))
        result = self.safe_value(response, "result", [])
        trades = self.safe_value(result, "trades", [])
        return self.parse_trades(trades, market, since, limit)

    def parse_trade(self, trade, market=None):
        _id = self.safe_string(trade, "exec_id")
        order_id = self.safe_string(trade, "order_id")
        symbol = self.find_symbol(self.safe_string(trade, "symbol"))
        timestamp = self.safe_integer(trade, "exec_time")
        side = self.safe_string(trade, "side").lower()
        price = self.safe_float(trade, "exec_price")
        amount = self.safe_float(trade, "exec_qty")
        cost = None
        if amount and price:
            cost = round(amount / price, 8)
        fee = None
        fee_cost = self.safe_float(trade, "exec_fee")
        if fee_cost is not None:
            # fee_currency_id = self.safe_string(trade, "fee_currency")
            # fee_currency_code = self.common_currency_code(fee_currency_id)
            fee = {
                "cost": fee_cost,
                "currency": "BTC",  # fee_currency_code,
            }
        return {
            "id": _id,
            "info": trade,
            "timestamp": timestamp,
            "datetime": self.iso8601(timestamp),
            "symbol": symbol,
            "order": order_id,
            "type": None,
            "side": side,
            "takerOrMaker": None,
            "price": price,
            "amount": amount,
            "cost": cost,
            "fee": fee,
        }

    def set_leverage(self, symbol, leverage):
        self.load_markets()
        symbol = self.find_symbol(symbol)
        _id = self.market(symbol)["id"]
        return self.private_post_user_leverage_save({"symbol": _id, "leverage": leverage})

    def get_positions(self):
        self.load_markets()
        positions_to_return = list()
        positions = self.private_get_position_list()
        for position in positions["result"]:
            liq_price = self.safe_float(position, "liq_price", 0)
            size = position["size"]
            if size:
                side = position.get("side", "buy").lower()
                if side == "sell":
                    size = -size
                leverage = position["leverage"]
                margin_type = "cross" if leverage == 0 else "isolated"
                result = {"info": position, "symbol": self.find_market(position["symbol"])["symbol"],
                          "quantity": size, "leverage": leverage, "margin_type": margin_type,
                          "maintenance_margin": position["position_margin"],
                          "liquidation_price": max(liq_price, 0)}
                positions_to_return.append(result)
        return positions_to_return

    def fetch_ticker(self, symbol, params=None):
        if params is None:
            params = {}
        self.load_markets()
        market = self.market(symbol)
        _request = {
            'symbol': market['id'],
        }
        response = self.public_get_v2_public_tickers(self.extend(_request, params))
        return self.parse_ticker(response['result'][0])

    def fetch_tickers(self, symbol=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        response = self.public_get_v2_public_tickers()
        return self.parse_tickers(response['result'])

    def symbol_to_currency(self, symbol):
        symbol = self.find_symbol(symbol)
        currency = symbol.split("/")[0]
        return currency

    def fetch_balance(self, params=None):
        if params is None:
            params = {}
        self.load_markets()
        response = self.private_get_position_list()
        ret_data = response['result']
        result = {'info': ret_data}
        for position in ret_data:
            symbol = self.safe_value(position, 'symbol')
            currency_id = self.symbol_to_currency(symbol)
            code = self.safe_currency_code(currency_id)
            account = self.account()
            account['total'] = position['wallet_balance']
            account['used'] = position['position_margin'] + position['occ_closing_fee'] \
                + position['occ_funding_fee'] + position['order_margin']
            result[code] = account
        return self.parse_balance(result)

    def fetch_markets(self, params=None):
        if params is None:
            params = {}
        response = self.public_get_v2_public_symbols()
        data = self.safe_value(response, "result")
        return self.parse_markets(data)

    def fetch_orders(self, symbol=None, since=0, limit=0, params=None):
        if params is None:
            params = {}
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request["symbol"] = market["id"]
        response = self.private_get_open_api_order_list(self.extend(request, params))
        result = response["result"]
        data = result["data"] if result else list()
        orders = self.parse_orders(data, market, since, limit)
        return self.filter_by_symbol(orders, symbol)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request["symbol"] = market["id"]
        request["order_status"] = "Created,New"
        regular_response = self.private_get_open_api_order_list(self.extend(request, params))
        regular_result = regular_response["result"]
        regular_data = self.safe_value(regular_result, "data", [])
        stop_response = self.private_get_open_api_stop_order_list(self.extend(request, params))
        stop_result = stop_response["result"]
        stop_data = [order for order in self.safe_value(stop_result, "data", [])
                     if self.parse_order_status(order["stop_order_status"]) == "open"]
        data = regular_data + stop_data
        sorted_data = sorted(data, key=lambda order: -self.parse8601(order["created_at"]))
        if limit:
            sorted_data = sorted_data[:limit]
        orders = self.parse_orders(sorted_data, market, since, limit)
        orders = self.filter_by_symbol(orders, symbol)
        return orders

    def fetch_closed_orders(self, symbol=None, since=0, limit=0, params=None):
        if params is None:
            params = {}
        self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request["symbol"] = market["id"]
        request["order_status"] = "Filled,Cancelled,Rejected"
        regular_response = self.private_get_open_api_order_list(self.extend(request, params))
        regular_result = regular_response["result"]
        regular_data = regular_result["data"] if regular_result else list()
        stop_response = self.private_get_open_api_stop_order_list(self.extend(request, params))
        stop_result = stop_response["result"]
        stop_data = [order for order in (stop_result["data"] if stop_result else list())
                     if self.parse_order_status(order["stop_order_status"]) != "open"]
        data = regular_data + stop_data
        data = sorted(data, key=lambda order: -self.parse8601(order["created_at"]))[:limit or -1]
        orders = self.parse_orders(data, market, since, limit)
        orders = self.filter_by_symbol(orders, symbol)
        return orders

    def fetch_order(self, _id, symbol=None, params=None):
        if params is None:
            params = {}
        self.load_markets()
        try:
            order = self.fetch_regular_order(_id, symbol, params)
            if order["status"] == "inactive":
                return self.fetch_stop_order(_id, symbol, params)
            return order
        except OrderNotFound:
            return self.fetch_stop_order(_id, symbol, params)

    def fetch_stop_order(self, _id, symbol=None, params=None):
        if params is None:
            params = {}
        request = {"stop_order_id": _id}
        response = self.private_get_open_api_stop_order_list(self.extend(request, params))
        result = response["result"]
        if not result:
            raise OrderNotFound("Order ID wasn't found in ByBit")
        data = result.get("data")
        if not data:
            raise OrderNotFound("Order data wasn't received from ByBit")
        return self.parse_order(data[0])

    def fetch_regular_order(self, _id, symbol=None, params=None):
        if params is None:
            params = {}
        request = {"order_id": _id}
        response = self.private_get_open_api_order_list(self.extend(request, params))
        result = response["result"]
        if not result:
            raise OrderNotFound("Order ID wasn't found in ByBit")
        data = result.get("data")
        if not data:
            raise OrderNotFound("Order data wasn't received from ByBit")
        return self.parse_order(data[0])

    def parse_market(self, market):
        _id = market["name"]
        base_id = market["base_currency"]
        _base_or_quote = _id.lstrip(base_id)
        if _base_or_quote == _id:
            _quote = base_id
            _base = _id.rstrip(base_id)
        else:
            _base = base_id
            _quote = _base_or_quote
        symbol = _base + "/" + _quote
        price_filter = market["price_filter"]
        amount_filter = market["lot_size_filter"]
        return {
            "id": _id,
            "symbol": symbol,
            "base": _base,
            "quote": _quote,
            "active": True,
            "precision": {
                "amount": self.safe_float(amount_filter, "qty_step"),
                "price": self.safe_float(price_filter, "tick_size"),
            },
            "limits": {
                "amount": {
                    "min": self.safe_float(amount_filter, "min_trading_qty"),
                    "max": self.safe_float(amount_filter, "max_trading_qty")
                },
                "price": {
                    "min": self.safe_float(price_filter, "min_price"),
                    "max": self.safe_float(price_filter, "max_price")
                },
            },
            "info": market,
        }

    def parse_markets(self, markets):
        results = []
        for market in markets:
            results.append(self.parse_market(market))
        return results

    def parse_order_status(self, status):
        statuses = self.order_statuses()
        return self.safe_string(statuses, status, status)

    @staticmethod
    def order_statuses(_filter=None):
        statuses = {
            'Created': 'created',
            'New': 'open',
            'PartiallyFilled': 'open',
            'Filled': 'closed',
            'Cancelled': 'canceled',
            'Rejected': 'rejected',
            'Untriggered': 'open',
            'Triggered': 'open',
            'Active': 'open',
            'NotActive': 'inactive',
            'Deactivated': 'canceled'
        }
        return {key: value for key, value in statuses.items() if not _filter or value == _filter}

    def parse_order(self, order, market=None):
        side = self.safe_string(order, "side")
        # We parse different fields in a very specific order.
        # Order might well be closed and then canceled.
        status = self.parse_order_status(self.safe_string(order, "order_status") or
                                         self.safe_string(order, "stop_order_status"))
        market_id = self.safe_string(order, "symbol")
        if market_id:
            market = self.markets_by_id[market_id]
            symbol = market["symbol"]
        elif market:
            symbol = market["symbol"]
        else:
            raise ExchangeError("Missing symbol in the order")

        creation_datetime = order.get("created_at")
        last_trade_datetime = order.get("updated_at")
        price = self.safe_float(order, "stop_px") or self.safe_float(order, "price")
        amount = self.safe_float(order, "qty")
        cost = self.safe_float(order, "cost")
        if price:
            cost = round(amount / price, 8)
        fee = {
            "cost": order.get("cum_exec_fee"),
            "currency": symbol.split("/")[0]
        }
        remaining = self.safe_float(order, "leaves_qty") or 0.
        filled = order.get("cum_exec_qty") or 0.
        execution_cost = order.get("cum_exec_value")
        average = None
        if filled and execution_cost:
            average = filled / execution_cost
            average = float(self.price_to_precision(symbol, average))
        _type = order.get("order_type").lower()
        _id = self.safe_string(order, "stop_order_id", self.safe_string(order, "order_id"))
        _type = ("stop" if ("stop_order_id" in order) else "") + _type
        result = {
            "info": order,
            "id": _id,
            "timestamp": self.parse8601(creation_datetime),
            "datetime": creation_datetime,
            "lastTradeTimestamp": self.parse8601(last_trade_datetime),
            "symbol": symbol,
            "type": _type,
            "side": side.lower(),
            "price": price,
            "cost": cost,
            "average": average,
            "amount": amount,
            "filled": filled,
            "remaining": remaining,
            "status": status,
            "fee": fee,
        }
        return result

    def parse_symbol(self, _id):
        quote, base = _id.split(self.options["_"])
        base = self.common_currency_code(base)
        quote = self.common_currency_code(quote)
        return base + "/" + quote

    def parse_tickers(self, tickers):
        return [self.parse_ticker(ticker) for ticker in tickers]

    def parse_ticker(self, ticker, market=None):
        from datetime import datetime
        symbol = self.safe_string(ticker, "symbol")
        symbol = self.find_symbol(symbol)
        now = datetime.utcnow()
        return {
            "symbol": symbol,
            "timestamp": now.timestamp(),
            "datetime": now,
            "high": self.safe_float(ticker, "high_price_24h"),
            "low": self.safe_float(ticker, "low_price_24h"),
            "bid": self.safe_float(ticker, "bid_price"),
            "bidVolume": None,
            "ask": self.safe_float(ticker, "ask_price"),
            "askVolume": None,
            "vwap": None,
            "open": None,
            "close": self.safe_float(ticker, "last_price"),
            "last": self.safe_float(ticker, "last_price"),
            "previousClose": self.safe_float(ticker, "prev_price_24h"),
            "change": self.safe_float(ticker, "price_24h_pcnt"),
            "percentage": self.safe_float(ticker, "price_24h_pcnt"),
            "average": None,
            "baseVolume": self.safe_float(ticker, "total_volume"),
            "quoteVolume": self.safe_float(ticker, "volume_24h"),
            "info": ticker,
        }

    def sign(self, path, api="public", method="GET", params=None, headers=None, body=None):
        if params is None:
            params = {}
        body = body or ""
        url = self.urls["api"]["v1"].format(hostname=self.hostname) + "/" + path
        if api == "public":
            if params:
                url += "?" + self.urlencode(params)
        else:
            self.check_required_credentials()
            timestamp = str(self.nonce())
            params["timestamp"] = timestamp
            params["api_key"] = self.apiKey
            params = self.keysort(params)
            url_params = "&".join(["%s=%s" % (key, value) for key, value in params.items()])
            signature = self.hmac(self.encode(url_params), self.encode(self.secret))
            url += "?"
            encoded_url_params = self.urlencode(params)
            encoded_url_params += "&sign=%s" % signature
            if method == "GET":
                url += encoded_url_params
            elif method == "POST":
                body = encoded_url_params

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
            }
            if self.partner_name:
                headers["Referer"] = self.partner_name
        return {"url": url, "method": method, "body": body, "headers": headers}

    def handle_errors(self, code, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if type(response) is dict:
            data = self.safe_value(response, "result")
            return_code = self.safe_value(response, "ret_code")
            return_message = self.safe_value(response, "ret_msg")
            return_message = return_message.lower() if return_message else return_message
            feedback = self.id + " " + self.json(response)
            if "order not exists" in return_message:
                raise OrderNotFound(feedback)
            if "unknown order_status" in return_message:
                if "untriggered" in return_message:
                    raise OrderNotFound(feedback)
                else:
                    raise OrderCancelled(feedback)
            if "api key has expired" in return_message:
                raise AuthenticationError(feedback)
            if return_code:
                if return_code in self.exceptions:
                    raise self.exceptions[return_code](feedback)
                raise ExchangeError(self.id + " an error occoured: " + self.json(response))
            if data is None:
                raise ExchangeError(self.id + ": malformed response: " + self.json(response))

    def request(self, path, api="", method="GET", params=None, headers=None, body=None):
        if params is None:
            params = {}
        response = self.fetch2(path, api, method, params, headers, body)
        return response
