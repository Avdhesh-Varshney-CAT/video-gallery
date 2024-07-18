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

    json_data = []
    for i in range(len(data)):
        dic = {
            "ID": data[i]["ID"],
            "name": data[i]["name"],
            "boyName": data[i]['boyName'],
            "girlName": data[i]['girlName'],
            "imageURL": data[i]["imageURL"],
            "timeStamp": data[i]["timeStamp"],
            "tags": data[i]['tags'],
            "iFrameURL": data[i]["iFrameURL"],
            "videoURL": data[i]["videoURL"],
            "downloadURL": data[i]['downloadURL'],
            "websiteName": data[i]["websiteName"],
            "websiteURL": data[i]["websiteURL"],
        }
        json_data.append(dic)

    print(json_data[0])

    # with open(FILE_PATH, 'w') as f:
    #     json.dump(json_data, f, indent=2)

if __name__ == '__main__':
    jsonUpdate()
