#!/usr/bin/env python
import os
import argparse

from bbox import bbox_string, load_bboxes_csv
from tilepack_downloader import TilepackDownloader

def main():
    parser = argparse.ArgumentParser(usage="List Valhalla Tilepacks.")
    args = parser.parse_args()
    downloader = TilepackDownloader()
    downloader.list()

if __name__ == '__main__':
    main()
