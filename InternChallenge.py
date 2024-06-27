
#Imports
from pickle import GET
from qdrant_client.models import Distance, VectorParams, PointStruct 
import xml.etree.ElementTree as ET 
import re 
import json 
import hashlib
import os 
from typing import List
import requests 
from qdrant_client import QdrantClient, models
import pandas as pd 
from urllib.parse import urlparse
