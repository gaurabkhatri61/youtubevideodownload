import webbrowser
import pyautogui
import time

def youtube():
    choice = input("Enter 'Video' for video, 'Channel' for channel name, or 'Download' for Download: ")

    if choice == 'Video':
        video_link = input("Enter the link: ")
        webbrowser.open(video_link)

    elif choice == "Channel":
        channel_name = input("Enter the channel name: ")
        webbrowser.open(f"https://www.youtube.com/@{channel_name}")

    else:
        video_link = input('Enter the link of the video you want to download: ')
        position = 12
        download_link = video_link[:position] + "ss" + video_link[position:]
        webbrowser.open(download_link)

        # positions for clicks
        positions = [
            (1050, 750),  
            (1050, 770),  
            (1350, 770),  
            (1320, 650)   
        ]

        def auto_click(position_index):
            try:
                if 0 <= position_index < len(positions):
                    x, y = positions[position_index]

                    if position_index == 0:
                        time.sleep(10)  # 5 sec delay

                    pyautogui.moveTo(x, y, duration=0.5)
                    pyautogui.click()
                    print(f"Clicked at position: {positions[position_index]}")

                    # flow of clicks
                    if position_index < len(positions) - 1:
                        time.sleep(1)  # 2 sec delay
                        auto_click(position_index + 1)  
                else:
                    print("Index out of bounds")
            except Exception as e:
                print(f"Error occurred: {e}")

        auto_click(0)

if __name__ == "__main__":
    youtube()
