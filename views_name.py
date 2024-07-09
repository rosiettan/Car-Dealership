from django.http import HttpRequest, HttpResponse


def name(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        age = request.POST.get("age", "0")
        name = request.POST.get("name", "")
        return HttpResponse(f"""
        Thank you, {name}! <br>
        You are {age} years old.
        """)

    return HttpResponse("""
    <form method="POST">
        <label for="name"> What's your name? </label>
        <input id="name" name="name" value="Bill"><br>
        <label for="name"> What's your age? </label>
        <input id="age" name="age" type="number" value="50"><br>
        <button type="submit">OK</button>
    </form>
    """)
