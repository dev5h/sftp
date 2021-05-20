from flask import Flask, render_template, redirect, request

app = Flask(__name__, template_folder="ui", static_folder="static")

from src import home