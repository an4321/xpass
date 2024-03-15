
run:
	uvicorn main:app --reload

user:
	uvicorn user_model:app --reload

tw:
	bunx tailwindcss -i ./static/input.css -o ./static/output.css --watch

