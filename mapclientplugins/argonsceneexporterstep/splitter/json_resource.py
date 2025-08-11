import argparse
import json
import math
import os
import sys

from mapclientplugins.argonsceneexporterstep.splitter.utilities import convert_to_bytes

FILE_SIZE_LIMIT = 1024 * 1024 * 18

# Threejs types.
THREEJS_TYPE_TRIANGLE = 0
THREEJS_TYPE_MATERIAL = 2
THREEJS_TYPE_VERTEX_TEX_COORD = 8
THREEJS_TYPE_VERTEX_NORMAL = 32
THREEJS_TYPE_FACE_COLOUR = 64
THREEJS_TYPE_VERTEX_COLOUR = 128


def _pad_or_truncate(some_list, target_len):
    return some_list[:target_len] + [0] * (target_len - len(some_list))


def _split_file(big_file, splits_required):
    split_files = []

    with open(big_file["full_path"]) as f:
        large_content = json.load(f)

    base_dir = os.path.dirname(big_file["full_path"])

    common_items = {}
    for common_key in ["metadata", "materials"]:
        if common_key in large_content:
            common_items[common_key] = large_content[common_key].copy()

    faces = large_content.get("faces", None)
    vertices = large_content.get("vertices", None)
    normals = large_content.get("normals", None)
    colours = large_content.get("colors", None)
    uvs = large_content.get("uvs", None)
    morph_colours = large_content.get("morphColors", None)

    if faces is None:
        raise Exception("Help, can only deal with faces!!!")
    else:
        data_len = len(faces)
        chunk_size = data_len // splits_required
        index = 0
        chunk_progress = 0

        split_faces = []
        split_vertices = []
        split_normals = []
        split_colours = []
        split_uvs = []
        split_morph_colours = []
        current_faces = []
        current_vertices = []
        current_normals = []
        current_colours = []
        current_uvs = []
        morph_colours_count = 0 if morph_colours is None else len(morph_colours)
        current_morph_colours = [{} for _ in range(morph_colours_count)]
        face_vertex_map = {}
        face_normal_map = {}
        face_colour_map = {}
        face_uvs_map = {}
        face_morph_colour_map = {}

        while index < data_len:
            face_mask = faces[index]
            current_faces.append(face_mask)
            index += 1
            chunk_progress += 1
            # We always have vertices.
            current_faces.extend(
                _map_values(current_vertices, face_vertex_map, faces[index: index + 3], vertices))
            index += 3
            chunk_progress += 3
            if face_mask == THREEJS_TYPE_TRIANGLE and chunk_progress >= chunk_size and index < data_len:
                # These aren't really triangles they are interpreted as lines so, we can't
                # break on an odd number of vertex pairs.
                # If we are even do nothing otherwise add one more face on to make it even.
                even = int(len(current_faces) - len(current_faces) / 4) % 2 == 0
                if not even:
                    current_faces.extend(
                        _map_values(current_vertices, face_vertex_map, faces[index: index + 3], vertices))
                    index += 3
                    chunk_progress += 3
            if face_mask & THREEJS_TYPE_VERTEX_NORMAL:
                current_faces.extend(
                    _map_values(current_normals, face_normal_map, faces[index: index + 3], normals))
                index += 3
                chunk_progress += 3
            if face_mask & THREEJS_TYPE_VERTEX_COLOUR:
                current_faces.extend(
                    _map_values(current_colours, face_colour_map, faces[index: index + 3], colours, size=1))
                _update_morph_colours(current_morph_colours, face_morph_colour_map, faces, index, morph_colours)
                index += 3
                chunk_progress += 3
            if face_mask & THREEJS_TYPE_VERTEX_TEX_COORD:
                current_faces.extend(
                    _map_values(current_uvs, face_uvs_map, faces[index: index + 3], uvs[0], size=2))
                index += 3
                chunk_progress += 3
            if face_mask & THREEJS_TYPE_FACE_COLOUR:
                raise Exception(f"Cannot handle face mask: {face_mask}. Not dealing with {THREEJS_TYPE_FACE_COLOUR}")
            if face_mask & THREEJS_TYPE_MATERIAL:
                raise Exception(f"Cannot handle face mask: {face_mask}. Not dealing with {THREEJS_TYPE_MATERIAL}")

            if chunk_progress >= chunk_size:
                if len(current_faces):
                    split_faces.append(current_faces[:])
                if len(current_vertices):
                    split_vertices.append(current_vertices[:])
                if len(current_normals):
                    split_normals.append(current_normals[:])
                if len(current_colours):
                    split_colours.append(current_colours[:])
                if len(current_uvs):
                    split_uvs.append(current_uvs[:])
                if len(current_morph_colours):
                    split_morph_colours.append(current_morph_colours.copy())

                chunk_progress = 0
                current_faces = []
                current_vertices = []
                current_normals = []
                current_colours = []
                current_uvs = []
                current_morph_colours = [{} for _ in range(morph_colours_count)]
                face_vertex_map = {}
                face_normal_map = {}
                face_colour_map = {}
                face_uvs_map = {}
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
        if len(current_uvs):
            split_uvs.append(current_uvs[:])
        if len(current_morph_colours):
            split_morph_colours.append(current_morph_colours.copy())

        for chunk_index, split_face_values in enumerate(split_faces):
            split_data = common_items.copy()

            base_name, ext = os.path.splitext(big_file["URL"])
            split_url = f"{base_name}_split_{chunk_index + 1}{ext}"
            split_files.append(split_url)

            split_data["faces"] = split_face_values
            if len(split_vertices):
                split_data["vertices"] = split_vertices[chunk_index]
            if len(split_normals):
                split_data["normals"] = split_normals[chunk_index]
            if len(split_colours):
                split_data["colors"] = split_colours[chunk_index]
            if len(split_uvs):
                split_data["uvs"] = [split_uvs[chunk_index]]
            if len(split_morph_colours):
                split_data["morphColors"] = split_morph_colours[chunk_index]

            split_file = os.path.join(base_dir, split_url)
            with open(split_file, 'w') as f:
                json.dump(split_data, f)

    return split_files


def _update_morph_colours(current_morph_colours, face_morph_colour_map, faces, index, morph_colours):
    if morph_colours is not None:
        for source_value in faces[index: index + 3]:
            if source_value not in face_morph_colour_map:

                for index_colour, morph_colour in enumerate(morph_colours):
                    if "name" not in current_morph_colours[index_colour]:
                        current_morph_colours[index_colour]["name"] = morph_colours[index_colour]["name"]
                        current_morph_colours[index_colour]["colors"] = []

                    face_morph_colour_map[source_value] = len(current_morph_colours[0]["colors"]) - 1
                    value = morph_colour["colors"][source_value]
                    current_morph_colours[index_colour]["colors"].append(value)


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
            values = value_store[size * source_value:size * source_value + size]

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


def _is_useful_resource(item, lod=False):
    type_valid = True if lod else ("Type" in item and item["Type"] != "View")
    if "URL" in item and type_valid:
        return not isinstance(item["URL"], list)
    return False


def _analyse_resources(meta_content, meta_dir):
    analysed_files = []
    for index, item in enumerate(meta_content):
        if _is_useful_resource(item):
            resource = os.path.join(meta_dir, item["URL"])
            file_stats = os.stat(resource)
            analysed_files.append({
                "URL": item["URL"],
                "full_path": resource,
                "size": file_stats.st_size,
                "meta_index": index,
            })
            if "LOD" in item and "Levels" in item["LOD"]:
                for level in item["LOD"]["Levels"]:
                    if _is_useful_resource(item["LOD"]["Levels"][level], lod=True):
                        if "LOD" not in analysed_files[-1]:
                            analysed_files[-1]["LOD"] = {}
                            analysed_files[-1]["LOD"]["Levels"] = {}
                        resource = os.path.join(meta_dir, item["LOD"]["Levels"][level]["URL"])
                        file_stats = os.stat(resource)
                        analysed_files[-1]["LOD"]["Levels"][level] = {
                            "URL": item["LOD"]["Levels"][level]["URL"],
                            "full_path": resource,
                            "size": file_stats.st_size,
                        }

    return analysed_files


def split_webgl_output(meta_file, file_size_limit, delete_split_source=False):
    with open(meta_file) as f:
        meta_content = json.load(f)

    meta_dir = os.path.dirname(meta_file)
    analysed_resources = _analyse_resources(meta_content, meta_dir)

    new_meta_content = meta_content.copy()
    for resource in analysed_resources:
        size = resource["size"]
        if size > file_size_limit:
            splits_required = math.ceil(size / file_size_limit)
            split_files = _split_file(resource, splits_required)
            new_meta_content[resource["meta_index"]]["URL"] = split_files
            if delete_split_source:
                os.remove(resource["full_path"])
        if "LOD" in resource:
            for level in resource["LOD"]["Levels"]:
                size = resource["LOD"]["Levels"][level]["size"]
                if size > file_size_limit:
                    splits_required = math.ceil(size / file_size_limit)
                    split_files = _split_file(resource["LOD"]["Levels"][level], splits_required)
                    new_meta_content[resource["meta_index"]]["LOD"]["Levels"][level]["URL"] = split_files
                    if delete_split_source:
                        os.remove(resource["LOD"]["Levels"][level]["full_path"])

    # split_meta_file = os.path.join(meta_dir, 'split_' + os.path.basename(meta_file))
    with open(meta_file, 'w') as f:
        json.dump(new_meta_content, f, default=lambda o: o.__dict__, sort_keys=True, indent=2)


def _combination_file_name(url, index):
    base_name, ext = os.path.splitext(url)
    combined_url = f"{base_name}_combination_{index + 1}{ext}"
    return combined_url


def combine_webgl_output(meta_file, file_size_limit, delete_combined_source=False):
    with open(meta_file) as f:
        meta_content = json.load(f)

    meta_dir = os.path.dirname(meta_file)
    analysed_resources = _analyse_resources(meta_content, meta_dir)

    new_meta_content = meta_content.copy()

    resources = {
        "none": [],
    }

    for resource in analysed_resources:
        resources["none"].append(resource)
        if "LOD" in resource:
            for level in resource["LOD"]["Levels"]:
                lod_resource = resource["LOD"]["Levels"][level]
                lod_resource["meta_index"] = resource["meta_index"]
                if level not in resources:
                    resources[level] = []

                resources[level].append(lod_resource)

    combine = {}
    for key in resources:
        level_data = sorted(resources[key], key=lambda entry: entry['size'])
        sizes = [d['size'] for d in level_data]

        total = 0
        count = 0

        if key not in combine:
            combine[key] = []

        stack = []
        for i, s in enumerate(sizes):
            if total + s < file_size_limit:
                count += 1
                total += s
                stack.append(level_data[i])
            else:
                if count < 2:
                    break

                combine[key].append(stack)
                stack = [level_data[i]]
                total = s
                count = 1

        if count > 1:
            combine[key].append(stack)

    for key in combine:
        for i, combine_resources in enumerate(combine[key]):
            filename = _combination_file_name(combine_resources[0]["URL"], i)
            combine_filenames = []  # resource["full_path"] for resource in combine_resources]
            for j, resource in enumerate(combine_resources):
                combine_filenames.append(resource["full_path"])
                if key == 'none':
                    new_meta_content[resource["meta_index"]]["URL"] = filename
                    new_meta_content[resource["meta_index"]]["Index"] = j
                else:
                    new_meta_content[resource["meta_index"]]["LOD"]["Levels"][key]["URL"] = filename
                    new_meta_content[resource["meta_index"]]["LOD"]["Levels"][key]["Index"] = j

            _combine_data_files(combine_filenames, filename, delete_combined_source, meta_dir)

    with open(meta_file, 'w') as f:
        json.dump(new_meta_content, f, default=lambda o: o.__dict__, sort_keys=True, indent=2)


def _combine_data_files(combined_files, current_combination_filename, delete_combined_source, meta_dir):
    if len(combined_files):
        combined_data = []
        for _file in combined_files:
            with open(_file) as fh:
                data = json.load(fh)
            combined_data.append(data)

            if delete_combined_source:
                os.remove(_file)

        with open(os.path.join(meta_dir, current_combination_filename), "w") as fh:
            json.dump(combined_data, fh)


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
