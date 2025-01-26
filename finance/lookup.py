def lookup(symbol):
    symbol = symbol.upper()
    if (symbol == "AAAA"):
        return {"name": "AAAA stock", "price": 28.00, "symbol": "AAAA"}
    elif (symbol == "BBBB"):
        return {"name": "BBBB stock", "price": 14.00, "symbol": "BBBB"}
    elif (symbol == "CCCC"):
        return {"name": "CCCC stock", "price": 2000.00, "symbol": "CCCC"}
    else:
        return None
