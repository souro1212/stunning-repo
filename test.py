from flask import Flask, jsonify, request

app = Flask(__name__)


def get_some_data(company_id: str) -> []:
return []


def validate_company(company_id: str) -> bool:
# Do something to validate the request
return True


@app.route('/company/<company_id>/some_insecure_endpoint')
def some_insecure_endpoint(company_id: str):
data = get_some_data(company_id)
return jsonify(data)


@app.route('/company/<company_id>/some_other_insecure_endpoint')
def some_other_insecure_endpoint(company_id: str):
validate_company(company_id)
data = get_some_data(request.args.get('company_id'))
return jsonify(data)


@app.route('/company/<company_id>/a_secure_endpoint')
def a_secure_endpoint(company_id: str):
# other code
validate_company(company_id)
# other code
data = get_some_data(company_id)
return jsonify(data)