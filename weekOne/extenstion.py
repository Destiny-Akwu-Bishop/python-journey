#Program used to find the sort of image file a document is

file_name = input("File name: ")

if file_name.endswith("gif"):
    print("Image/gif")
elif file_name.endswith("jpg"):
    print("Image/jpg")
elif file_name.endswith("jpeg"):
    print("Image/jpeg")
elif file_name.endswith("png"):
    print("Image/png")
elif file_name.endswith("pdf"):
    print("Application/pdf")
elif file_name.endswith("txt"):
    print("Application/txt")
elif file_name.endswith("zip"):
    print("folder/zip")
else:
    print("application/octect-stream")