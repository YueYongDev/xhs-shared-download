#!/usr/bin/python3
# encoding:utf-8
import json
import os
import re

import requests
from flask import Flask, jsonify, make_response, request, send_from_directory
from flask_cors import CORS
from lxml import html

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"
    )
}

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(STATIC_DIR, filename)


@app.route("/api/images", methods=["POST"])
def img_download():
    share_url = request.json.get("shareUrl")
    if share_url:
        short_url = parse_share(share_url)
        html_content = requests.get(short_url, headers=headers).content
        tree = html.fromstring(html_content)
        title_link = tree.xpath('//*[@id="detail-title"]/text()')[0]
        img_list = tree.xpath('//meta[@name="og:image"]/@content')
        if title_link and img_list:
            data = {}
            data["code"] = 200
            data["message"] = ""
            data["data"] = img_list
            return json.dumps(data, ensure_ascii=False)


@app.route("/proxy_image")
def proxy_image():
    image_url = request.args.get("url")
    if not image_url:
        return jsonify({"code": 400, "message": "缺少图片 URL"}), 400

    response = requests.get(image_url)
    if response.status_code == 200:
        return (
            response.content,
            response.status_code,
            {"Content-Type": response.headers["Content-Type"]},
        )
    return (
        jsonify({"code": response.status_code, "message": "无法访问图片"}),
        response.status_code,
    )


@app.route("/api/download", methods=["GET"])
def download():
    try:
        img_url = request.args.get("url")
        if not img_url:
            return "URL不能为空", 400
        response = requests.get(img_url, headers=headers)
        response.raise_for_status()
        resp = make_response(response.content)
        resp.headers["Content-Type"] = "image/jpeg"
        resp.headers["Content-Disposition"] = "attachment;filename=image.jpg"
        return resp
    except Exception as e:
        return f"下载失败: {str(e)}", 500


@app.route("/api/video", methods=["POST"])
def video_dowload():
    share_url = request.get_json().get("shareUrl")
    if share_url:
        short_url = parse_share(share_url)
        html_content = requests.get(short_url).content
        tree = html.fromstring(html_content)
        video_keywords = tree.xpath('//meta[@name="keywords"]/@content')[0]
        video_link = tree.xpath('//meta[@name="og:video"]/@content')[0]
        video_time = tree.xpath('//meta[@name="og:videotime"]/@content')[0]
        if video_link and video_keywords and video_time:
            data = {}
            obj = {"keyword": video_keywords, "link": video_link, "time": video_time}
            data["code"] = 200
            data["message"] = ""
            data["data"] = obj
            return json.dumps(data, ensure_ascii=False)


def parse_share(share_text):
    pattern = r"https?://[^\s]+"
    match = re.search(pattern, share_text)
    if match:
        short_url = match.group(0).split("，")[0].strip()
        return short_url
    return None
