from model import Json,JsonException
import pathlib

path = pathlib.Path("tests/step1/")
for file in path.iterdir():
    print(file)
    try:
        with file.open(mode='r',encoding='utf-8') as f:
            json_string = f.read()
            json_obj = Json(json_string)
            json_obj.object_parser()
    except JsonException as je:
        print(f"Json Error in file {file}: {je}")
    except :  # Catch any other unexpected errors
        pass