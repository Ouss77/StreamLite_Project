import pickle
from pathlib import path
import streamlit_authenticator as stauth
names = ["admin"]
passwords = ["admin"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
