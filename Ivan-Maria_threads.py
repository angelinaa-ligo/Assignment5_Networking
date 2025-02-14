import requests, time, argparse, os, threading

#part A
def download_file(url, pathname):
    response = requests.get(url, stream=True)
    response.raise_for_status() #raise error 
    if response.status_code == 200:
        with open(pathname, 'wb') as fd:
            fd.write(response.content)
        print(f"Image downloaded and saved in {pathname}")
    else:
        print("Failed to download file")

#part B
def download_multiple_images():
    urls = [
        'https://th.bing.com/th/id/OIP.MhwSzfXnBG1MpuuA6IFi-AAAAA?w=218&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.m8b7Y9-81Q4UMCBMaFkw2QAAAA?w=198&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.XN9D7tH47WNJ8h214YgqTwAAAA?w=220&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.cFvfW8dARmuVtR3zOxfTSAHaE9?w=274&h=183&c=7&r=0&o=5&pid=1.7',
        'https://www.southernliving.com/thmb/xFlQn020pc1NJAl4ksr7_o_B5u4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-598083938-1-22dab883ff2a43d8b2751d9f363f2d5d.jpg', 
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj0y6Vhjobxd6Bkhwc5tQ8qHR4yXifC_oovQ&s', 
        'https://th.bing.com/th/id/OIP.JYXSCIpGskpiOxYTw1vuwgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.QjWOHkojgYSz1LhaypSB-gAAAA?w=190&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.Wlfm_lF4VWlYLiPNfbmbDwHaHa?w=181&h=181&c=7&r=0&o=5&pid=1.7',
        'https://www.aaronreedphotography.com/images/xl/Sweet-Dreams-2022.jpg',
        'https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg', 
        'https://th.bing.com/th/id/OIP.A7o1Bm-XNr9A_4pLPCCujgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.oSjt2rY3YUScDY7pw3b1WAHaFj?w=236&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.AroTG9KnmisPIhICyGjoDAHaFj?w=223&h=180&c=7&r=0&o=5&pid=1.7',
        'https://images.squarespace-cdn.com/content/v1/56bf55504c2f85a60a9b9fe5/1456362861375-B3ABTH337NGBFYQBUCUZ/image-asset.jpeg', 
        'https://th.bing.com/th/id/OIP.pGTxkbwreLj7l2ORZrtA8gAAAA?w=147&h=184&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.5SaLUh616MU7KDIP2_0VCwAAAA?w=204&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.S-lrZd2TFhSEpI3VRQyKqQAAAA?w=173&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.sDmZWxXBrF329vZvDu2HrAAAAA?w=266&h=180&c=7&r=0&o=5&pid=1.7',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT72QvkYm_YieHQQN2q2ppP8CevbdHj-Xpi3A&s', 
        'https://whs-blogs.co.uk/teaching/wp-content/uploads/2021/04/pexels-pixabay-37534-2000x1200.jpg', 
        'https://hatrabbits.com/wp-content/uploads/2017/01/random.jpg', 
        'https://th.bing.com/th/id/OIP.MksSZEmu5Cgly2HNvRp4NQAAAA?w=180&h=163&c=7&r=0&o=5&pid=1.7',
        'https://images.contentstack.io/v3/assets/bltcedd8dbd5891265b/blt4a4af7e6facea579/6668df6ceca9a600983250ac/beautiful-flowers-hero.jpg?q=70&width=3840&auto=webp'
    ]
    folder = "Images"
    if not os.path.exists(folder):  #checking if the folder exists 
        os.makedirs(folder)

    start_time = time.perf_counter() 
    for index, url in enumerate(urls):
        filename = os.path.join(folder, f"image_{index + 1}.jpg")
        download_file(url, filename)  #part A function
    end_time = time.perf_counter() 
    elapsed_time = int(end_time - start_time) * 1000 #miliseconds
    print(f"Sequential download completed in {elapsed_time} miliseconds")

#part C
def download_images_threaded():
    urls = [
        'https://th.bing.com/th/id/OIP.MhwSzfXnBG1MpuuA6IFi-AAAAA?w=218&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.m8b7Y9-81Q4UMCBMaFkw2QAAAA?w=198&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.XN9D7tH47WNJ8h214YgqTwAAAA?w=220&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.cFvfW8dARmuVtR3zOxfTSAHaE9?w=274&h=183&c=7&r=0&o=5&pid=1.7',
        'https://www.southernliving.com/thmb/xFlQn020pc1NJAl4ksr7_o_B5u4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-598083938-1-22dab883ff2a43d8b2751d9f363f2d5d.jpg', 
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj0y6Vhjobxd6Bkhwc5tQ8qHR4yXifC_oovQ&s', 
        'https://th.bing.com/th/id/OIP.JYXSCIpGskpiOxYTw1vuwgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.QjWOHkojgYSz1LhaypSB-gAAAA?w=190&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.Wlfm_lF4VWlYLiPNfbmbDwHaHa?w=181&h=181&c=7&r=0&o=5&pid=1.7',
        'https://www.aaronreedphotography.com/images/xl/Sweet-Dreams-2022.jpg',
        'https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg', 
        'https://th.bing.com/th/id/OIP.A7o1Bm-XNr9A_4pLPCCujgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.oSjt2rY3YUScDY7pw3b1WAHaFj?w=236&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.AroTG9KnmisPIhICyGjoDAHaFj?w=223&h=180&c=7&r=0&o=5&pid=1.7',
        'https://images.squarespace-cdn.com/content/v1/56bf55504c2f85a60a9b9fe5/1456362861375-B3ABTH337NGBFYQBUCUZ/image-asset.jpeg', 
        'https://th.bing.com/th/id/OIP.pGTxkbwreLj7l2ORZrtA8gAAAA?w=147&h=184&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.5SaLUh616MU7KDIP2_0VCwAAAA?w=204&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.S-lrZd2TFhSEpI3VRQyKqQAAAA?w=173&h=180&c=7&r=0&o=5&pid=1.7',
        'https://th.bing.com/th/id/OIP.sDmZWxXBrF329vZvDu2HrAAAAA?w=266&h=180&c=7&r=0&o=5&pid=1.7',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT72QvkYm_YieHQQN2q2ppP8CevbdHj-Xpi3A&s', 
        'https://whs-blogs.co.uk/teaching/wp-content/uploads/2021/04/pexels-pixabay-37534-2000x1200.jpg', 
        'https://hatrabbits.com/wp-content/uploads/2017/01/random.jpg', 
        'https://th.bing.com/th/id/OIP.MksSZEmu5Cgly2HNvRp4NQAAAA?w=180&h=163&c=7&r=0&o=5&pid=1.7',
        'https://images.contentstack.io/v3/assets/bltcedd8dbd5891265b/blt4a4af7e6facea579/6668df6ceca9a600983250ac/beautiful-flowers-hero.jpg?q=70&width=3840&auto=webp'
    ]
    folder = "Images"
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    start_time = time.perf_counter()
    threads = []
    for index, url in enumerate(urls):
        filename = os.path.join(folder, f"image_{index + 1}.jpg")
        thread = threading.Thread(target = download_file, args = (url, filename))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
    
    end_time = time.perf_counter()
    elapsed_time = int((end_time - start_time) * 1000)
    print(f"Threaded download completed in {elapsed_time} milliseconds")   
    
#part D
def main():
    parser = argparse.ArgumentParser(description = "Download images using threads or sequentially.")
    parser.add_argument("mode", choices=["serial", "threaded"], help="Choose (serial) for sequential download or (threaded) for multi-threaded download.")
    parser.add_argument("--folder", default = "Images", help = "Please select a folder to save an images.")
    args = parser.parse_args()
    
    if args.mode == "serial":
        download_multiple_images()
    elif args.mode == "threaded":
        download_images_threaded()
        
if __name__ == "__main__":
    main()

# #part A
# image_url='https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7'
# pathname = r'Images\image_partA.jpg'
# print("Part A:")
# download_file(image_url, pathname)

# #part B 
# print("Part B:")
# download_multiple_images()

# #part C
# print("Part C:")
# download_images_threaded()