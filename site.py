from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html dir='rtl'>
    <head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
    <body style='background:linear-gradient(135deg,#0f172a,#38bdf8);color:white;text-align:center;padding:50px;font-family:sans-serif'>
        <h1>أهلاً من درنة 🌊</h1>
        <h2>موقعي الدائم اشتغل!</h2>
        <p style='background:white;color:black;padding:20px;border-radius:15px'>MA825580 - mahualdin0@gmail.com</p>
        <button onclick="alert('مبروك يا مبرمج درنة!')" style='padding:15px 30px;font-size:20px;border-radius:10px;border:none'>اضغط هنا</button>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
