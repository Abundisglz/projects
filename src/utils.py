def to_mxn(value,rate=18.58) -> float:
    """
    This function converts
    a value from dollars to 
    maxican pesos via rate
    """
    return float(value)*float(rate)

def clean_text(text:str)->str:
    """
    This functions formats text via
    string methods 
    """
    return " ".join(text.strip().title().split())