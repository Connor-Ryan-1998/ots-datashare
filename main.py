from flask import Flask, request, send_file
import subprocess

app = Flask(__name__)


@app.route("/share-file")
def share_file():
    file_path = "MastercardFile.enc"  # Replace with the actual file path on your system
    decrypted_file_path = (
        "MastercardFile.csv"  # Replace with the desired decrypted file path
    )
    secret = request.args.get("secret")  # Get the password from the request parameters

    # Decrypt the file using openssl command
    subprocess.run(
        [
            "openssl",
            "enc",
            "-d",
            "-aes-256-cbc",
            "-in",
            file_path,
            "-out",
            decrypted_file_path,
            "-k",
            secret,
        ]
    )

    return send_file(decrypted_file_path, as_attachment=True)


if __name__ == "__main__":
    app.run()
