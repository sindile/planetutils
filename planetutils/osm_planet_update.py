#!/usr/bin/env python
import argparse

import log
from planet import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('osmpath', help='Name or path to existing OSM planet file. Will be created and downloaded, if it does not exist.')
    parser.add_argument('outpath', help='Name or path to where updated output file should be placed.')
    parser.add_argument('--s3', action='store_true', help='Download using S3 client from AWS Public Datasets program. AWS credentials required.')
    parser.add_argument('--workdir', help="Osmosis replication workingDirectory.", default='.')
    parser.add_argument('--verbose', help="Verbose output", action='store_true')
    args = parser.parse_args()

    if args.verbose:
        log.set_verbose()

    if not os.path.exists(args.osmpath):
        log.info("planet does not exist; downloading")
        if args.s3:
            d = PlanetDownloaderS3(args.osmpath)
        else:
            d = PlanetDownloaderHttp(args.osmpath)
        d.download_planet()
    p = PlanetUpdaterOsmosis(args.osmpath)
    p.update_planet(args.outpath)

if __name__ == '__main__':
    main()
