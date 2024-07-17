import json

FILE_PATH = './data/data.json'

def jsonUpdate():
    try:
        with open(FILE_PATH, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("JSON file not found.")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return

    json_data = {}
    for i in range(len(data)):
        dic = {
            "ID": data[str(i)]["ID"],
            "name": data[str(i)]["name"],
            "imageURL": data[str(i)]["imageURL"],
            "timeStamp": data[str(i)]["timeStamp"],
            "exactTimeLength": data[str(i)]["exactTimeLength"],
            "tags": data[str(i)]['tags'],
            "iFrameURL": data[str(i)]["iFrameURL"],
            "videoURL": data[str(i)]["videoURL"],
            "downloadURL": "",
            "websiteName": data[str(i)]["websiteName"],
            "websiteURL": data[str(i)]["websiteURL"],
        }
        json_data[i] = dic

    print(json_data[0])

    # with open(FILE_PATH, 'w') as f:
    #     json.dump(json_data, f, indent=2)

if __name__ == '__main__':
    jsonUpdate()
