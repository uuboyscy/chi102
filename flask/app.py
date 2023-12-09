from flask import Flask, request, jsonify
import poker as p

app = Flask(__name__)


@app.route("/test")
def index_page():
    return "<h1>Hello Flask!</h1>"


# /hello/<name>
@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}!"


@app.route("/sum_fn/<x>/<y>")
def sum_fn(x, y):
    return str(int(x) + int(y))


@app.route("/sum_fn2/<int:x>/<int:y>")
def sum_fn2(x: int, y: int) -> str:
    return str(x + y)


# [GET] /v1/get_emp/<string:dep_id>/<int:emp_id>
@app.route("/v1/get_emp/<string:dep_id>/<int:emp_id>")
def get_emp(dep_id: str, emp_id: int) -> str:
    sql = f"""
        SELECT
            emp_name
            , emp_id
            , dep_id
            , salary
        FROM emp
        WHERE emp_id = @dep_id AND emp_id = @emp_id
    """
    #connect(sql, dep_id, emp_id)
    return sql


# /hello_get?username=Allen&age=22
@app.route("/hello_get")
def hello_get() -> str:
    username = request.args.get("username")
    age = request.args.get("age")

    if not username:
        return "What is your name?"

    if not age:
        return f"Hello {username}."

    return f"Hello {username}, you are {age} years old."


@app.route("/hello_post", methods=["GET", "POST"])
def hello_post() -> str:
    result = """
        <form method="POST">
            <input name="username">
            <button>SUBMIT</button>
        </form>
    """

    request_method = request.method

    if request_method == "POST":
        username = request.form.get("username")
        result += f"""
            <h1>Hello {username} !</h1>
        """

    return result


# [GET] /poker?player=5
@app.route("/poker")
def poker() -> str:
    player = int(request.args.get("player"))
    result = p.poker(player=player)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
