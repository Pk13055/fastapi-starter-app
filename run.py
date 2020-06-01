#!/usr/bin/env python3
# coding: utf-8
"""
    :author: pk13055
    :brief: Sample FastAPI application
"""
from app import app


def main():
    app.run(host='0.0.0.0', port=8000, debug=True)


if __name__ == "__main__":
    main()
