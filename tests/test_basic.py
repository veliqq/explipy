from explipy import explain_exception

def test_key_error():
    d = {}
    try:
        x = d["missing"]
    except KeyError:
        explanation = explain_exception(print_output=False)
        assert "does not exist" in explanation

def test_index_error():
    l = []
    try:
        x = l[0]
    except IndexError:
        explanation = explain_exception(print_output=False)
        assert "out of range" in explanation
