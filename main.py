oped by Ahegao Devs
# (c) ahegao.ovh 2022

from flask_restful import Resource, Api, reqparse
import requests
from flask import Flask
import os
from bs4 import BeautifulSoup


# Utils Imports
import news # news parse utils
import rm
import ml




app = Flask("API AHEGAO")
api = Api(app)

class GetLastPost(Resource):
    def get(self):
        return news.lastpost()



class GetRmInfo(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        link = rm.rm_search(args['name'])
        
        return rm.rm_info(link)


class GetMangaInfoId(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        args = parser.parse_args()
        link = rm.rm_search_id(args['id'])
        
        return rm.rm_info_id(link)


# Manga Resources
api.add_resource(GetRmInfo, '/v1/manga/getInfoRM')         
api.add_resource(GetMangaInfoID, '/v1/manga/getInfo')         

# News Resources
api.add_resource(GetLastPost, '/v1/news/getLp')




# Main EndPoint
@app.route('/')
def main_ep():
    return 'Shirix API by nknodev'

@app.route('/*')
def forbidden():
    return '404! Where Are you?'