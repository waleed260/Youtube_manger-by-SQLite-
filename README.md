🎬 YouTube Video Manager (SQLite Version)

A simple command-line YouTube Video Manager built with Python and SQLite.
This program lets you add, view, update, and delete video records from a local SQLite database — acting like a mini CRUD (Create, Read, Update, Delete) system for managing your video collection.

📋 Features

✅ Create and store videos with name and duration
✅ View all videos stored in the database
✅ Update existing video records
✅ Delete unwanted videos
✅ Data persistence using SQLite
✅ Simple and interactive command-line menu

🛠️ Requirements

Python 3.7+

SQLite (comes built-in with Python)

🚀 Setup Instructions

Clone or Download this repository to your computer:

git clone https://github.com/yourusername/youtube-manager.git
cd youtube-manager


Run the Python script:

python youtube_manager.py


The app will automatically create a database file called youtube_videos.db in the same directory.

🧠 How It Works

The program uses an SQLite database to store video information.

Field	Type	Description
id	INTEGER (Primary Key)	Auto-incremented ID for each video
name	TEXT	Video title
time	TEXT	Duration or length of the video
💡 Usage Example

When you run the program, you’ll see:

YouTube Manager App with DB
1. List Videos
2. Add Video
3. Update Video
4. Delete Video
5. Exit App
Enter your choice:


Example workflow:

Enter your choice: 2
Enter the video name: Python Tutorial
Enter the video time: 15:30

Video added successfully!


Then choose 1 to list all videos:

(1, 'Python Tutorial', '15:30')

🧰 Code Overview

Database setup: Creates a table videos if it doesn’t exist.

Functions:

add_video(name, time) → Add a new video.

list_Videos() → Show all videos.

update_Videos(video_id, new_name, new_time) → Modify an existing record.

Delete_Videos(video_id) → Delete a video by ID.

Menu loop: Provides a text interface for easy use.

⚠️ Common Fixes & Tips
🧩 1. Fixing the Update Function

In your code:

cursor.execute( "UPDATE VIDEOS SET name = ?, time =? where id ", (new_name, new_time, Video_id))


should be:

cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, Video_id))


Missing = ? in the WHERE clause — without it, the update won’t work correctly.

🧼 2. Improve Display Format

You can format the list output for better readability:

def list_Videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    if not videos:
        print("No videos found.")
    else:
        print("\nID | Name | Duration")
        print("-" * 30)
        for vid in videos:
            print(f"{vid[0]} | {vid[1]} | {vid[2]}")
🗂️ 3. Handle Invalid Inputs
Wrap critical sections in try/except blocks to avoid crashes:

try:
    video_id = int(input("Enter video ID: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    return

💾 4. Backup Your Database

You can easily back up your database by copying the .db file:

cp youtube_videos.db backup_youtube_videos.db

🌟 5. Possible Future Enhancements

Add search functionality by video name.

Export the video list to a CSV or JSON file.

Use argparse to make it runnable with command-line options.

Add timestamps for when each video was added.

Build a simple Tkinter or Flask web interface for GUI lovers.


