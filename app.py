from flask import Flask, render_template, request
import os
import psycopg2
from dotenv import load_dotenv
from google import genai
from prompts import career_prompt
from openai import OpenAI


load_dotenv()
app = Flask(__name__)

conn=psycopg2.connect(host=os.getenv("DB_HOST"),database=os.getenv("DB_NAME"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),port=os.getenv("DB_PORT"))


#client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
def generate():
    MODEL_NAME = "llama-3.3-70b-versatile"
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": "Hello"
            }
        ]
    )

    return response.choices[0].message.content

@app.route("/")

def home():
	return render_template("index.html")
	


@app.route("/submit", methods=["POST"])

def submit():
	name=request.form["name"]
	email=request.form["email"]
	age=request.form["age"]
	course=request.form["course"]
	city=request.form["city"]
	prompt = career_prompt(name, age, course, city)
	response=generate()
		
	cur=conn.cursor()
	
	cur.execute("INSERT into students001(name,email,age,course,city,ai_reply) VALUES(%s,%s,%s,%s,%s,%s)", (name,email,age,course,city,response))

	conn.commit()
	student = {"name": name,"email": email,"age": age,"course": course,"city": city,"ai_reply": response}

	
	
	
	
	cur.close()
	#return response.text
	return render_template("career.html", student=student)
	#return response.text
	#return render_template("career.html")
	

if __name__ == "__main__":
    app.run(debug=True)