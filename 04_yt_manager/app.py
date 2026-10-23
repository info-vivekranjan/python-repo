"""
## Enumerate

users = ["Vivek Ranjan", "Ajey Kumar", "Prashant Sharma"]
scores = [800, 632, 875]
for index, (item, score) in enumerate(zip(users, scores), start=1):
    print(index, item, score) 
"""

yt_list = [{"id": 1, "video_url":"video url 1"}, {"id": 2, "video_url":"video url 2"}]

def list_all_videos(data):
    print(data)

def add_video(video_name):

    yt_list.append({"id": len(yt_list) + 1, "video_url":f"Video url - {video_name} - {len(yt_list) + 1}"})

def edit_video(id, video_name):
    print("Video to be edited - ", id)
    selected_video = yt_list[int(id)]
    selected_video["video_url"] = video_name


def delete_video(id):
    print("Video to be deleted - ", id)
    yt_list.pop(int(id))


def main():

    while True:
        print("YT Manager | Choose an option")
        print("1. List all YT videos")
        print("2. Create a YT video")
        print("3. Edit a YT video")
        print("4. Delete a YT video")
        print("5. Exit")

        choice = input("Select an option - ")

        match choice:
            case "1":
                print("Listing all YT videos")
                list_all_videos(yt_list)
            case "2":
                print("Creating an YT video")
                video_name=input("Add Video name : ")
                add_video(video_name)
                list_all_videos()

            case "3":
                video_index = input("Choose video index/id - ")
                video_name=input("Add Video name : ")
                edit_video(video_index, video_name)
                print("Editing Done!!!")

            case "4":
                video_index = input("Choose video index/id - ")
                delete_video(video_index)
                print("Deleting...")


            case "5":
                print("Exiting...")
                break
            case _:
                print("====================Invalid Request=====================")

if __name__ == "__main__":
    main()