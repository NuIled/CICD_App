from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def generate_static():
    # Create a test request context to allow `url_for` to work
    output_dir = 'deploy'

    # Create the directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a test request context to allow `url_for` to work
    with app.test_request_context():
        pages = {
            "index.html": render_template('index.html'),
        }

        # Save the rendered templates to files
        for filename, content in pages.items():
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"Generated {filepath}")

if __name__ == "__main__":
    generate_static()