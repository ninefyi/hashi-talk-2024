import azure.functions as func
from shared_code import data_helpers

app = func.FunctionApp()

@app.function_name(name="DecryptData")
@app.route(route="decrypt", auth_level=func.AuthLevel.ANONYMOUS)
def decrypt_function(req: func.HttpRequest) -> func.HttpResponse:
    
    name = req.params.get('name')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        data = data_helpers.read_data(name)
        pass
    else:
        data = "No body"

    return func.HttpResponse(f"Hello, {data}. successfully.")

@app.function_name(name="EncryptData")
@app.route(route="encrypt", auth_level=func.AuthLevel.ANONYMOUS)
def encrypt_function(req: func.HttpRequest) -> func.HttpResponse:

    print(f"{req.params}")
    name = req.params.get('name')
    ssn = req.params.get('ssn')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if not ssn:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            ssn = req_body.get('ssn')

    print(f"{name}-{ssn}")

    if name and ssn:
        data_helpers.encrypt_data_field(name, ssn)
        pass
    else:
        name = "No body"
    
    return func.HttpResponse(f"Hello, {name}. successfully.")
