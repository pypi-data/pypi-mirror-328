import osm_bot_abstraction_layer.util_download_file
import osm_bot_abstraction_layer.tag_knowledge as tag_knowledge
import os
import os.path
import osmium
import csv
import json
import base64
import datetime
from pathlib import Path

# TODO: something to manage dates?
# to allow clearing on request?
# maybe something to get age of when file was obtained?

def download_from_geofabrik(location_code, directory_path, filename):
    """
    this will obtain Geofabrik extract
    
    location_code will be used to download data from Geofabrik
    downloaded file are from https://download.geofabrik.de/ (thanks for making this available)

    for example https://download.geofabrik.de/europe/poland/malopolskie.html would have code
    europe/poland/malopolskie
    """
    download_url = "https://download.geofabrik.de/" + location_code + "-latest.osm.pbf"
    osm_bot_abstraction_layer.util_download_file.download_file_if_not_present_already(download_url, directory_path, filename)

def create_osmium_nodecache(pbf_file_filepath, nodecache_file_filepath):
    print("building nodecache - running create_osmium_nodecache in shops package")
    # https://github.com/osmcode/pyosmium/blob/v3.7.0/examples/create_nodecache.py
    # https://github.com/osmcode/pyosmium/blob/v3.7.0/examples/use_nodecache.py
    # https://docs.osmcode.org/pyosmium/latest/intro.html#handling-geometries
    reader = osmium.io.Reader(str(pbf_file_filepath), osmium.osm.osm_entity_bits.NODE)

    idx = osmium.index.create_map("sparse_file_array," + str(nodecache_file_filepath))
    lh = osmium.NodeLocationsForWays(idx)

    osmium.apply(reader, lh)

    reader.close()
    print("building nodecache completed")

class TagImitation():
    def __init__(self, key, value):
        self.k = key
        self.v = value

class TagListImitation():
    def __init__(self, tag_dictionary):
        self.tag_dictionary = tag_dictionary

    def __iter__(self):
        self.iterator = self.tag_dictionary.__iter__()
        return self

    def __next__(self):
        key = self.iterator.__next__()
        return TagImitation(key, self.tag_dictionary[key])

    def get(self, key):
        return self.tag_dictionary.get(key)

    def __getitem__(self, index):
        return self.tag_dictionary[index]

    def __setitem__(self, index, value):
        self.tag_dictionary[index] = value

def is_shoplike_based_on_this_tag_group(taglist):
    """
    broad shop definition, vending machine qualifies as shop here

    no longer existing objects are not listed
    """
    # see https://github.com/osmcode/pyosmium/issues/263#issuecomment-2309624021
    # taglist cannot be instantiated in Python
    #
    # but converting it to taglist for all objects introduces unacceptable
    # performance overhead (roughly six times increase of time, leading to
    # processing planet in 80h making it extremely irritating)

    # give up on supporting lifecycle prefixes as attempts to do so
    # murdered performance and I have not figured out doable way
    #
    # as it was a nice-to-have not a hard requirement, lets skip it
    # 
    # hopefully it will not turn out to be needed
    """
    key_count = 0
    for entry in taglist:
        key_count += 1
    if key_count == 0:
        return False
    for prefix in tag_knowledge.typical_lifecycle_prefixes_for_past():
        deprefixed = {}
        for entry in taglist:
            key = entry.k
            if key.startswith(prefix):
                deprefixed[key.replace(prefix, "")] = taglist[key]
        if len(deprefixed) >= 1:
            return is_shoplike_based_on_this_tag_group(TagListImitation(deprefixed))
    """

    for important_main_key in ['amenity', 'shop', 'craft', 'office', 'leisure', 'healthcare']:
        if taglist.get(important_main_key) != None:
            # TODO: move upstream, release a new version of osm_bot_abstraction_layer.tag_knowledge
            # TODO: and of file downloader for that matter
            if taglist.get("office") == "yes":
                return True
            if taglist.get("shop") == "yes":
                return True
            if taglist.get("shop") == "vacant":
                return True
            # TODO reduce costs of this checks, several functions calls there are NOT needed
            # maybe cache it? build tag filter and make tag filter builder cachable?
            return tag_knowledge.is_shoplike(taglist)
    return False # no need for expensive checks

def get_way_center(way, nodeindex):
    osmium_coordinate_precision = 10_000_000
    max_lat = -90 * osmium_coordinate_precision
    max_lon = -180 * osmium_coordinate_precision
    min_lat = 90 * osmium_coordinate_precision
    min_lon = 180 * osmium_coordinate_precision
    for n in way.nodes:
        loc = nodeindex.get(n.ref) # note that cache is used here
        if max_lat < loc.y:
            max_lat = loc.y
        if min_lat > loc.y:
            min_lat = loc.y
        if max_lon < loc.x:
            max_lon = loc.x
        if min_lon > loc.x:
            min_lon = loc.x
    # Coordinates are stored as 32 bit signed integers after multiplying the coordinates 
    #with osmium::coordinate_precision = 10,000,000. This means we can store coordinates 
    # with a resolution of better than one centimeter, good enough for OSM use. 
    # The main OSM database uses the same system.
    # We do this to save memory, a 32 bit integer uses only 4 bytes, a double uses 8.
    # https://osmcode.org/libosmium/manual.html
    return ((max_lon + min_lon)/2/osmium_coordinate_precision, (max_lat + min_lat)/2/osmium_coordinate_precision)

def get_relation_center(relation, ways_location_cache):
    max_lat = -90
    max_lon = -180
    min_lat = 90
    min_lon = 180
    for member in relation.members:
        if member.type == "w":
            if member.ref in ways_location_cache:
                lon = ways_location_cache[member.ref][0]
                lat = ways_location_cache[member.ref][1]
                if max_lat < lat:
                    max_lat = lat
                if min_lat > lat:
                    min_lat = lat
                if max_lon < lon:
                    max_lon = lon
                if min_lon > lon:
                    min_lon = lon
    return ((max_lon + min_lon)/2, (max_lat + min_lat)/2)

def relation_size_limit():
    """
    exists to prevent processing crashing just because someone add bad shop tag or office tag
    to some outsized relation with thousands of elements or worse
    """
    # https://www.openstreetmap.org/relation/3321177 (possibly valid, but a poor idea at best!)
    # https://www.openstreetmap.org/note/4301459 (about seemingly invalid)
    return 200

def generate_file_with_listing_of_shoplike(pbf_file_filepath, nodecache_file_filepath, response_store_filepath, response_success_marker_filepath, is_shoplike_function):
    # based on https://github.com/osmcode/pyosmium/tree/v3.7.0/examples
    # https://docs.osmcode.org/pyosmium/latest/intro.html#collecting-data-from-an-osm-file
    # https://docs.osmcode.org/pyosmium/latest/intro.html#handling-geometries
    # https://docs.osmcode.org/pyosmium/latest/intro.html#interfacing-with-shapely
    # https://github.com/osmcode/pyosmium/blob/master/examples/use_nodecache.py
    class WaysCollectorHandler(osmium.SimpleHandler):
        """
        collect ways that are needed for building relation geometries
        """
        def __init__(self):
            super(WaysCollectorHandler, self).__init__()
            self.ways_needed_by_relations = {}
            self.relation_counter = 0

        def relation(self, o):
            if is_shoplike_function(o.tags) == False:
                return
            if o.tags.get('type') != 'multipolygon':
                return
            self.relation_counter += 1
            if len(o.members) > relation_size_limit():
                print("https://www.openstreetmap.org/relation/" + str(o.id), "relation is overly complex,", len(o.members), "members, skipping it")
                return
            for member in o.members:
                if member.type == "w":
                    self.ways_needed_by_relations[member.ref] = None

    class CollectorHandler(osmium.SimpleHandler):
        """
        collect and record shop locations
        """
        def __init__(self, idx, ways_needed_by_relations):
            """
            ways_needed_by_relations is cache of way locations, created by WaysCollectorHandler
            """
            super(CollectorHandler, self).__init__()
            self.idx = idx
            self.ways_needed_by_relations = ways_needed_by_relations
            self.ways_needed_by_relations_set_for_quick_check = set(ways_needed_by_relations)

        def node(self, o):
            if is_shoplike_function(o.tags):
                csv_shops_file_writer.writerow([o.location.lat, o.location.lon, encode_dict_to_base64(dict(o.tags)), "https://www.openstreetmap.org/node/" + str(o.id)])

        def way(self, o):
            if is_shoplike_function(o.tags):
                center = get_way_center(o, self.idx)
                csv_shops_file_writer.writerow([center[1], center[0], encode_dict_to_base64(dict(o.tags)), "https://www.openstreetmap.org/way/" + str(o.id)])
            if o.id in self.ways_needed_by_relations_set_for_quick_check:
                self.ways_needed_by_relations[o.id] = get_way_center(o, self.idx)
                #print("center of way", o.id, "calculated as requested")

        def relation(self, o):
            if is_shoplike_function(o.tags):
                if o.tags.get('type') != 'multipolygon':
                    return
                if len(o.members) > relation_size_limit():
                    print("https://www.openstreetmap.org/relation/" + str(o.id), "relation is overly complex,", len(o.members), "members, skipping it")
                center = get_relation_center(o, self.ways_needed_by_relations)
                csv_shops_file_writer.writerow([center[1], center[0], encode_dict_to_base64(dict(o.tags)), "https://www.openstreetmap.org/relation/" + str(o.id)])

    if os.path.isfile(nodecache_file_filepath) == False:
        print(datetime.datetime.now(), "nodecache generation - start, as", nodecache_file_filepath, "does not exist")
        create_osmium_nodecache(pbf_file_filepath, nodecache_file_filepath)
        print(datetime.datetime.now(), "nodecache generation - end")

    clear_files(response_store_filepath, response_success_marker_filepath)
    print(datetime.datetime.now(), "generation of", response_store_filepath, "started")
    w = WaysCollectorHandler()
    w.apply_file(pbf_file_filepath)
    print(datetime.datetime.now(), w.relation_counter, "relations", len(w.ways_needed_by_relations), 'ways in relations gathered')

    with open(response_store_filepath, "w") as myfile:
        csv_shops_file_writer = csv.writer(myfile)
        csv_shops_file_writer.writerow(["lat", "lon", "osm_tags_dict_in_base64", "osm_link"])
        idx = osmium.index.create_map("sparse_file_array," + str(nodecache_file_filepath))
        h = CollectorHandler(idx, w.ways_needed_by_relations)
        h.apply_file(pbf_file_filepath)
    with open(response_success_marker_filepath, "w") as myfile:
        myfile.write("run completed")

def list_shops_based_on_osm_file_path(location_code, pbf_file_filepath, nodecache_file_filepath, path_processing_directory):
    response_store_filepath = output_csv_filepath(path_processing_directory, location_code)
    response_success_marker_filepath = output_csv_success_marker_filepath(path_processing_directory, location_code)
    if response_success_marker_filepath.is_file() != True or response_success_marker_filepath.is_file() != True:
        print(datetime.datetime.now(), "starting generation of listing of shoplike")
        generate_file_with_listing_of_shoplike(pbf_file_filepath, nodecache_file_filepath, response_store_filepath, response_success_marker_filepath, is_shoplike_based_on_this_tag_group)
        print(datetime.datetime.now(), "generation of listing of shoplike completed")
    for entry in load_and_yield_data_from_file(response_store_filepath):
        yield entry

def output_csv_filepath(path_processing_directory, location_code):
    return path_processing_directory / ("shop_listing_" + location_code.replace("/", "-") + ".csv")

def output_csv_success_marker_filepath(path_processing_directory, location_code):
    return path_processing_directory / ("shop_listing_" + location_code.replace("/", "-") + ".csv.success")

def load_and_yield_data_from_file(response_store_filepath):
    with open(response_store_filepath) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        for row in reader:
            yield {"tags": decode_base64_to_dict(row[2]), "center": {'lat': float(row[0]), 'lon': float(row[1])}, "osm_link": row[3]}

def clear_files(response_store_filepath, response_success_marker_filepath):
    if response_store_filepath.is_file():
        response_store_filepath.unlink() #=remove =delete
    if response_success_marker_filepath.is_file():
        response_success_marker_filepath.unlink() #=remove =delete

#gptchat generated
def encode_dict_to_base64(input_dict):
    # Convert the dictionary to a JSON string
    json_str = json.dumps(input_dict)
    # Encode the JSON string to bytes
    json_bytes = json_str.encode('utf-8')
    # Encode the bytes to a Base64 string
    base64_bytes = base64.b64encode(json_bytes)
    # Convert Base64 bytes to a string
    base64_str = base64_bytes.decode('utf-8')
    return base64_str

#gptchat generated
def decode_base64_to_dict(base64_str):
    # Decode the Base64 string to bytes
    base64_bytes = base64_str.encode('utf-8')
    # Decode the bytes to a JSON string
    json_bytes = base64.b64decode(base64_bytes)
    # Convert the JSON bytes to a string
    json_str = json_bytes.decode('utf-8')
    # Convert the JSON string to a dictionary
    output_dict = json.loads(json_str)
    return output_dict
