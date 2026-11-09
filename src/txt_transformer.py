from utils import to_mxn,clean_text
raw = [
    {"name":"            AnA","active":True, "Cash":"1000"},
    {"name":"         CharLY","active":False, "Cash":"0.0"},
    {"name":"         ARnoLdo     ","active":True, "Cash":"99.99"},
    ]
def clean (row:dict)->dict:
    """
    recibe diccionario sin formato y lo formatea
    """
    return{
        "name":clean_text(row["name"]),
        "active":bool(row["active"]),
        "cash_mxn":to_mxn(row["cash"]),
    }
