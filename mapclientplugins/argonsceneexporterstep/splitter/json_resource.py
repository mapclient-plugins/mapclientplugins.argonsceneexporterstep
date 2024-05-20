import argparse
import json
import math
import os
import sys

from mapclientplugins.argonsceneexporterstep.splitter.utilities import convert_to_bytes

FILE_SIZE_LIMIT = 1024 * 1024 * 18

# Threejs face types.
THREEJS_TYPE_TRIANGLE = 0
THREEJS_TYPE_MATERIAL = 2
THREEJS_TYPE_VERTEX_TEX_COORD = 8
THREEJS_TYPE_VERTEX_NORMAL = 32
THREEJS_TYPE_FACE_COLOR = 64
THREEJS_TYPE_VERTEX_COLOR = 128


def _pad_or_truncate(some_list, target_len):
    return some_list[:target_len] + [0]*(target_len - len(some_list))


def _split_file(big_file, splits_required):
    split_files = []

    with open(big_file["full_path"]) as f:
        large_content = json.load(f)

    base_dir = os.path.dirname(big_file["full_path"])
    common_items = {}
    if "metadata" in large_content:
        common_items["metadata"] = large_content["metadata"].copy()
    if "materials" in large_content:
        common_items["materials"] = large_content["materials"].copy()

    vertices = None
    if "vertices" in large_content:
        vertices = large_content["vertices"]

    normals = None
    if "normals" in large_content:
        normals = large_content["normals"]

    colours = None
    if "colors" in large_content:
        colours = large_content["colors"]

    morph_colours = None
    if "morphColors" in large_content:
        morph_colours = large_content["morphColors"]

    chunk_size = None
    faces_len = 0
    if "faces" in large_content:
        faces_len = len(large_content["faces"])
        chunk_size = int(faces_len / splits_required)

    if faces_len == 0:
        print("Help, can only deal with faces!!!")
    else:
        faces = large_content["faces"]
        index = 0
        chunk_progress = 0
        split_faces = []
        split_vertices = []
        split_normals = []
        split_colours = []
        split_morph_colours = []
        current_faces = []
        current_vertices = []
        current_normals = []
        current_colours = []
        if morph_colours is None:
            current_morph_colours = []
        else:
            current_morph_colours = [{} for _ in morph_colours]
        face_vertex_map = {}
        face_normal_map = {}
        face_colour_map = {}
        face_morph_colour_map = {}

        while index < faces_len:
            face_mask = faces[index]
            current_faces.append(face_mask)
            index += 1
            chunk_progress += 1
            if face_mask == THREEJS_TYPE_TRIANGLE:
                # These aren't really triangles they are interpreted as lines so, we can't
                # break on an odd number of vertex pairs.
                current_faces.extend(
                    _map_values(current_vertices, face_vertex_map, faces[index: index + 3], vertices))
                index += 3
                chunk_progress += 3
                if chunk_progress >= chunk_size and index < faces_len:
                    # If we are even do nothing otherwise add one more face on to make it even.
                    even = int(len(current_faces) - len(current_faces) / 4) % 2 == 0
                    if not even:
                        current_faces.extend(
                            _map_values(current_vertices, face_vertex_map, faces[index: index + 3], vertices))
                        index += 3
                        chunk_progress += 3
            elif face_mask == THREEJS_TYPE_VERTEX_NORMAL:
                current_faces.extend(
                    _map_values(current_vertices, face_vertex_map, faces[index: index + 3], vertices))
                index += 3
                chunk_progress += 3
                current_faces.extend(
                    _map_values(current_normals, face_normal_map, faces[index: index + 3], normals))
                index += 3
                chunk_progress += 3
            elif face_mask == (THREEJS_TYPE_VERTEX_NORMAL + THREEJS_TYPE_VERTEX_COLOR):
                current_faces.extend(
                    _map_values(current_vertices, face_vertex_map, faces[index: index + 3], vertices))
                index += 3
                chunk_progress += 3
                current_faces.extend(
                    _map_values(current_normals, face_normal_map, faces[index: index + 3], normals))
                index += 3
                chunk_progress += 3
                current_faces.extend(
                    _map_values(current_colours, face_colour_map, faces[index: index + 3], colours, size=1))
                for source_value in faces[index: index + 3]:
                    if source_value not in face_morph_colour_map:

                        for index_colour, morph_colour in enumerate(morph_colours):
                            if "name" not in current_morph_colours[index_colour]:
                                current_morph_colours[index_colour]["name"] = morph_colours[index_colour]["name"]
                                current_morph_colours[index_colour]["colors"] = []

                            face_morph_colour_map[source_value] = len(current_morph_colours[0]["colors"]) - 1
                            value = morph_colour["colors"][source_value]
                            current_morph_colours[index_colour]["colors"].append(value)

                index += 3
                chunk_progress += 3

            else:
                raise Exception(f"Cannot handle face mask: {face_mask}.")

            if chunk_progress >= chunk_size:
                if len(current_faces):
                    split_faces.append(current_faces[:])
                if len(current_vertices):
                    split_vertices.append(current_vertices[:])
                if len(current_normals):
                    split_normals.append(current_normals[:])
                if len(current_colours):
                    split_colours.append(current_colours[:])
                if len(current_morph_colours):
                    split_morph_colours.append(current_morph_colours.copy())

                chunk_progress = 0
                current_faces = []
                current_vertices = []
                current_normals = []
                current_colours = []
                current_morph_colours = [{}] * (0 if morph_colours is None else len(morph_colours))
                face_vertex_map = {}
                face_normal_map = {}
                face_colour_map = {}
                face_morph_colour_map = {}

        # Mop up any remaining bits and pieces.
        if len(current_faces):
            split_faces.append(current_faces[:])
        if len(current_vertices):
            split_vertices.append(current_vertices[:])
        if len(current_normals):
            split_normals.append(current_normals[:])
        if len(current_colours):
            split_colours.append(current_colours[:])
        if len(current_morph_colours):
            split_morph_colours.append(current_morph_colours.copy())

        for chunk_index, split_face_values in enumerate(split_faces):
            split_data = common_items.copy()

            base_name, ext = os.path.splitext(big_file["URL"])
            split_url = f"{base_name}_split_{chunk_index + 1}{ext}"
            split_files.append(split_url)

            if len(split_vertices):
                split_data["vertices"] = split_vertices[chunk_index]
            if len(split_normals):
                split_data["normals"] = split_normals[chunk_index]
            if len(split_colours):
                split_data["colors"] = split_colours[chunk_index]
            if len(split_morph_colours):
                split_data["morphColors"] = split_morph_colours[chunk_index]
            split_data["faces"] = split_face_values

            split_file = os.path.join(base_dir, split_url)
            with open(split_file, 'w') as f:
                json.dump(split_data, f)

    return split_files


def _list_in(a, b):
    for x in range(len(b) - len(a) + 1):
        if b[x:x + len(a)] == a:
            return x

    return -1


def _map_values(current_values, value_map, source_triple, value_store, size=3):
    """
    Map a triple from the main value_store to the current_values.
    Adding to the current_values from the value_store if a mapped value is not available.

    Returns the mapped values.
    """
    mapped_values = []
    for source_value in source_triple:

        if source_value not in value_map:
            values = value_store[size*source_value:size*source_value + size]

            current_values.extend(values)
            value_map[source_value] = int(len(current_values) / size - 1)

        mapped_values.append(value_map[source_value])

    return mapped_values


def _replace_big_file(meta_content, split_files, url):
    new_meta_content = []
    for item in meta_content:
        if "URL" in item and item["URL"] == url:
            for split_file in split_files:
                new_item = item.copy()
                new_item["URL"] = split_file
                new_meta_content.append(new_item)
        else:
            new_meta_content.append(item)

    return new_meta_content


def split_webgl_output(meta_file, file_size_limit, delete_split_source=False):
    with open(meta_file) as f:
        meta_content = json.load(f)

    meta_dir = os.path.dirname(meta_file)
    big_files = []
    for item in meta_content:
        if "URL" in item:
            resource = os.path.join(meta_dir, item["URL"])
            file_stats = os.stat(resource)
            if file_stats.st_size > file_size_limit:
                big_files.append({
                    "URL": item["URL"],
                    "full_path": resource,
                    "size": file_stats.st_size,
                })

    new_meta_content = meta_content.copy()
    for big_file in big_files:
        size = big_file["size"]
        splits_required = math.ceil(size / file_size_limit)
        split_files = _split_file(big_file, splits_required)
        new_meta_content = _replace_big_file(new_meta_content, split_files, big_file["URL"])
        if delete_split_source:
            os.remove(big_file["full_path"])

    # split_meta_file = os.path.join(meta_dir, 'split_' + os.path.basename(meta_file))
    with open(meta_file, 'w') as f:
        json.dump(new_meta_content, f, indent=4)


def _parse_arguments():
    parser = argparse.ArgumentParser(prog="json_resource_splitter")
    parser.add_argument("webgl_meta", help="A webGL metadata file")
    parser.add_argument("-s", "--size", help="Set text description of split limit, 1MB, 3GB etc.")
    parser.add_argument("-d", "--delete", action="store_true", help="Delete big files that are split", default=False)

    return parser.parse_args()


def main():
    args = _parse_arguments()

    if not os.path.isfile(args.webgl_meta):
        sys.exit(3)

    if args.size:
        size_limit = convert_to_bytes(args.size)
    else:
        size_limit = FILE_SIZE_LIMIT

    split_webgl_output(args.webgl_meta, size_limit, args.delete)


if __name__ == "__main__":
    main()
