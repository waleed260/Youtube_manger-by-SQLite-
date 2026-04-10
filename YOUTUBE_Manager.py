
                
import sqlite3

conn=sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()
cursor.execute(""" 
             CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
                )  
              """)
def list_Videos():
    cursor.execute("Select * FROM videos ")
    for row in cursor.fetchall():
        print(row)
        



def add_video(name , time):
    cursor.execute("Insert into videos (name , time) VALUES (?,?)", (name, time))
    # cursor.execute("UPDATE VIDEOS SET name = ? , time = ? where id = ?",() )
    conn.commit()
    
    
    
 
 
def update_Videos(Video_id,new_name,new_time):
    cursor.execute( "UPDATE VIDEOS SET name = ?, time =? where id ",(new_name,new_time, Video_id))
    conn.commit()
 
def Delete_Videos(video_id):
    cursor.execute("DELETE FROM videos where id = ?",(video_id,))
    conn.commit()
    
def main():
    while True:
         print("\n Youtube manager app with DB")
         print("1. List Videos  ")
         print("2. Add Videos ")
         print("3. Update Videos ")
         print("4. Delete Videos ")
         print("5. exit app")
         choice=input("enter your choice:")
            
         if choice == "1":
             list_Videos()
         elif choice == "2":
             name=input("Enter the video name:")
             Time=input("Enter the video time:" )
             add_video(name , Time)
         elif choice == "3":
             
            video_id =input("Enter video id to Update:")
            name=input("Enter the video name:")
            Time=input("Enter the video time:" )
            update_Videos(video_id,name , Time)
         elif choice == "4":
             
            video_id =input("Enter video id to Delete:")
          
            Delete_Videos(video_id)
         elif choice == "5":
             break
         else:
             print("invalid choice")
             
    conn.close()
if __name__ == "__main__":
    main()
