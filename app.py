import os
import tkinter as tk
from PIL import Image, ImageTk
from detection_service import startapplication
from tkinter import filedialog

video_path = None

# Predefined username and password
correct_username = "Yassine"
correct_password = "1234"

def submit():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == correct_username and password == correct_password:
        print("Login successful!")
        create_menu()
    else:
        print("Invalid username or password")

def create_menu():
    # Function to create the menu after successful login
    # Destroy previous widgets
    hello_label.destroy()
    username_label.destroy()
    password_label.destroy()
    username_entry.destroy()
    password_entry.destroy()
    submit_button.destroy()
    
    root.title("Menu")

    # Create menu labels and buttons
    menu_title = tk.Label(root, text="Menu", font=("Helvetica", 16))
    menu_title.place(relx=0.5, rely=0.2, anchor="center")
    
    u_label = tk.Label(root, text="User : {}".format(correct_username), bg="green")
    u_label.pack()

    button1 = tk.Button(root, text="Detect Accidents", command=detect_accidents, height=1, width=23)
    button1.place(relx=0.5, rely=0.4, anchor="center")

    button2 = tk.Button(root, text="Real time detection", command=real_time_detection, height=1, width=23)
    button2.place(relx=0.5, rely=0.5, anchor="center")

    button3 = tk.Button(root, text="Images of Accidents", command=open_image_gallery, height=1, width=23)
    button3.place(relx=0.5, rely=0.6, anchor="center")

    # button4 = tk.Button(root, text="Settings", command=open_settings, height=1, width=23)
    # button4.place(relx=0.5, rely=0.7, anchor="center")

    button5 = tk.Button(root, text="Exit", command=root.destroy, height=1, width=23, bg="red")
    button5.place(relx=0.5, rely=0.7, anchor="center")

def real_time_detection():
    startapplication(0)

def detect_accidents():
    global video_path
    file_path = filedialog.askopenfilename(title="Select a Video File",
                                            filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
    print(">>> ",file_path)
    if file_path:
        startapplication(file_path)

def open_settings():
    # Function to open settings window
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    
    # Set window size
    settings_window.geometry("800x450")


def open_image_gallery():
    # Function to open image gallery window
    gallery_window = tk.Toplevel(root)
    gallery_window.title("Image Gallery")
    
    # Set window size
    gallery_window.geometry("1120x780")
    
    # Load images
    directory_path = "./Accidents_Screen"
    image_files = sorted([f for f in os.listdir(directory_path) if f.endswith((".png", ".jpg", ".jpeg"))])
    image_paths = [os.path.join(directory_path, f) for f in image_files]
    images = [Image.open(path) for path in image_paths]
    photo_images = [ImageTk.PhotoImage(image) for image in images]

    def show_image(index):
        # Function to display image with index
        current_image = images[index]
        label.config(image=photo_images[index])
        label.image = photo_images[index]
        label.pack()
        # Update label with current image number
        image_number_label.config(text="Image {} of {}".format(index + 1, len(image_paths)))

    def on_select(event):
        # Function to handle image selection from the listbox
        widget = event.widget
        index = int(widget.curselection()[0])
        show_image(index)

    label = tk.Label(gallery_window)

    # Create a listbox to display image names
    listbox = tk.Listbox(gallery_window, selectmode=tk.SINGLE)
    for file_name in image_files:
        listbox.insert(tk.END, file_name)
    listbox.pack(side=tk.LEFT, fill=tk.Y)
    listbox.bind("<<ListboxSelect>>", on_select)

    # Create a scrollbar for the listbox
    scrollbar = tk.Scrollbar(gallery_window, orient=tk.VERTICAL)
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)

    # Label to display image number
    image_number_label = tk.Label(gallery_window, text="Image 1 of {}".format(len(image_paths)))
    image_number_label.pack()

# Create main window
root = tk.Tk()
root.title("Login")

# Set window size
root.geometry("600x350")


# Load the PNG image
image_path = "./Images/cam_pic33.png"
image = tk.PhotoImage(file=image_path)

# Resize the image
resized_image = image.subsample(2, 2)

# Create a label to display the image
image_label = tk.Label(root, image=resized_image)
image_label.pack(side=tk.TOP, anchor=tk.NE)


# Load the PNG image
image_path2 = "./Images/cam_pic22.png"
image2 = tk.PhotoImage(file=image_path2)

# Resize the image
resized_image2 = image2.subsample(2, 2)

# Create a label to display the image
image_label2 = tk.Label(root, image=resized_image2)
image_label2.pack(side=tk.BOTTOM, anchor=tk.SW)

# Create labels
hello_label = tk.Label(root, text="Login", font=("Helvetica", 16))
hello_label.place(relx=0.5, rely=0.3, anchor="center")

username_label = tk.Label(root, text="Username:")
username_label.place(relx=0.3, rely=0.5, anchor="center")

password_label = tk.Label(root, text="Password:")
password_label.place(relx=0.3, rely=0.6, anchor="center")

# Create entry fields
username_entry = tk.Entry(root)
username_entry.place(relx=0.5, rely=0.5, anchor="center")

password_entry = tk.Entry(root, show="*")
password_entry.place(relx=0.5, rely=0.6, anchor="center")

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.place(relx=0.5, rely=0.7, anchor="center")

# Run the application
def launch_application():
    root.mainloop()
