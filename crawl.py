def activate_crawler(target_directory, date_boundary,url):
    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    from deleter import delete_files_in_folder

    # Directory to save the downloaded files
    download_directory = os.path.join(os.getcwd(), target_directory) #Puts shit in current directory
    delete_files_in_folder(target_directory) #Clears the directory.

    # Send a GET request to the URL
    response = requests.get(url) #I think this asks for the html page

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser') #Soup translates it to HTML

    # Find all the <a> tags with href attributes
    links = soup.find_all('a', href=True) #Finds all the links

    # Download each zip file
    for link in links:
        # Get the absolute URL of the zip file
        file_url = urljoin(url, link['href']) #The link will just have the end of the link. Add it to main link.

        # Check if the link points to a zip file
        if file_url.endswith('.zip'):
            numberdate_currentdata = int(((file_url.split("/")[-1]).split("_")[-1]).split(".")[0])
            numberdate_mydata = int((date_boundary.split("/"))[0]+(date_boundary.split("/"))[1]+(date_boundary.split("/"))[2])
            if(numberdate_currentdata>=(numberdate_mydata-1)):
                # Send a GET request to download the file
                file_response = requests.get(file_url)

                # Extract the filename from the URL
                filename = os.path.basename(file_url)

                # Save the file to the download directory
                with open(os.path.join(download_directory, filename), 'wb') as f:
                    f.write(file_response.content)